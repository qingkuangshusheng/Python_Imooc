#coding:utf-8
class IntTuple(tuple):
    def __new__(cls, iterable):#真正的构造器先于__init__调用，并将返回值传入__init__
        g=(x for x in iterable if isinstance(x,int) and x>0)
        return super(IntTuple,cls).__new__(cls,g)
    def __init__(self,iterable):
        #before
        print self#self值为（1，6，3）
        super(IntTuple,self).__init__(iterable)
        #after
        print self #self值为（1，6，3）
t=IntTuple([1,-1,"abc",6,["x","y"],3])
print t

