#coding=utf-8

import os
import struct

#
# 全局变量
#
g_version = "1.0.0"

#
# 全局函数
#
def g_print_version():
    print("Programe: version = " + g_version)

#########

def g_print_os_info():
    print("Python Work Directory: " + os.getcwd())

#########

def process_file():
    fd = open(os.getcwd()+"/data/rawfile",'rb')
    fd.seek(0);
    nfd = open(os.getcwd()+"/data/newrawfile",'wb')
    size = os.path.getsize(os.getcwd()+"/data/rawfile")
    print("size = " + str(size))     #注意int转换为string

    for i in range(0,size):
        buf = fd.read(1)
        if i == 5 :
            cbuf = int('00',16) 
            for j in range(0,100):
                xbuf = struct.pack("B",cbuf)
                nfd.write(xbuf)
        nfd.write(buf)

    fd.close();
    nfd.close();
 
#########

def g_do_print_times(times): 
    while(times):
        g_print_version()
        times -= 1

def g_tuple_return(x,y):
    return x+y,x*y

#
# 全局类
#
class Object:
    def __init__(self):
        print("Object init")
    def __del__(self):
        print("Object destroy")

    m_ID = "Object"
#
# 内部私有变量
#
    __m_name = "kevin"
