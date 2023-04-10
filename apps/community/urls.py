from django.urls import path
from . import views

urlpatterns = [
    # 文章图片上传路径
    path('api/upload_text_img/', views.UploadImage.as_view()),
    path('upload_text_img/', views.UploadImage.as_view()),
    # 文章视频上传路径
    path('api/upload_text_video/', views.UploadVideo.as_view()),
    path('upload_text_video/', views.UploadVideo.as_view()),
    # 保存文章
    path('api/set_essay/', views.SetEssay.as_view()),
    path('set_essay/', views.SetEssay.as_view()),
    # 获取全部文章
    path('api/get_all_essay/', views.GetAllEssay.as_view()),
    path('get_all_essay/', views.GetAllEssay.as_view()),
    # 获取用户发表文章
    path('api/get_user_essay/', views.GetUserEssay.as_view()),
    path('get_user_essay/', views.GetUserEssay.as_view()),
    # 获取某一文章
    path('api/get_essay/', views.GetEssay.as_view()),
    path('get_essay/', views.GetEssay.as_view()),
    # 文章点赞
    path('api/support_essay/', views.SupportEssay.as_view()),
    path('support_essay/', views.SupportEssay.as_view()),
    # 查看是否点赞
    path('api/get_support_essay/', views.GetSupportEssay.as_view()),
    path('get_support_essay/', views.GetSupportEssay.as_view()),
    # 增加文章浏览量
    path('api/add_read_essay/', views.AddReadEssay.as_view()),
    path('add_read_essay/', views.AddReadEssay.as_view()),
    # 保存评论
    path('api/set_essay_comment/', views.SetEssayComment.as_view()),
    path('set_essay_comment/', views.SetEssayComment.as_view()),
    # 获取文章所有评论
    path('api/get_essay_comment/', views.GetEssayComment.as_view()),
    path('get_essay_comment/', views.GetEssayComment.as_view()),
    # 评论点赞
    path('api/support_comment/', views.SupportComment.as_view()),
    path('support_comment/', views.SupportComment.as_view()),
    # 删除文章
    path('api/delete_essay/', views.DeleteEssay.as_view()),
    path('delete_essay/', views.DeleteEssay.as_view()),
    # 删除评论
    path('api/delete_comment/', views.DeleteComment.as_view()),
    path('delete_comment/', views.DeleteComment.as_view()),
]
