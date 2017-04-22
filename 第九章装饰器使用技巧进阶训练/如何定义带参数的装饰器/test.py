#coding:utf-8
#以下内容为python3环境
from inspect import signature
def typeassert(*args,**kwargs):#为了向装饰器内部传递参数
    def decorator(func):
        pass
        sig=signature(func)
        btypes=sig.bind_partial(*args,**kwargs).arguments
        def wrapper(*args,**kwargs):
            for name, obj in sig.bind(*args,**kwargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj,btypes[name]):
                        raise TypeError("%s must be %s"%(name,btypes[name]))

            return func(*args,**kwargs)
        return wrapper
    return decorator

@typeassert(int )
def f(a,b,c):
    print(a,b,c)

f(1,"abc",[1,2,3])
f(1,2,[1,2,3])
