#coding:utf-8
from random import randint
#方法一
d={x : randint(60,100) for x in "xyzabc"}
print d
print sorted(d)
#元组的比较，先比较第零个元素如果相等再比较第一个元素
print (97,'a')>(69,'b')
print sorted(zip(d.itervalues(),d.iterkeys()))
#方法二
print d.items() #[('a', 85), ('c', 74), ('b', 69), ('y', 76), ('x', 62), ('z', 89)]
print sorted(d.items(),key=lambda x:x[1])
#[('z', 61), ('c', 76), ('a', 86), ('b', 96), ('y', 96), ('x', 96)]

