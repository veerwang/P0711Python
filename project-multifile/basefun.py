#! /usr/bin/python
#coding=utf-8             			# 声明编码方式
"""
这个模块存放的是全局使用到的类
"""

class Basefun:
#private valriable
	__m_ID = 0

	def __init__(self):
		print "Basefun class create"
	def __del__(self):
		print "Basefun class destroy"
# public function
	def Set_ID(self,id):
		self.__m_ID = id
	def Get_ID(self):
		return self.__m_ID
	def Chang_Value(self,value):
		value[0] = value[0] + 50;

class Subclass(Basefun):
	def __init__(self):
		print "subclass create"
	def __del__(self):
		print "subclass destroy"
