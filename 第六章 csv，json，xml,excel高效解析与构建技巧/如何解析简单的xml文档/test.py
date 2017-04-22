#coding:utf-8
from xml.etree.ElementTree import parse

f=open("city.xml")
et=parse(f)
root=et.getroot()
# print root.tag
# print root.attrib#根节点属性
# print root.text.strip()#根节点文本
#root为可迭代对象
# for child in root:
#     print child.get("name")#get方法取元素的属性
#通过标签找到子元素
# root.find("province")#总是找到碰到的第一个标签
# root.findall("province")#找到所有的名字为province的子标签，并返回一个包含了所有子标签对象的列表
# root.iterfind("province")#作用同findall,不过返回的是一个迭代器对象
# for e in root.iterfind("province"):
#     print e.get("name")
#find,findall.iterfind,都只能找到当前元素的直接子元素
# print root.findall("city")#返回空列表
# i=root.iter()#默认找到当前结点的所有子元素并返回一个迭代器对象
# print i
# print list(i)#将迭代器对象转换为列表
# i2=root.iter("city")#找到当前节点下名字为"city"的子节点
# print list(i2)
# print root.findalll("province/*")#找到当前节点下province节点下的所有子节点
# print root.findall(".//city")#找到任意节点下的所有子元素
# print root.findall(".//city/..")#找到某个节点的父节点
#通过节点属性查找结点
# print root.findall("province[@name]")
#通过节点属性及属性值查找结点
# print root.findall("province[@postcode='110000']")
# print root.findall("province[city]")#查找包含指定子节点的父节点
# print root.findall("province[city='1']")#查找子节点包含特定值的父节点
print root.findall("province[1]")#根据查找到所有子节点的相对位置返回对应的子节点
print root.findall("province[last()]")#同上倒着来找
print root.findall("province[last()-1]")

