#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年10月10日 
# 版本:		1.0.0     

import os

# 进行文件操作异常实验
def raise_test():
    try:
        fhandle = open('README','w')
        fhandle.write('hello the world\n')
        # Exception 也可以自行发出
        raise Exception('Specail Exception','kevin')
        fhandle.close()
    # 对于特定的异常可以通过 type(Exception) 来确认
    except FileNotFoundError as fe:
        print('File No Found')
    # Exception是全部异常的基类
    except Exception as e: 
        print(type(e))
        print(e.args)
        print(e)
    # 如果没有异常进入的分支
    else:
        print('open file OK')
    # 无论如何都会执行的代码 
    finally:
        print("Open File With READ right finish")

# 进行文件操作异常实验
def exception_test():
    try:
        fhandle = open('README','w')
        fhandle.write('hello the world\n')
        fhandle.close()
    # 对于特定的异常可以通过 type(Exception) 来确认
    except FileNotFoundError as fe:
        print('File No Found')
    # Exception是全部异常的基类
    except Exception as e: 
        print(type(e))
        print(e.args)
        print(e)
    # 如果没有异常进入的分支
    else:
        print('open file OK')
    # 无论如何都会执行的代码 
    finally:
        print("Open File With READ right finish")

if __name__ == '__main__':
    print("hello the world")
    #exception_test()
    raise_test()
