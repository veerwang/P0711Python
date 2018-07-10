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

    bin_name = './bin/cat'
    elf = pwn.ELF(bin_name);  #导入cat二进制文件
    print("BIN NAME: "+bin_name+"; ADDRESS: 0x"+str(elf.address))

if __name__ == '__main__':
    main()
