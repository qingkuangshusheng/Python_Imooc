#coding:utf-8
from threading import Thread
from multiprocessing import Process
import time

#判断水仙花数
def isArmstrong(n):
    a,t=[],n
    while t>0:
        a.append(t%10)
        t/=10
    k=len(a)
    return  sum(x ** k for x in a)==n

def findArmstrong(a,b):
    print a,b
    res=[k for k in xrange(a,b) if isArmstrong(k)]
    print "%s ~ %s: %s"%(a,b,res)

def findByThread(*argsList):
    workers=[]
    for args in argsList:
        worker=Thread(target=findArmstrong,args=args)
        workers.append(worker)
        worker.start()
    for worker in workers:
        worker.join()

def findByProcess(*argsList):
    workers=[]
    for args in argsList:
        worker=Process(target=findArmstrong,args=args)
        workers.append(worker)
        worker.start()
    for worker in workers:
        worker.join()

if __name__=="__main__":
    start=time.time()
    findByProcess((20000000,25000000),(25000000,30000000))#有两个cpu占有率为100%,用时不足20s
    # findByThread((20000000,25000000),(25000000,30000000))#四个cpu占有率都不足50%,用时将近100s
    print time.time()-start
#总结由于进程中GIL锁的原因,一个进程中某个时刻某个获得GIL锁的线程只能获得一个cpu资源
#如果一个电脑有多个cpu，就会造成cpu资源浪费，此时用多进程可以保证某个时刻有多个线程同时运行
#从而对大大提高了程序的运行效率，因此多线程不适用与cpu密集型操作，此时可用多进程

