#coding:utf-8
# l=[1,2,3,4,5]
#改变了原列表
# l.reverse()
# print l[::-1]#步进值为-1
# print l
# iter(l)#得到一个正向迭代器
# reversed(l)#得到一个反向迭代器,实际调用l.__reversed__方法
# for x in reversed(l):
#     print x
class FloatRange:
    def __init__(self,start,end,step=0.1):
        self.start=start
        self.end=end
        self.step=step

    def __iter__(self):
        t=self.start
        while t<=self.end:
            yield t
            t+=self.step

    def __reversed__(self):
        t=self.end
        while t>=self.start:
            yield t
            t-=self.step

for x in reversed(FloatRange(1.0,4.0,0.5)):
    print x

