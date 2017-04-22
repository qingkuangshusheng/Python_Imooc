#coding:utf-8
from telnetlib import Telnet
from sys import stdin,stdout
from collections import deque

class TelnetClient(object):
    def __init__(self,addr,port=80):
        self.addr=addr
        self.port=port
        self.tn=None

    def start(self):
        #self.tn=Telnet(self.addr,self.port)
        #self.history=deque()
        #user
        raise Exception("test")
        t=self.tn.read_until("login: ")
        stdout.write(t)
        user=stdin.readline()
        self.tn.write(user)
        #password
        t=self.tn.read_until("Password: ")
        if t.startswith(user[:-1]) :t=t[len(user)+1:]
        stdout.write(t)
        self.tn.write(stdin.readline())
        t=self.tn.read_until("$ ")
        stdout.write(t)
        while True:
            uinput=stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.write(uinput)
            t=self.tn.read_until("$ ")
            stdout.write(t[len(uinput)+1:])

    def cleanup(self):
        self.tn.close()
        self.tn=None
        with open(self.addr+"_history.txt","w") as f:
            f.writelines(self.history)
    #实现with语句的上下文协议
    #__enter__()会在__init__()方法调用后被调用
    def __enter__(self):
        self.tn=Telnet(self.addr,self.port)
        self.history=deque()
        return self#返回值即为client对象
    #__exit__()方法会在退出with语句或者抛出异常时调用
    def __exit__(self, exc_type, exc_val, exc_tb):
        print "int __exit__"
        self.cleanup()
        #方法默认返回值为return None
        return True#return True表示不抛出异常
with TelnetClient("127.0.0.1") as client:
    client.start()
print "END"

# client=TelnetClient("127.0.0.1")
'''print "\nstart"
client.start()
print "\ncleanup"
client.cleanup()'''