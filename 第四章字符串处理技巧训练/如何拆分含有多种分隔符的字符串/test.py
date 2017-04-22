#coding:utf-8
from pprint import pprint
import re
#str.split()一次只能处理一个分隔符，re.split一次可以处理多个分隔符
s="bfvjd;k/jfn,bhsv/jf;dj dj,fdf"
#默认空格作为分隔符
# pprint(s.split())
# print s.split(";")
# res=s.split(";")
# print map(lambda x:x.split("/"),res)
# t=[]
# map(lambda x:t.extend(x.split("/")),res)
#方法一
def mysplit(s,ds):
    res=[s]
    for d in ds:
        t=[]
        map(lambda x:t.extend(x.split(d)),res)
        res=t
    return [x for x in res if x]#过滤掉字符串中有连续的分隔符时生成的空字符串
#print mysplit(s,reg)

#方法二
reg=r"[,/; ]+"
reg=re.compile(reg)
l=re.split(reg,s)
print l
