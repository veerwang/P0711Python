#!/usr/bin/env python3

import os
import sys
import types
import xml.etree.ElementTree as ET
from subprocess import call

def analyze(xmlfilepath):
	print("start analyze ...")
	xmlFilePath = os.path.abspath(xmlfilepath)
	print("xmlfile patch: " + xmlFilePath)

	try:
		tree = ET.parse(xmlFilePath)
		print ("tree type:", type(tree))
						# 获得根节点
		root = tree.getroot()
	except Exception as e:  		# 捕获除与程序退出sys.exit()相关之外的所有异常
		print ("parse test.xml fail!")
		sys.exit()

	print ("root type:", type(root))    
	print (root.tag, "----", root.attrib)
	print ("--")
	print ("this is the key ----> "+root.attrib.get("package","com.epay.test")+"!!!!!")
	print ("--")

	for child in root:
        	print ("遍历root的下一层", child.tag, "----", child.attrib)

############################################
#
#   输出参数:xmlfilepath
#            xml文件的路径
#
############################################
def get_package_name(xmlfilepath):
	xmlFilePath = os.path.abspath(xmlfilepath)
	try:
		tree = ET.parse(xmlFilePath)
		root = tree.getroot()
	except Exception as e:  		# 捕获除与程序退出sys.exit()相关之外的所有异常
		sys.exit()

	return root.attrib.get("package","com.epay.test")

############################################
#
#   输出参数:apkfilepath:apk文件的路径
#	     apktoolpath:apktool工具的路径
#	     output:输出apk解压出了的路径
#
############################################
def unpack_apk_file(apkfilepath,apktoolpath,output):
	call(['java','-jar',apktoolpath,'d',apkfilepath,'-o',output])


if __name__ == '__main__':
	print("starting xml file analyze")
	#print(get_package_name(sys.argv[1]))
	#unpack_apk_file("./cutfruit.apk","./apktool.jar","./123")
	#analyze(sys.argv[1])
