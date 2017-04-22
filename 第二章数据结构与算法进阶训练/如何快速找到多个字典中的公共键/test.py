#coding:utf-8
from random import randint,sample
# print sample('abcdefg',3)
# print sample("abcdefg",randint(3,6))
s1 ={x : randint(1,4) for x in sample('abcdefg',randint(3,6))}
s2 ={x : randint(1,4) for x in sample('abcdefg',randint(3,6))}
s3 ={x : randint(1,4) for x in sample('abcdefg',randint(3,6))}
print s1
print s2
print s3
#方法一，效率不高
res=[]
for k in s1:
    if k in s2 and k in s3:
        res.append(k)
print res
#方法二,使用集合操作
print s1.viewkeys()&s2.viewkeys()&s3.viewkeys()
#n个字典时使用map,reduce函数进行计算
print reduce(lambda a,b:a&b,map(dict.viewkeys,[s1,s2,s3]))