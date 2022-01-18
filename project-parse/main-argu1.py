#! /usr/bin/env python3
# coding=utf-8

"""
 描述:	    用于测试cli用户界面命令解析
 创建人:	kevin.wang
 创建日期:	2022年01月18日
 版本:		1.0.0
"""


import argparse


class FooAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))
        setattr(namespace, self.dest, values)


if __name__ == '__main__':
    # 用于测试
    parser = argparse.ArgumentParser(description='用于rita测试使用')
    parser.add_argument('-f', '--foo', help='foo help', action=FooAction)
    args = parser.parse_args()
