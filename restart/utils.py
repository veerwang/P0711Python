#coding=utf-8

import os
#
# 全局变量
#
g_version = "1.0.0"

#
# 全局函数
#
def g_print_version():
    print "Programe: version = " + g_version

def g_print_os_info():
    print "Python Work Directory: " + os.getcwd()

#
# 全局类
#
class Object:
    def __init__(self):
        print "Object init"
    def __del__(self):
        print "Object destroy"

    m_ID = "Object"
#
# 内部私有变量
#
    __m_name = "kevin"
