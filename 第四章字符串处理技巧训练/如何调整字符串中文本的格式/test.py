#coding:utf-8
import re
log=open("WiFi_Log2.txt").read()
# sublog=re.sub("(\d{4})-(\d{2})-(\d{2})",r"\2/\3/\1",log)
#为捕获组起名
sublog=re.sub("(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})",r"\g<month>/\g<day>/\g<year>",log)
print sublog