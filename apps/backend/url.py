from django.urls import path
from . import views

urlpatterns = [
    # 提供网页
    path('news/', views.TestView.as_view()),
]