#coding:utf-8
from random import randint
from collections import deque#使用队列
import pickle
N=randint(0,100)
try:
    history=pickle.load(open("history"))
except Exception,e:
    history=deque([],5)
def guess(k):
    if k==N:
        print "right"
        return True
    if k<N:
        print "%s is less-than N"%k
    else:
        print "%s is greater-than N"%k
    return False

while True:
    line=raw_input("please input a number: ")
    if line.isdigit():
        k=int(line)
        history.append(k)
        if guess(k):
            pickle.dump(history,open("history","w"))
            break
    elif line=="history" or line=="h?":
        print list(history)#以列表的形式打印队列


