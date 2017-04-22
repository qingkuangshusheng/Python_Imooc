#coding:utf-8
import struct#将二进制转换为十进制
import array#导入数组
# print struct.unpack("h","\x01\x02")
f=open("chat.mp3","rb")#应使用wav格式音频文件，找不到暂时用mp3格式替代
info=f.read(44)
# print struct.unpack("h",info[22:24])
#将音频文件44字节之后的数据部分读入数组中
f.seek(0,2)#将文件指针移到末尾
# print f.tell()
n=(f.tell()-44)/2#数组大小数组中每个元素占两个字节
# print n
buf=array.array("h",(0 for _ in xrange(n)))#"h"代表short型"i"代表int型
f.seek(44)#将指针定位到data部分
f.readinto(buf)#将数据部分读到数组
# print buf[0]
for i in xrange(n):buf[i]/=8#降低采样频率将声音变小
#二进制文件写操作
f2=open("chat2.mp3","wb")
f2.write(info)#将音频文件头44个字节写入文件
buf.tofile(f2)#将数组中的数据写到二进制文件中
f2.close()

