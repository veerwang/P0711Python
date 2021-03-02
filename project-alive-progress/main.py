#! /usr/bin/env python3
#coding=utf-8

"""
 描述:		工程测试,安装alive_progress模块
 创建人:	kevin.wang
 创建日期:	2021年03月02日
 版本:		1.0.0
"""

import os
from alive_progress import alive_bar
import time

if __name__ == '__main__':
    print("start alive progress test")

    with alive_bar(10,bar ='blocks') as bar:
        for i in range(10): 
            time.sleep(0.1)
            bar()
