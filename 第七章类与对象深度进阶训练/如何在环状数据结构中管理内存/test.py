#coding:utf-8
import sys
import gc
import weakref#导入弱引用模块

class A(object):
    def __del__(self):
        print "in A.__del__"

# a=A()
# print sys.getrefcount(a)-1#查看对象的引用计数，对象被引用一次计数加1
# a2=a
# print sys.getrefcount(a)-1
# #当一个对象的引用计数为零时将会被回收
# del a2#计数减一
# print sys.getrefcount(a)-1
# a=5#计数减一

class Data(object):
    def __init__(self,value,owner):
        # self.owner=owner#self.owner引用了Node实例
        self.owner=weakref.ref(owner)#使用弱引用
        self.value=value

    def __str__(self):
        return "%s'data,value is %s"%(self.owner(),self.value)

    def __del__(self):
        print "in Data.__del__"

class Node(object):
    def __init__(self,value):
        self.data=Data(value,self)#self.data引用Data实例
        print self.data.__str__()

    def __del__(self):
        print "in Node.__del__"

# node=Node(100)
# del node#由于循环引用，node实例没有被立即回收
# gc.collect()#强制回收，由于析构函数的存在，并没有被回收
# raw_input("wait...")
#使用弱引用
# a=A()
# print sys.getrefcount(a)-1
# a_wref=weakref.ref(a)
# a2=a_wref()
# # print a2 is a
# print sys.getrefcount(a)-1
# del a
# del a2
# print a_wref() is None
node=Node(100)
del node
