#coding:utf-8
import os
import stat
import time
#1，系统调用，os.stat(),os.lstat(),os.fstat
# print os.stat("a")#获取文件状态
# print os.lstat("a")#不跟随符号连接
# f=open("a.txt","w")
# print os.fstat(f.fileno())#参数为文件描述符
s=os.stat("a.txt")
print s.st_mode#获取文件的类型
print stat.S_ISDIR(s.st_mode)#判断路径是否为文件夹
print stat.S_ISREG(s.st_mode)#判断是否为普通文件
print s.st_mode & stat.S_IRUSR#判断文件是否可读，stat.S_IRUSR是掩码，与运算的值大于0即时可读
print s.st_mode & stat.S_IXUSR#判断文件是否可执行
t=time.localtime(s.st_atime)#获取文件的最后修改时间
print t
print s.st_size#获取文件大小
#2快捷函数os.path
print os.path.isdir("a.txt")#判断文件是否为目录
print os.path.islink("a.txt")#判断是否为符号链接
print os.path.isfile("a.txt")#判断是否为文件
#os.path无法查看文件的访问权限
print time.localtime(os.path.getatime("a.txt"))#文件的最后修改时间
print os.path.getsize("a.txt")#获取普通文件的大小