#coding:utf-8
from functools import wraps
import time
from random import randint
import logging
#带参数的装饰器,增加了打印超时运行的函数的日志
def warn(timeout):
    timeout=[timeout]
    def decorator(func):
        def wrapper(*args,**kwargs):
            start=time.time()
            res=func(*args,**kwargs)
            used=time.time()-start
            if used>timeout[0]:
                msg="%s:%s>%s"%(func.__name__,used,timeout[0])
                logging.warn(msg)
            return res
        def setTimeout(k):
            timeout[0]=k
        wrapper.setTimeout=setTimeout#向wrapper函数对象中动态添加setTimeout属性
        return wrapper
    return decorator

@warn(1.5)
def test():
    print ("In test")
    while randint(0,1):
        time.sleep(0.5)

for _ in xrange(30):
    test()
test.setTimeout(1)
for _ in xrange(30):
    test()