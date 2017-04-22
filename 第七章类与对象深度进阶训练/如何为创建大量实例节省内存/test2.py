#coding:utf-8
from test import Player,Player2
import sys

p1=Player(0001,"jim")
p2=Player2(0001,"jim")
# print set(dir(p1))-set(dir(p2))
# print p1.__dict__#{'status': 0, 'level': 1, 'uid': 1, 'name': 'jim'}
#实例属性的动态绑定
# p1.x=123
# print p1.__dict__#{'status': 0, 'x': 123, 'level': 1, 'uid': 1, 'name': 'jim'}
#逆向仍成立
# p1.__dict__["y"]=99
# print p1.y
#动态删除实例属性
# del p1.__dict__["x"]
# print p1.x#AttributeError: 'Player' object has no attribute 'x'
#实例的__dict__字典属性主要是为了维护实例的内部属性，便于实例属性的动态绑定与删除，但增大了内存开销
# print sys.getsizeof(p1.__dict__)#获取实例或其属性所占内存
#p2关闭了动态绑定属性的特性
# print sys.getsizeof(p2.__dict__)#AttributeError: 'Player2' object has no attribute '__dict__'
# p2.x=123#AttributeError: 'Player2' object has no attribute 'x'
print sys.getsizeof(p1)#56
print sys.getsizeof(p2)#72
#总结:如果使用实例的动态绑定功能时p2更节省内存，否则p1较节省内存