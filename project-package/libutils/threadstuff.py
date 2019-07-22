#! /usr/bin/python
#coding=utf-8

#
# 描述:	        线程基类	
# 创建人: 	kevin.wang
# 创建日期:     2019年07月20日 
# 版本:		1.0.0     

import threading 
import time

class daemonthread(threading.Thread):
    def __init__(self,id,name):
        threading.Thread.__init__(self)
        self.name   = name
        self.id     = id

    def run(self):
        self.thread_core()

    def thread_core(self):
        count = 5
        while count > 0:
            print("This is base thread %s" % self.name)
            time.sleep(1)
            count -= 1

if __name__ == '__main__':
    print("hello the world")
