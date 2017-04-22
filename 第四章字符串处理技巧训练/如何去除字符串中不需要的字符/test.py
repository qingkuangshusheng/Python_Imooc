#coding:utf-8
import re
#str.strip()去掉字符串前后的空白,str.lstrip(),str.rstrip()
# s=" abc123 "
# s=s.strip()
# s="---abc+++"
# s=s.strip("+-")
# print s
#字符串切片
# s="abc:123"
# s=s[:3]+s[4:]
# print s
#str.replace(),re.sub()
# s="\tabc\t123\txyz"
# s=s.replace("\t","")
# print s
# s="\tabc\t123\txyz\r"
# s=re.sub("[\t\r]","",s)
# print s
#str.translate()
import string
# s=string.maketrans("abcxyz","xyzabc")#字符映射
# print s
# s="abc1230323xyz"
# s=s.translate(string.maketrans("abcxyz","xyzabc"))
# print s
s="abc\rrefg\n2345\t"
s=s.translate(None,"\r\n\t")
print s



