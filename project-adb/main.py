#! /usr/bin/python3
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年10月14日 
# 版本:		1.0.0     

import os.path as op

from adb import adb_commands
from adb import sign_cryptography

# KitKat+ devices require authentication
# 前提是要安装adb，并且pip 要安装libusb1
# 注意adb的服务要killer掉
signer = sign_cryptography.CryptographySigner(op.expanduser('~/.android/adbkey'))

# Connect to the device
device = adb_commands.AdbCommands()
#device.ConnectDevice(rsa_keys=[signer])
#device.ConnectDevice('','172.27.20.117:5556','3000',rsa_keys=[signer])
device.ConnectDevice('','172.27.20.117:5556','9000',rsa_keys='')

# Now we can use Shell, Pull, Push, etc!
print(device.Shell('ls -al /sdcard/'))
print(device.Shell('dmesg'))
