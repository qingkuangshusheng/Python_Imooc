#coding:utf-8
from itertools import islice

f=open("testText")
# l=f.readlines()
# print l
# i=islice(f,0,5)
# i=islice(f,8)
i=islice(f,4,None)

# for x in i:
#     print x
# for x in range(6):
#     print i.next()
l=[x for x in range(20)]
t=iter(l)
#会接着原来的位置进行迭代
for x in islice(t,5,10):
    print x

for x in t:
    print x
