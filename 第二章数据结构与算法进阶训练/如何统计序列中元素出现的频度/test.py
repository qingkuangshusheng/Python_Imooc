#coding:utf-8
from pprint import pprint
from random import randint
from collections import Counter
import re
#方法一
data=[randint(0,20) for _ in xrange(30)]
# print data
c=dict.fromkeys(data,0)#根据键来生成字典
# pprint(c)
for x in data:
    c[x]+=1
# print(c)

c2=Counter(data)
# print type(c2)
# pprint(c2)
# print c2.most_common(3)
text=open("IFRToolLog.txt").read()
l=re.split("\W+",text)
c3=Counter(l)
pprint(c3.most_common(5))

