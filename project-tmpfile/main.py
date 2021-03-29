#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2021年03月29日
 版本:		1.0.0
"""


import tempfile


if __name__ == '__main__':
    with tempfile.NamedTemporaryFile(dir='.', delete=False) as fp:
        fp.write(b'Hello world!')
        fp.seek(0)
        fp.read()
        fp.close()
