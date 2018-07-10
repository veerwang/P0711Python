#! /usr/bin/python
#coding=utf-8

#
# 安装过程
#
# pip install --upgrade pwntools
#
#

import pwn
import utils

#
# 本工程用于实验pwmtools工程
#

def main():
    print("Pwm tools starting ...")
    utils.g_display_char('H')

    elf = pwn.ELF('./bin/cat');  #导入cat二进制文件

if __name__ == '__main__':
    main()
