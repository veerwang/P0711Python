from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11, default='13488508087')

    def __str__(self):
        return self.first_name + self.last_name + ':' + self.phone_number


class User(models.Model):
    """正式的用户数据，用于管理账户"""
    # 登陆输入的用户名英文 xmadmin
    Account = models.CharField(max_length=32, unique=True)
    # 显示用户的名称，例如厦门水文站
    Name = models.CharField(max_length=64,
                            default=bytes('用户名', encoding='utf-8'))
    # 密码, Hash-256
    Password = models.CharField(max_length=256)
    # 权限 超级管理员,管理员，用户
    Authority = models.IntegerField(default=0)
    # 属地省
    LocationProvince = models.CharField(max_length=48)
    # 属地市
    LocationCity = models.CharField(max_length=48)
    # 属地Arae
    LocationArea = models.CharField(max_length=48)

    def __str__(self):
        return self.Name
