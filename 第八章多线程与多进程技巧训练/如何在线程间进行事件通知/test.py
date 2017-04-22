# coding:utf-8
import csv
from xml.etree.ElementTree import Element, ElementTree, tostring
import requests
from StringIO import StringIO
from pretty import pretty
from  threading import Thread,Event
from collections import deque#线程不安全，需要锁操作
from Queue import Queue#标准库中的Queue线程安全，内部实现了锁操作
import tarfile
import os

# e=Element("data")#设置标签
# print e.tag
# e.set("name","abc")#设置属性，得到属性get()
# print tostring(e)
# e.text="123"#设置标签文本
# print tostring(e)
# e2=Element("row")
# e3=Element("open")
# e3.text="8.80"
# e2.append(e3)#将 e3设置为e2的子元素
# # print tostring(e2)
# e.text=None
# e.append(e2)
# # print tostring(e)
# et=ElementTree(e)#创建节点树，将根结点作为参数
# et.write("demo.xml")#将节点树写入文件


# q=deque()#一个进程的多个线程都可以访问全局变量，但设置全局变量是不良的习惯
#生产者与消费者模型
class DownLoadThread(Thread):#生产者
    def __init__(self, sid,queue):
        Thread.__init__(self)
        self.sid = sid
        self.queue=queue#在类的内部维护比使用全局变量好
        self.url = "http://table.finance.yahoo.com/table.csv?s=%s.sz"
        self.url %= str(sid).rjust(6, "0")

    def download(self,url):
        response = requests.get(url, timeout=3)
        if response.ok:
            return StringIO(response.content)
    def run(self):
        #1下载
        data=self.download(self.url)
        #2把(sid,data)传递给Convert线程
        self.queue.put((self.sid,data))
class ConvertThread(Thread):#消费者
    def __init__(self,queue,cEvent,tEvent):
        Thread.__init__(self)
        self.cEvent=cEvent
        self.tEvent=tEvent
        self.queue=queue
    def csvToXml(self,fname):
        with open(fname, "rb") as f:
            reder = csv.reader(f)
            header = reder.next()
            # print header
            root = Element("data")
            for row in reder:
                # print row
                # break
                erow = Element("row")
                root.append(erow)
                for tag, text in zip(header, row):
                    e = Element(tag)
                    e.text = text
                    erow.append(e)
            pretty(root)
            et = ElementTree(root)
            et.write(fname + ".xml")
    def run(self):
        #1接收(sid,data)
        count=0
        while True:
            sid,data=self.queue.get()
            if sid==-1:
                #退出前不足五个的也要打包
                self.tEvent.set()
                self.cEvent.wait()
                break
            if data:
                fname=str(sid).rjust(6,"0")+".xml"
                self.csvToXml(data)
                count+=1
            if count==5:
                self.tEvent.set()
                self.cEvent.wait()
                self.cEvent.clear()

class TarThread(Thread):
    def __init__(self,cEvent,tEvent):
        Thread.__init__(self)
        self.count=0
        self.cEvevt=cEvent
        self.tEvent=tEvent
        self.setDaemon(True)#守护线程，其他线程退出后次线程自动退出

    def tarXML(self):
        self.count+=1
        tfname="%d.tgz"%self.count
        tf=tarfile.open(tfname,"w:gz")
        for fname in os.listdir("."):
            if fname.endswith(".xml"):
                tf.add(fname)
                os.remove(fname)
        tf.close()
        if not tf.members:
            os.remove(tfname)
    def run(self):
        while True:
            self.tEvevt.wait()
            self.tarXML()
            self.tEvevt.clear()#重复使用通知事件
            self.cEvent.set()

if __name__=="__main__":
    q=Queue()
    dThreads=[DownLoadThread(i,q) for i in xrange(1,11)]
    cEvent=Event()
    tEvent=Event()
    cThread=ConvertThread(q,cEvent,tEvent)
    tThread=TarThread(cEvent,tEvent)
    tThread.start()
    for t in dThreads:
        t.start()
    cThread.start()

    for t in dThreads:
        t.join()
    q.put(-1,None)

#两个线程间要都能够独立运行不发生异常，不要相互依赖