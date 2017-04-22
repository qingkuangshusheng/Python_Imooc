#coding:utf-8
# print ord("a"),ord("b")
# s=u"你好"#unicode字符串不能直接存到磁盘中，经过encode("编码格式")才能存到磁盘中
# print s
# print s.encode("utf-8")
# print s.encode("gbk")
s=u"你好"
f=open("py2.txt","w")
f.write(s.encode("gbk"))
f.close()
f=open("py2.txt","r")
t=f.read()
print t.decode("gbk")




