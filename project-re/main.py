#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
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

def sub_string():
    str = 'hello the world: 0592-2654281'
    newstr = re.sub('(.*): ','',str)
    # 仅仅打印出 0592-2654281
    print(newstr)

if __name__ == '__main__':
    print("正则表达式")
    match_string()
    search_string()
    sub_string()
