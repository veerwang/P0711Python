#! /usr/bin/python
#coding=utf-8

#
# 本工程用于测试tushare金融数据接口
# 官网　www.tushare.org
# 
# 学习python的网站
# https://docs.python.org/zh-cn/3.7/howto/
# http://www.runoob.com/python/python-date-time.html
# http://www.runoob.com/python3/python3-tutorial.html

#from utils import g_print_version
import os
import logging

import libutils.utils
import libutils.threadstuff

if __name__ == '__main__':
    libutils.utils.g_print_version()

    # 获取股票交易函数
    #data = utils.g_get_stock_data('600027')
    #print(data)

    firstthread = libutils.threadstuff.daemonthread(1,"printthread")
    firstthread.start()

    # 获取外币汇率的函数
    openfile = libutils.utils.FileClass("./price.db")
    openfile.open_with_write_file()
    openfile.write_string_into_file(libutils.utils.g_formate_current_data("HKD"))
    openfile.write_string_into_file(libutils.utils.g_formate_current_data("SGD"))
    openfile.write_string_into_file(libutils.utils.g_formate_current_data("USD"))
    openfile.write_string_into_file(libutils.utils.g_formate_current_data("JPY"))
    openfile.write_string_into_file('\n')
    openfile.close_file()

    # 设置日志的输出
    logging.basicConfig(filename='example.log',level=logging.INFO)
    # 等待线程结束
    firstthread.join()
    logging.info("主线程运行结束")
