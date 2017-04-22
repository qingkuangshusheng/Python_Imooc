#coding:utf-8
#1,"+"(浪费内存且速度慢)2,str.join()(高效且速度快)
s1="sgdhsdvbsk"
s2="2742282224"
#
# s=";".join(["123","abc","392"])
# s="".join(["123","abc","392"])
# print s
# l=["abc",123,45,"xyz"]#列表太长不适用
# s3=''.join([str(x) for x in l])
# print s3
l=["abc",123,45,"xyz"]#列表太长不适用
s3=''.join(str(x) for x in l)#使用生成器表达式
print s3