#! /usr/bin/env python3
# coding=utf-8

"""
 描述:	    全局变量管理类
 创建人:	kevin.wang
 创建日期:	2022年12月07日
 版本:		1.0.0
"""

from entity import EntityClass


class GlobalVars(EntityClass):

    def __init__(self):
        """docstring for __init__
        Description:
        Args:
        Returns:
        Raises:
        """
        self._account = 'None'

    def __del__(self):
        """docstring for __del__
        Description:
        Args:
        Returns:
        Raises:
        """
        pass

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
