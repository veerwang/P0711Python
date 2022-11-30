from django.urls import path

from . import views

# 添加命名空间后，对应的index.hml文件也要进行修改
app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
]
