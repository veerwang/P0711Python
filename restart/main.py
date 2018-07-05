#! /usr/bin/python
#coding=utf-8

#
# 本工程用于测试我重新开始学习的python语言
#

#from utils import g_print_version
import utils
import os

if __name__ == '__main__':
    utils.g_print_version()           #本行语句需要紧紧连着上一条语句
    utils.g_print_os_info()
    fd = open(os.getcwd()+"/data/rawfile",'rb')
    #print "file size = " + os.path.getsize(fd)
    size = os.path.getsize(os.getcwd()+"/data/rawfile")
    print ("size = " + str(size))     #注意int转换为string

    fd.close();
