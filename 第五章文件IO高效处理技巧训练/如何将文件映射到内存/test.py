#coding:utf-8
import mmap#文件映射模块
f=open("blued.mp3","rb+")
# print f.fileno()
# m=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_WRITE)#可以对文件进行数组类型的操作如数组索引操作，0表示映射整个文件
# print type(m)
#对文件进行读操作
# print m[1]
# print m[0:10]
#对文件进行写操作
# m[0]="\x88"#文件已被修改
# print m[0]
# print m[0:10]
# m[4:8]="\xff"*4#用切片进行修改时，切片长度与修改内容应相等
#将文件从第四页开始映射，一共映射8页
m=mmap.mmap(f.fileno(),mmap.PAGESIZE*8,access=mmap.ACCESS_WRITE,offset=mmap.PAGESIZE*4)
