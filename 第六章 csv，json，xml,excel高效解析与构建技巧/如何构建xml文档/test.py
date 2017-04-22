#coding:utf-8
import csv
from xml.etree.ElementTree import Element,ElementTree,tostring
from pretty import pretty

# e=Element("data")#设置标签
# print e.tag
# e.set("name","abc")#设置属性，得到属性get()
# print tostring(e)
# e.text="123"#设置标签文本
# print tostring(e)
# e2=Element("row")
# e3=Element("open")
# e3.text="8.80"
# e2.append(e3)#将 e3设置为e2的子元素
# # print tostring(e2)
# e.text=None
# e.append(e2)
# # print tostring(e)
# et=ElementTree(e)#创建节点树，将根结点作为参数
# et.write("demo.xml")#将节点树写入文件
def csvToXml(fname):
    with open(fname,"rb") as f:
        reder=csv.reader(f)
        header=reder.next()
        # print header
        root=Element("data")
        for row in reder:
            # print row
            # break
            erow=Element("row")
            root.append(erow)
            for tag,text in zip(header,row):
                e=Element(tag)
                e.text=text
                erow.append(e)
        pretty(root)
        et=ElementTree(root)
        et.write(fname+".xml")
        # print tostring(et)
csvToXml("table.csv")
