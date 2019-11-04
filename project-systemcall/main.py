#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年11月04日 
# 版本:		1.0.0     

import threading
import ctypes

if __name__ == '__main__':
    SYS_gettid = 186
    libc = ctypes.cdll.LoadLibrary('libc.so.6')
    tid = libc.syscall(SYS_gettid)
    print(tid)
    print(threading.currentThread().ident)
