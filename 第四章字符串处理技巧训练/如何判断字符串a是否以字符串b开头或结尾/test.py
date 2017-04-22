#coding:utf-8
import os,stat
#str.startswith(),str.endswith()
l=os.listdir(".")
# s="b.css"
# f=s.endswith((".html",".css"))#只能是元祖不能是列表
# n=[name for name in l if name.endswith((".css",".html"))]
# print n
#修改文件的权限
print oct(os.stat("a.html").st_mode)
os.chmod("a.html",os.stat("a.html").st_mode|stat.S_IXUSR)