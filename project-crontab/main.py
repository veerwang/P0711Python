#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2021年04月19日
 版本:		1.0.0
"""


from crontab import CronTab


def createJobs():
    """docstring for c
    Description:
    Args:
    Returns:
    Raises:
    """
    cron = CronTab(user='kevin')
    job = cron.new(command='echo hello_world')
    job.minute.every(1)
    cron.write()
    return cron, job


def delJobs(cron, job):
    """docstring for delJob
    Description:
    Args:
    Returns:
    Raises:
    """
    cron.remove(job)


if __name__ == '__main__':
    cron, job = createJobs()
    delJobs(cron, job)
