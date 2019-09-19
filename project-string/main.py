#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年09月19日 
# 版本:		1.0.0     

import os

def find_string():
    mystr = 'hello the world hello'
    # first index of l
    print(mystr.find('l'))
    print('end: ' + str(mystr.rfind('l')))

def len_string():
    str = 'hello the world hello'
    print(len(str))

def count_string():
    str = 'hello the hello world hello'
    print(str.count('hello'))

def replace_string():
    str = 'hello the hello world hello'
    newstr = str.replace('hello','baby',2)
    print(newstr)

def split_string():
    str = 'a b c d e f g'
    worldlist = str.split(' ',2)
    print(worldlist)

def start_end_string():
    str = 'hello the hello world hello'
    print(str.startswith('hello'))
    print(str.endswith('hello'))

def just_string():
    str = 'hello'
    nstr = str.ljust(10) 
    mstr = str.rjust(10) 
    cstr = str.center(10) 
    print(nstr)
    print(mstr)
    print(cstr)

def strip_string():
    str = '   hello   '
    nstr = str.lstrip()
    print(nstr)
    mstr = str.rstrip()
    print(mstr)

# 以关键字作为分割符号，将字符串分为三个部分
def partition_string():
    str = 'hello the hello world hello'
    newstr = str.partition('the')
    print(newstr)

def splitlines_string():
    str = 'hello the world \n hello the world'
    newstr = str.splitlines()
    print(newstr)

def join_string():
    str = 'hello the world'
    flag = 'm'
    # 把每个字符后面添加分隔字符
    newstr = flag.join(str)
    print(newstr)

if __name__ == '__main__':
    print("string programe")
    find_string()
    len_string()
    count_string()
    replace_string()
    split_string()
    start_end_string()
    just_string()
    strip_string()
    partition_string()
    splitlines_string()
    join_string()
