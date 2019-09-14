#! /usr/bin/python
#coding=utf-8

#
# 描述:	        ｃｏｌｏｒａｍａ测试	
# 创建人: 	kevin.wang
# 创建日期:     2019年09月14日 
# 版本:		1.0.0     

import os
from colorama import init
from colorama import Fore, Back, Style

if __name__ == '__main__':
    init(autoreset = True)
    print(Fore.RED + '这个是color的测试')
