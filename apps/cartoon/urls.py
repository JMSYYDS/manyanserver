from django.urls import path
from . import views

urlpatterns = [
    # 展示漫画页资源
    path('api/main_cartoon/', views.All_cartoonView.as_view()),
    path('main_cartoon/', views.All_cartoonView.as_view()),
    # 获取具体图片
    path('api/get_imgs/', views.GetImgsView.as_view()),
    path('get_imgs/', views.GetImgsView.as_view()),
    # 获取分类漫画资源
    path('get_type/', views.GetType.as_view()),
    path('api/get_type/', views.GetType.as_view()),
]
