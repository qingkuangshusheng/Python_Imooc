#coding:utf-8
def pretty(e,level=0):
    if len(e)>0:
        e.text="\n"+"\t"*(level+1)
        for child in e:
            pretty(child,level+1)
            child.tail=child.tail[:-1]
    e.tail="\n"+'\t'*level
