#coding:utf-8
from urllib import urlretrieve
import csv

#urlretrieve("url","filename")#下载table.csv
#读取csv文件内容
# rf=open("table.csv","rb")
# reader=csv.reader(rf)#reder为迭代器对象，用next或for循环进行迭代
# print reader.next()
# for row in reader:
#     print row
#将内容写入csv文件
# wf=open("table_copy.csv","wb")
# writer=csv.writer(wf)
# writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'])
# writer.flush()
#将平安银行这只股票，在2016年-2017年中成交量超过50000000的记录存储到另一个csv文件中
with open("table.csv","rb") as rf:
    reader=csv.reader(rf)
    with open("table2.csv","wb") as wf:
        writer=csv.writer(wf)
        headers=reader.next()
        writer.writerow(headers)
        for row in reader:
            if row[0]<"2016-01-01":#日期可以直接比较
                break
            if int(row[5])>50000000:
                writer.writerow(row)
    print "end"





