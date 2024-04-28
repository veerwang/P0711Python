#! /usr/bin/env python3
# coding=utf-8

"""
 description:
 author:		kevin.wang
 create date:	2024-04-22
 version:		1.0.0
"""

from functools import wraps

class CommandExecutor:
    def __init__(self):
        self.last_command_str = None

def write_command_name(func):
    # keep raw function information
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 确保至少有一个参数，并且它是CommandExecutor类的实例
        if args and isinstance(args[0], CommandExecutor):
            args[0].last_command_str = func.__name__
        return func(*args, **kwargs)
    return wrapper

@write_command_name
def reset(executor, name):
    print(f'Resetting {name}')
    return f'{name} has been reset'

# 使用示例
executor = CommandExecutor()
result = reset(executor, 'system')
print(result)
print(executor.last_command_str)  # 应该输出 'reset'
