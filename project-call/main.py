#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2021年06月02日
 版本:		1.0.0
"""


class DispLedger():
    """description"""

    def __init__(self):
        """docstring for __init__
        Description:
        Args:
        Returns:
        Raises:
        """
        pass

    def __del__(self):
        """docstring for __del__
        Description:
        Args:
        Returns:
        Raises:
        """
        pass

    def __call__(self, Name):
        """docstring for
        Description: __call__ 用法，可以将类当成函数使用
        Args:
        Returns:
        Raises:
        """
        print("DispLedger: " + Name)


if __name__ == '__main__':
    l = DispLedger()
    l('kevin')
