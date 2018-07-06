#! /usr/bin/python
#coding=utf-8

#
# 本工程用于测试我重新开始学习的python语言
#  该程序的功能是进行二进制文件的调整
#

#from utils import g_print_version
import utils
import os
import struct

if __name__ == '__main__':
    utils.g_print_version()           #本行语句需要紧紧连着上一条语句
    utils.g_print_os_info()
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
