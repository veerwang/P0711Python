#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2020年01月12日 
# 版本:		1.0.0     

import os

if __name__ == '__main__':
    print("hello the world")

    try:
        from configparser import ConfigParser
    except ImportError:
        from ConfigParser import ConfigParser  # ver. < 3.0

    # instantiate
    config = ConfigParser()

    # parse existing file
    config.read('test.ini')

    str_Version = config.get('Config','Version')
    str_Color   = config.get('Config','Color')

    print("Version:" + str_Version)
    print("Color:" + str_Color)

    # update existing value
    config.set('Config', 'Version', '2.0.0')

    # add a new section and some values
    config.add_section('Layout')
    config.set('Layout', 'Pattern', 'Middle')

    # save to a file
    with open('test.ini', 'w') as configfile:
        config.write(configfile)
