#! /usr/bin/python
#coding=utf-8             			# 声明编码方式

import globle
import basefun
import platform

if __name__ == '__main__':
	print "program version: V" + globle.g_version
	bf = basefun.Basefun()
	bf.Set_ID(108)
	print "Basefun ID:%d" % (bf.Get_ID())   	# 格式化输出
	value = [20]
	bf.Chang_Value(value)				# 传递一个地址进去
	#print "Chang Value:%d" % (value)   		# 格式化输出
	print value[0]   				# 格式化输出
	print platform.uname()				# 输出系统信息
	print platform.linux_distribution()		# 输出系统信息
