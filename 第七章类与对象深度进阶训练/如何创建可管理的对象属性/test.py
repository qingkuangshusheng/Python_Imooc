#coding:utf-8
from math import pi

class Circle(object):
    def __init__(self,radius):
        self.radius=radius
    def getRadius(self):
        # return self.radius
        return round(self.radius,2)
    def setRadius(self,value):
        if not isinstance(value,(int ,long,float)):#可传入包含可能对象的元组
            raise ValueError("wrong type")
        self.radius=value
    def getArea(self):
        return self.radius ** 2 * pi

# c=Circle(3.2)
#直接访问属性导致的问题1,不安全
# c.radius="abc"
# d=c.radius*2
# print d#"abcabc",逻辑上错误，但语法没错导致程序能够正常运行，但得出错误的结果
# c.setRadius("abc")
#直接访问属性导致的问题2,不灵活，如改变需求，希望得到的radius是保留两位小数的值
# c.getRadius()#在方法内部改变需求比较方便灵活
#总结直接访问属性简洁，但不够安全和灵活，使用set,get方法访问属性，安全灵活，但不够简洁
#下面是实现简洁安全灵活的属性访问方式
class Circle2(object):
    def __init__(self,radius):
        self.radius=radius
    def getRadius(self):
        # return self.radius
        return round(self.radius,2)
    def setRadius(self,value):
        if not isinstance(value,(int ,long,float)):#可传入包含可能对象的元组
            raise ValueError("wrong type")
        self.radius=value
    def getArea(self):
        return self.radius ** 2 * pi
    R=property(getRadius,setRadius)

c2=Circle2(3.2)
c2.R=5.9
print c2.R



