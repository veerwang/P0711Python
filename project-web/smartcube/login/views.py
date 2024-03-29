from django.shortcuts import render, redirect
import login.models
from django.contrib.auth.hashers import check_password
from globals.globalsvar import GlobalVars


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
            someone = None
            try:
                someone = login.models.User.objects.get(Account=username)
            except:
                message = '用户名或密码错误'
                return render(request,
                              'login/login.html', {"message": message})

                if (someone is None):
                    message = '无效用户名'
                    return render(request,
                                  'login/login.html', {"message": message})

            if (check_password(password, someone.Password)):
                GlobalVars.getInstance().account = someone.Name
                return redirect('/home/')
            else:
                message = '用户名或密码错误'
                return render(request,
                              'login/login.html', {"message": message})

    site_version = 'V1.0.0-2022.12.04'
    context = {'site_version': site_version}
    return render(request, 'login/login.html', context)
