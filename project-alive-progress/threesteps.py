#! /usr/bin/env python3
#coding=utf-8

"""
 描述:		工程测试		 
 创建人:	kevin.wang
 创建日期:	2021年03月02日 
 版本:		1.0.0     
"""

import os
from alive_progress import alive_bar
import time

if __name__ == '__main__':
    print("步骤测试")

    " length 标示进度条的长度，默认使40 
    with alive_bar(4,title='==>',length=10) as bar:
        print("步骤1，进行检测....")
        time.sleep(1)
        bar()
        print("步骤2，进行分析....")
        time.sleep(3)
        bar()
        print("步骤3，进行报告....")
        time.sleep(4)
        bar()
        print("步骤4，进行清除....")
        time.sleep(3)
        bar()
