#coding:utf-8
from random import randint
from pprint import pprint
from itertools import chain

chinese=[randint(60,100) for _ in range(40)]
#pprint(chinese)
math=[randint(60,100) for _ in range(40)]
english=[randint(60,100) for _ in range(40)]
#计算每位同学三门成绩的总成绩,并行迭代
#方法一：
# for i in xrange(len(chinese)):
#     chinese[i]+math[i]+english[1]
#方法二，通用方法
# total=[]
# for x,y,z in zip(chinese,math,english):
#     total.append(x+y+z)
# pprint(total)
#串行迭代,itertools.chain()
#过滤语数英三门成绩大于八十的成绩
grade=[x for x in chain(chinese,math,english) if x>=80]
pprint(grade)





