#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2022年01月18日
 版本:		1.0.0
"""


import sys
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description="stcgal {} - an STC MCU ISP flash tool\n".format('1.0.0') +
                                                 "(C) 2014-2018 Grigori Goronzy and others\nhttps://github.com/grigorig/stcgal")
    exclusives = parser.add_mutually_exclusive_group()
    exclusives.add_argument("code_image", help="code segment file to flash (BIN/HEX)", type=argparse.FileType("rb"), nargs='?')
    opts = parser.parse_args()
