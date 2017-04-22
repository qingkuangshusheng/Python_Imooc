#coding:utf-8
from functools import total_ordering#类装饰器
from abc import ABCMeta,abstractmethod#导入定义抽象基类的接口

@total_ordering#使用类装饰器定义两个方法就够了
class Shape(object):
    def __lt__(self, other):#<
        print "in __lt__()"
        return self.area()<other.area()
    def __eq__(self, other):
        print "in __eq__()"
        return self.area()==other.area()
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,w,h):
        self.w=w
        self.h=h
    def area(self):
        return self.w*self.h
    def __lt__(self, other):#<
        print "in __lt__()"
        if not isinstance(other,Shape):
            raise TypeError("other is not shape")
        return self.area()<other.area()
    def __eq__(self, other):
        print "in __eq__()"
        return self.area()==other.area()

# r1=Rectangle(5,3)
# r2=Rectangle(4,4)
# print r1>=r2#r1.__lt__(r2)

class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return self.r ** 2*3.14

r1=Rectangle(5,3)
r2=Rectangle(4,4)
c1=Circle(3)
print c1<=r1#c1.__lt__(r2)
print r1<c1#r1.__lt__(c1)
print r1<34
