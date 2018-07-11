P0711Python
===========

用于学习python语言的工程

第一条：运行python与shell进行交互。
python

工程目录结构
hello.py		该文件用于熟悉python语法

第二条：单双引号都是一样的。


第三条 :当C++与Python进行混合调用的时候，.py文件会先被编译成为.pyc文件

第四条 :https://pypi.python.org/pypi/      python的各种资源库
        https://www.python.org             python的官网

第五条 :如果程序当中没有在文件的开头处
添加如下信息，那么在文件中输入中文将会出现错误。
#coding=utf-8

第六条 :如果要引用外部变量
两种方法:
a.from utils import g_print_version
  g_print_version()

b.import utils
  utils.g_print_version()

第七条: python程序进行打包
a. pip install pyinstaller   安装pyinstaller安装包
   pyinstaller --oneline main.py   这样就会将main.py相关的信息打包进入dist/main的文件中，并且是一个可执行的权限
