#coding:utf-8
from multiprocessing import Process,Queue,Pipe
def f(s):
    print s
#进程间数据空间是各自独立的
x=1
def g():
    global x
    x=5
#进程间通信
q=Queue()
def h(q):
    print "start"
    print q.get()
    print "end"

def j(c):
    c.send(c.recv() * 2)

if __name__=="__main__":
    # p=Process(target=f,args=("hello",))
    # p.start()
    # p.join()

    #数据独立
    # g()
    # print x
    # x=1
    # p=Process(target=g)
    # p.start()
    # print x
    #进程间通信
    # p=Process(target=h,args=(q,))
    # p.start()
    # q.put(1)
    #管道pipe使用,管道和队列相似，只是管道是双向的，队列是单向的
    # c1,c2=Pipe()
    # c1.send("abc")
    # print c2.recv()
    # c2.send(123)
    # print c1.recv()
    c1,c2=Pipe()
    p=Process(target=j,args=(c2,))
    p.start()
    c1.send(55)
    print c1.recv()
