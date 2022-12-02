from django.db import models
from django.contrib.auth.hashers import make_password

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
    Account = models.CharField(max_length=32,
                               verbose_name='登陆账户', unique=True)
    # 显示用户的名称，例如厦门水文站
    Name = models.CharField(max_length=64,
                            verbose_name='用户名称',
                            default='用户名称')
    # 密码, Hash-256
    Password = models.CharField(max_length=256, verbose_name='登陆密码')
    # 权限 超级管理员,管理员，用户
    SUPPERADMIN = 'super'
    ADMIN = 'admin'
    CUSTOM = 'custom'
    AUTH_CHOICE = [(SUPPERADMIN, '超级管理员'), (ADMIN, '管理员'), (CUSTOM, '普通用户')]
    Authority = models.CharField(max_length=10,
                                 default='custom',
                                 choices=AUTH_CHOICE,
                                 verbose_name='权限类型')
    # 属地省
    LocationProvince = models.CharField(max_length=48, verbose_name='省级属地')
    # 属地市
    LocationCity = models.CharField(max_length=48, verbose_name='市级属地')
    # 属地Arae
    LocationArea = models.CharField(max_length=48, verbose_name='区县属地')

    def save(self, *args, **kwargs):
        self.Password = make_password(self.Password, None, 'pbkdf2_sha256')
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.Name
