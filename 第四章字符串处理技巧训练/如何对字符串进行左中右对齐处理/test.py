#coding:utf-8
#str.ljust(),str.rjust(),str.center(),使字符串左右居中对齐
s="abc"
#s=s.ljust(20,"-")
# s=format(s,">20")
# s=format(s,"<20")
# s=format(s,"^20")
# print s
d={"sfdjkv":12,
   "hfjkd":86,
   "sgvjvgf":87,
   "jf":56456,
   "wweygfwehf":7846}
# print d
# print d.keys()
# print map(len,d.keys())
# print max(map(len,d.keys()))
# w=max(map(len,d.keys()))
# for k in d:
#     print k.rjust(w),":",d[k]

def formatDirct(d,s):
    w=str(max(map(len,d.keys())))
    for k in d:
        print format(k,s+w),":",d[k]

formatDirct(d,">")