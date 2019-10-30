#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年10月30日 
# 版本:		1.0.0     

import os,time
from commanddef import command 

def static_process_mainline(q):
    while True:
        cmd = q.get(True)
        if cmd.mcmd == 'send':
            print("static process send")
            break;
        else:
            print("static process get cmd")
        time.sleep(1)

    cmd = command()
    cmd.mcmd = 'test'
    q.put(cmd)
    time.sleep(2)
    cmd.mcmd = 'quit'
    q.put(cmd)

if __name__ == '__main__':
    print("hello the world")
