from django.shortcuts import render, redirect
import login.models

from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                print(username)
                print(password)
            except:
                return render(request, 'login/login.html')
            if password == password:
                return redirect('/home/')
    return render(request, 'login/login.html')
