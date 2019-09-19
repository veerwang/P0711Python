#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年09月18日 
# 版本:		1.0.0     

import os
import sys
import pathlib

def usage():
    print("Uage: main.py write/read")

def display_dir_info(path):
    p = pathlib.Path(path)
    print('name:' + p.name)
    print('stem:' + p.stem)
    print('suffix:' + p.suffix)

def first_version():
    if  sys.argv[1] == 'write':
        p = pathlib.Path('run.log')
        with p.open('a') as f:
            f.write('hello the world\n')
    elif sys.argv[1] == 'read':
        p = pathlib.Path('run.log')
        with p.open('r') as f:
            print(f.read())

def second_version():
    if  sys.argv[1] == 'write':
        p = pathlib.Path('run.log')
        if not p.exists():
            print("file no exists")
            # 使用with语句无需进行关闭 close
            with p.open('ab') as f:
                f.write(b'12345678901234567891234567890dd\n')

    elif sys.argv[1] == 'read':
        p = pathlib.Path('run.log')
        if p.exists():
            print("file exists")
            with p.open('rb') as f:
                c = f.read(1)
                print(c)
                while c:
                    c = f.read(1)
                    print(c)

if __name__ == '__main__':
    print("文件操作工程")

    display_dir_info(__file__)

    if len(sys.argv) == 2:
        second_version()
    else:
        usage()

'''
path.suffix　　　　#文件后缀
path.stem　　　　　 #文件名不带后缀
path.name　　　　　　#带后缀的完整文件名
path.parent　　　　#路径的上级目录
 
基本用法:
Path.iterdir()　　#遍历目录的子目录或者文件
Path.is_dir()　　#判断是否是目录
Path.glob()　　#过滤目录(返回生成器)
Path.resolve()　　#返回绝对路径
/　　# 拼接路径(目录中进行导航-官网说法)
Path.exists()　　#判断路径是否存在
Path.open()　　#打开文件(支持with)
Path.unlink()　　#删除文件或目录(目录非空触发异常)
 
基本属性:
Path.parts　　#分割路径 类似os.path.split(), 不过返回元组
Path.drive　　#返回驱动器名称
Path.root　　#返回路径的根目录
Path.anchor　　#自动判断返回drive或root
Path.parents　　#返回所有上级目录的列表
 
改变路径:
Path.with_name()　　#更改路径名称, 更改最后一级路径名
Path.with_suffix()　　#更改路径后缀
/　　#拼接路径
Path.joinpath()　　#拼接路径
Path.relative_to()　　#计算相对路径
 
测试路径:
Path.match()　　#测试路径是否符合pattern
Path.is_dir()　　#是否是文件
Path.is_absolute()　　#是否是绝对路径
Path.is_reserved()　　#是否是预留路径
Path.exists()　　#判断路径是否真实存在
 
其他方法:
Path.cwd()　　#返回当前目录的路径对象
Path.home()　　#返回当前用户的home路径对象
Path.stat()　　#返回路径信息, 同os.stat()
Path.chmod()　　#更改路径权限, 类似os.chmod()
Path.expanduser()　　#展开~返回完整路径对象
Path.mkdir()　　#创建目录
Path.rename()　　#重命名路径
Path.rglob()　　#递归遍历所有子目录的文件
'''
