from django.contrib.auth.views import LoginView
# 引用默认登陆视图，并用字典传递html模板位置
from django.urls import path
urlpatterns=[
    path(r'login/',LoginView.as_view(template_name='users/login.html'),name='login')
]