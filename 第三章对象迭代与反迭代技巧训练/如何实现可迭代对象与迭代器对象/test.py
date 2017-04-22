#coding:utf-8
#可迭代对象如list,str,内部实现了__iter__或__getitem__方法,当调用iter方法时，
# 这些magic方法将会触发，并将可迭代对象转换为迭代器对象,迭代器提供了next接口
i=iter('abcdefg')
print i.next()
for x in i:#for循环实际是可迭代对象转换为迭代器对象之后连续不断地调用了迭代器的next方法
    print x
