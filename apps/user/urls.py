from django.urls import path
from . import views

urlpatterns = [
    # 注册
    path('api/register/', views.RegisterView.as_view()),
    path('register/', views.RegisterView.as_view()),
    # 登录
    path('api/login/', views.LoginView.as_view()),
    path('login/', views.LoginView.as_view()),
]