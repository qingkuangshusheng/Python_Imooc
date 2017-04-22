#coding:utf-8
import json
#json模块使用1，将python对象转为json字符串
l=[1, 2, "abc", {"name": "bmob", "age": 13}]
j=json.dumps(l)
print j,type(j)
d={"b":None,"a":5,"c":"abc"}
j2=json.dumps(d)
print j2
j3=json.dumps(l,separators=[",",":"])#设置json数据分隔符
print j3
j4=json.dumps(d,sort_keys=True)#对json中的key进行排序
print j4
#将json字符串对象转为python对象
l2=json.loads('[1, 2, "abc", {"name": "bmob", "age": 13}]')
print l2
d2=json.loads('{"b":null,"a":5,"c":"abc"}')
print d2
#将python对象写转为json字符串并到文件中
with open("demo.json","wb") as f:
    json.dump(d,f)
#将json文件中的json字符串转为python对象
with open("demo.json","rb") as rf:
    d3=json.load(rf)
    print "d3:",d3


