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
    path('api/get_type/', views.GetType.as_view()),
    path('get_type/', views.GetType.as_view()),
    # 收藏漫画
    path('api/love_car/', views.Love_Cartoon.as_view()),
    path('love_car/', views.Love_Cartoon.as_view()),
    # 获取收藏漫画
    path('api/get_love/', views.GetLoveCartoon.as_view()),
    path('get_love/', views.GetLoveCartoon.as_view()),
    # 获取漫画浏览历史
    path('api/get_history/', views.GetHistoryCartoon.as_view()),
    path('get_history/', views.GetHistoryCartoon.as_view()),
    # 存漫画
    path('api/set_cartoon/', views.SetCartoon.as_view()),
    path('set_cartoon/', views.SetCartoon.as_view()),
    # 手机获取全部漫画资源
    path('api/mobile_get_cartoon/', views.MobileGetCartoon.as_view()),
    path('mobile_get_cartoon/', views.MobileGetCartoon.as_view()),
    # 手机获取具体漫画
    path('api/mobile_get_imgs/', views.MobileGetImgs.as_view()),
    path('mobile_get_imgs/', views.MobileGetImgs.as_view()),
    # 手机获取章节跳转漫画资源
    path('api/mobile_get_page_imgs/', views.MobileNextPage.as_view()),
    path('mobile_get_page_imgs/', views.MobileNextPage.as_view()),
]
