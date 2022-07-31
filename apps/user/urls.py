from django.urls import path
from . import views

urlpatterns = [
    # 注册
    path('api/register/', views.RegisterView.as_view()),
    path('register/', views.RegisterView.as_view()),
    # 登录
    path('api/login/', views.LoginView.as_view()),
    path('login/', views.LoginView.as_view()),
    # 退出登录
    path('api/login_out/', views.LoginOutView.as_view()),
    path('login_out/', views.LoginOutView.as_view()),
    # 上传头像
    path('api/upload_img/', views.UploadHeadView.as_view()),
    path('upload_img/', views.UploadHeadView.as_view()),
    # 获取头像
    path('api/get_img/', views.GetHeadImgView.as_view()),
    path('get_img/', views.GetHeadImgView.as_view()),
]