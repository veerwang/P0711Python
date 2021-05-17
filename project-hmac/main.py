#! /usr/bin/env python3
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2020年01月12日 
# 版本:		1.0.0     


import hmac
import hashlib
import os
from datetime import datetime


if __name__ == '__main__':
    print("HMAC 用于校验信息是否被篡改")
    """ 
    key 可以任意 
    """ 
    key = bytes('99818976001025647765','utf-8')
    my = datetime.utcnow().strftime('%Y-%m-%d').encode('utf-8')
    h = hmac.new( key, my, hashlib.sha256 )
    print( h.hexdigest() )
