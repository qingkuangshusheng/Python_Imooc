#coding:utf-8
class PrimeNumbers(object):
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def isPrimeNumber(self,k):
        if k<2:
            return False
        for i in xrange(2,k):
            if k%i==0:
                return False
        return True
    def __iter__(self):
        for k in xrange(self.start,self.end+1):
            if self.isPrimeNumber(k):
                yield k
if __name__ == '__main__':
    for x in PrimeNumbers(1,100):
        print x

