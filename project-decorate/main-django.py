#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2023年03月22日
 版本:		1.0.0
"""


def permission_check(CoreFunction):
    def checkPermission(*args, **kwargs):
        print('checkout permission')
        print(args[0])
        print(args[1])
        if args[0] != 'post':
            return {'status': 'bad'}
        return CoreFunction(*args, **kwargs)
    return checkPermission


def CheckingPermission(CoreFunction):
    def CheckingPermission(*args, **kwargs):
        print('new permission check')
        return CoreFunction(*args, **kwargs)
    return CheckingPermission


@CheckingPermission
@permission_check
def getProvinceName(request, help):
    print(request)
    print(help)
    return {'province': '福建省'}


if __name__ == '__main__':
    print("用于测试权限检查")
    info = getProvinceName('post', 'help')
    print(info)
