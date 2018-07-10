#! /usr/bin/python
#coding=utf-8

import pwn
#
# 安装过程
#
def g_display_char(char):
    print("Hex: 0x" + str(pwn.u8(char)))
