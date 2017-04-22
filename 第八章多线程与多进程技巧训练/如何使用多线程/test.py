# coding:utf-8
import csv
from xml.etree.ElementTree import Element, ElementTree, tostring
import requests
from StringIO import StringIO
from pretty import pretty
from  threading import Thread


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
def download(url):
    response = requests.get(url, timeout=3)
    if response.ok:
        return StringIO(response.content)


def csvToXml(fname):
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
        # print tostring(et)


def handle(sid):
    print "Download...(%d)" % sid
    url = "http://table.finance.yahoo.com/table.csv?s=000001.sz"
    url %= str(sid).rjust(6, "0")
    rf = download(url)
    if rf is None: return

    print "Convert to XML...(%d)" % sid
    csvToXml(rf)

class MyThread(Thread):
    def __init__(self,sid):
        Thread.__init__(self)
        self.sid=sid
    def run(self):
        handle(self.sid)
if __name__ == "__main__":
    # url="http://table.finance.yahoo.com/table.csv?s=000001.sz"
    # rf=download(url)
    # if rf:
    #     with open("000001.xml",'wb') as wf:
    #         csvToXml(wf)

    for sid in xrange(1, 11):
        print "Download...(%d)" % sid
        url = "http://table.finance.yahoo.com/table.csv?s=000001.sz"
        url %= str(sid).rjust(6, "0")
        rf = download(url)
        if rf is None: continue

        print "Convert to XML...(%d)" % sid
        csvToXml(rf)

    #使用线程方法一
    t=Thread(target=handle,args=(1,))
    t.start()
    #使用线程方法二
    t=MyThread(1)
    t.start()
    t.join()#作用是使主线程等待子线程结束后再退出
    threads=[]
    for i in xrange(1,11):
        t=MyThread(i)
        threads.append(t)
        t.start()
    #主线程等待所有子线程退出
    for t in threads:
        t.join()
    print "in main thread"
#python中的线程只适合处理i/o密集型操作，不适合cpu密集型操作，因为有GIL(全局解释器所)
#所以即使有多个cpu,python解释器一次也只能处理一个线程（串行执行与并行执行效率一样）

#在python中处理i/o密集型任务时单核处理器与多核处理器的效率差不多(商店订货原理)，但在处理
#cpu密集型操作时多核处理器的效率更高(商店搬货原理)

#商店订货原理:商店订货所用时间远比货物送达的时间少得多，也即是cpu在执行下载任务时，
# 发送出下载请求后，在数据返回前线程暂时进入休眠状态，直到数据返回，因此单个cpu,
# 与多个cpu的执行效率差别不大

#商店搬货原理:多个工人搬货的效率，远比一个工人搬货的效率高，即多个cpu比一个cpu的执行效率高，
#因为cpu密集型任务线程不会进入休眠状态


