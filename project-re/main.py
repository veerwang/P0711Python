#! /usr/bin/python
#coding=utf-8

#
# 描述:	        正则表达式	
#
# 学习网站
# https://docs.python.org/zh-cn/3/howto/regex.html#regex-howto
#
# 创建人: 	kevin.wang
# 创建日期:     2019年09月19日 
# 版本:		1.0.0     

import os
import re

def match_string():
    str = 'hello the world'
    p = re.match('hello',str)
    print(p.span())

def search_string():
    str = 'hello the world'
    p = re.search('wor*',str)
    print(p.group())

def search_string_1():
    str = 'hello the world'
    p = re.search('[a-z]e',str)
    print(p.group())

def search_string_2():
    str = 'hello the [world]'
    p = re.search('\[world',str)
    print(p.group())

def search_string_3():
    str = 'hello thethe [world]'
    # + 匹配 0次或1次
    # ? 可选择的
    p = re.search('the+',str)
    print(p.group())

def search_string_4():
    str = 'hello thethe [world]'
    # * 匹配 1次或很多次
    p = re.search('the*',str)
    print(p.group())

def search_string_5():
    str = 'hello thethe [world]'
    # * 匹配 1次或很多次
    p = re.search('the*',str)
    print(p.group())

def sub_string():
    str = 'hello the world: 0592-2654281'
    newstr = re.sub('(.*): ','',str)
    # 仅仅打印出 0592-2654281
    print(newstr)

if __name__ == '__main__':
    print("正则表达式")
    match_string()
    search_string()
    search_string_1()
    search_string_2()
    search_string_3()
    search_string_4()
    sub_string()
