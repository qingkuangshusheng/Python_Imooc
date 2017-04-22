#coding:utf-8
from functools import update_wrapper,wraps,WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES
def f(a):
    '''f function'''#文档字符串
    return a* 2
print f.func_doc,f.func_dict,f.func_name,f.__module__

def f(a,b=1,c=[]):
    print a,b,c
print f.__defaults__#(1, [])保存函数的默认参数
f.__defaults__[1].append("abc")
f(100)

#闭包
def f2():
    a=2
    return lambda k:a ** k
g=f2()
c=g.__closure__[0]#访问闭包中的第一个变量
print c.cell_contents

def mydecorator(func):
    #第三种方法
    @wraps(func)#使用默认参数
    def wrapper(*args,**kwargs):
        '''wrapper function'''
        print "in wrapper"
        func(*args,**kwargs)
        #方法一
        wrapper.__name__==func.__name__
        #方法二
    # update_wrapper(wrapper,func,("__name__","__doc__"),(__dict__,))
    #使用默认参数
    update_wrapper(wrapper,func,WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES)
    return wrapper

@mydecorator#被装饰之后函数的__name__,__doc__属性就替换为wrapper函数的
def example():
    '''example function'''
    print "In example"

print example.__name__
print example.__doc__
print WRAPPER_ASSIGNMENTS
print WRAPPER_UPDATES