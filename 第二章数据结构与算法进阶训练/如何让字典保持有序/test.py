#coding:utf-8
from collections import OrderedDict
from time import time
from random import randint
# d={}
# d['jim']=(1,35)
# d['leo']=(2,37)
# d['Bob']=(3,40)
# for k in d:
#     print k
#使用OrderdDict 替代内置Dict
# d=OrderedDict()
# d['jim']=(1,35)
# d['leo']=(2,37)
# d['Bob']=(3,40)
# for k in d:
#     print k
d=OrderedDict()
player=list("ABCDEFGH")
start=time()
for i in xrange(8):
    raw_input()
    p=player.pop(randint(0,7-i))
    end=time()
    print i+1 ,p ,end-start
    d[p]=(i+1,end-start)
print
print "-"*20
for k in d:
    print k ,d[k]