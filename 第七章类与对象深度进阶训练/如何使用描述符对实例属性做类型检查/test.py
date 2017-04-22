#coding:utf-8
class Attr(object):
    def __init__(self,name,type_):
        self.name=name
        self.type_=type_

    def __get__(self, instance, owner):#p.age,p为instance,owner为p的类名
        # print "int __get__",instance,owner
        return instance.__dict__[self.name]
    #在__set__方法中进行类型检查
    def __set__(self, instance, value):#p.age=18,p即为instance
        print "in __set__"
        if not isinstance(value,self.type_):
            raise TypeError("expected an %s"%self.type_)
        instance.__dict__[self.name]=value

    def __delete__(self, instance):
        # print "in __delete__",
        del instance.__dict__[self.name]

class Person(object):#类实例可以访问类属性，但不可以修改，否则会为实例进行动态属性绑定
    # x=Attr()
    #def __init__(self,name,age,height):
        #变量类型声明，实例变量非类变量
        name=Attr("name",str)
        age=Attr("age",int)
        height=Attr("height",float)


# p=Person()
# p.x=5
# print p.x
# p=Person("bom",18,176.5)
# print p.name,p.age,p.height
p1=Person()
p1.name="tom"#执行p1.name时会执行__set__()方法
print p1.name#会执行__get__()方法

p2=Person()
p2.name="jim"
print p2.name


