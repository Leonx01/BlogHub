from django.contrib.auth.views import LoginView,LogoutView
# 引用默认登陆视图，并用字典传递html模板位置
from users import views
from django.urls import path
urlpatterns=[
    path(r'login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    path(r'logout/',LogoutView.as_view(template_name='blogs/index.html'),name='logout'),
    path(r'register/',views.register,name='register'),
]