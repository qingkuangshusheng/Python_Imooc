#coding:utf-8
from collections import namedtuple
#使用元祖可以降低内存开销
# ("jim",16,"male","jim8721@gmail.com")
# ("LiLei",17,"male","leile@qq.com")
# ("lucy",16,"female","lucy123@yahoo.com")
#方法一直接定义索引值
# name=0
# age=1
# sex=2
# email=3
name,age,sex,email=xrange(4)
student=("jim",16,"male","jim8721@gmail.com")
print student[age]

#方法二使用namedtuple替代内置tuple，开销比普通元组大一点点
Student=namedtuple("Student",["name","age","sex","email"])
# s=Student("jim",16,"male","jim8721@gmail.com")#位置传参
s=Student(name='jim', age=16, sex='male', email='jim8721@gmail.com')#关键字传参
print s[email]
#namedtuple 是内置元组的一个子类
print isinstance(s,tuple)