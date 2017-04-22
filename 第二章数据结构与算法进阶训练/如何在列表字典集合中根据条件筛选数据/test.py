#coding:utf-8
from random import randint
import timeit
import pprint

#方法一:循环迭代
data=[randint(-10,10) for _ in xrange(10)]
res=[]
for x in data:
    if x>=0:
        res.append(x)
print res

#方法二:filter()过滤函数
print filter(lambda x:x>=0,data)


#方法三:列表解析
print [x for x in data if x>=0]

#计算三种方法所用的时间
# t=timeit.Timer("filter(lambda x:x>=0,data)","from __main__ import data")
# print t.timeit()
# p='''for x in data:
#     if x>=0:
#         res.append(x)'''
# print timeit.timeit(p,"from __main__ import data,res,p")
# print timeit.timeit("filter(lambda x:x>=0,data)","from __main__ import data")
# print timeit.timeit("[x for x in data if x>=0]","from __main__ import data")
#字典生成式
d={x:randint(60,100) for x in xrange(1,21)}
pprint.pprint(d)
#字典解析
d2={k:v for k,v in d.iteritems() if v>90}
pprint.pprint(d2)

#集合解析
s=set(data)
# pprint.pprint(s)
print {x for x in s if x%3==0}