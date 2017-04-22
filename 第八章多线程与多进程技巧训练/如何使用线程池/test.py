#coding:utf-8
#环境python3
from concurrent.futures import ThreadPoolExecutor
executor=ThreadPoolExecutor(3)#创建线程池，线程池中线程数量为3
def f(a,b):
    print("f",a,b)
    return a ** b
executor.submit(f,2,3)#启动线程池的一个线程执行函数
future=executor.submit(f,2,4)
future.result()#得到函数返回值，函数没有执行完执行此函数，将阻塞在这里
executor.map(f,[2,3,5],[4,5,6])#开启多个线程同时执行函数
