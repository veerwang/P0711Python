---
title: OneWay工作室
---

<div align='center' ><font size='60'>进行Web服务端的编程</font></div>

## 1.创建该项目的初衷
进行Python+Django+Vue+MySQL的实验编程

## 2.判断http的服务端是否有运行
python -m http.server
可以通过浏览器访问8000，进行查看，正常是显示如下内容
就是文件列表

## 3.安装工具
pyenv:  使用系统自带的工具进行安装

## 4.django如何使用
### pyenv安装相关的python版本

``` shell
cd web-server
pyenv install 3.8.15
pyenv local 3.8.15
python --version 确认版本
```

### 创建一个Django的服务器
``` shell
pip install django
django startproject smartcube(项目名称)
cd smartcube
python manager runserver
```

### 在models中创建数据
a.修改apps中的models.py文件
b.使用makeimagration创建0001之类的数据文件
c.使用imagrate创建数据库数据

## 5.获取Django的工作目录
python -c "import django; print(django.__path__)"


参考链接:
https://developer.mozilla.org/zh-CN/docs/Learn/Server-side/Django/development_environment

## 附录
国内下载各个版本的python的路径
https://registry.npmmirror.com/binary.html?path=python/
