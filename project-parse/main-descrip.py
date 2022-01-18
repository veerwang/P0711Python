#! /usr/bin/env python3
# coding=utf-8

"""
 描述:	    用于测试cli用户界面命令解析	
 创建人:	kevin.wang
 创建日期:	2022年01月18日
 版本:		1.0.0
"""


import sys
import argparse


if __name__ == '__main__':
    # 用于测试
    parser = argparse.ArgumentParser(description='用于rita测试使用')
    parser.add_argument('--foo', help='foo help')
    args = parser.parse_args()
