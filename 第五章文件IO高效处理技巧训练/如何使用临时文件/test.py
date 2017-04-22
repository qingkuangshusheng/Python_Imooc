#coding:utf-8
from tempfile import TemporaryFile,NamedTemporaryFile
# f=TemporaryFile()#默认模式为"wb+"，Temporaraafile创建的临时文件不能在系统路径中找到只能通过文件对象访问，适合本进程访问
# f.write("abcdef"*100000)
# f.seek(0)#使文件指针回到文件首部
# print f.read(1)
nf=NamedTemporaryFile()#NamedTemporaryFile创建的临时文件能够在文件系统路径中找到
print nf.name
#创建新对象时旧文件对象会自动关闭并被回收
# nf=NamedTemporaryFile(delete=False)不指定delete则文件关闭后临时文件会自动删除，适合多进程访问