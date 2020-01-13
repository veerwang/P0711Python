#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年09月20日 
# 版本:		1.0.0     

import os
import json
import pathlib

def save_json(path):
    data = { "target sdk":"16","api version":"15","version":"['5','6','7']"  }
    p = pathlib.Path(path)
    if p.exists():
        os.remove(path)

    with open(path,'w') as fp:
        json.dump(data,fp) 

def load_json(path):
    p = pathlib.Path(path)
    if p.exists():
        with open(path,'r') as fp:
            data = json.load(fp) 
            print(data['target sdk'])
            print(data['version'])
            alist = eval(data['version'])
            for v in alist:
                print(v)

if __name__ == '__main__':
    print("json programe")
    save_json('test.json')
    load_json('test.json')

