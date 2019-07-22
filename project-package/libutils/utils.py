#coding=utf-8

import os
import struct

# 获取金融数据的接口包
import tushare as ts

# 获取外汇数据
import re
import json
import urllib.request

# 获取当前日期
from datetime import datetime

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

def g_print_tushare_version():
    print('tushare version: ' + ts.__version__)

#########
def g_get_stock_data(code):
    data = ts.get_hist_data(code)
    return data.head(1).close

#########
def g_get_exchance_data(current):
    url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREX" + current + "CNY&column=Code,Price"
    req = urllib.request.Request(url)
    f = urllib.request.urlopen(req)
    html = f.read().decode("utf-8")
    s = re.findall("{.*}",str(html))[0]
    sjson = json.loads(s)
    XXXCNY = sjson["Data"][0][0][1]/10000
    return XXXCNY

def g_formate_current_data(current):
    XXXCNY = g_get_exchance_data(current)
    return "P      " + g_get_date_today() + "    " + current + "     " + '￥' + str(XXXCNY) + '\n'

#########
def g_append_string_into_file(path,string):
    fileobject = open(path,'a+')
    fileobject.write(string)
    fileobject.close()

#########
def g_get_date_today():
    dt = datetime.now()
    return str(dt.year) + '/' + str(dt.month) + '/' + str(dt.day)

#########
class FileClass:
    def __init__(self,file_path_to_op):
        self.__mfilepath = file_path_to_op

    def open_with_write_file(self):
        self.__mfilehandle = open(self.__mfilepath,'a+')

    def write_string_into_file(self,value):
        self.__mfilehandle.write(value)

    def close_file(self):
        self.__mfilehandle.close()
