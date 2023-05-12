from django.shortcuts import render
from django.views import View
from django import http
from community.models import AllEssay, Comment, Support, supportComment

import json
import random
from datetime import datetime


# 文章图片上传方法
class UploadImage(View):

    def get(self, request):
        pass

    def post(self, request):
        data_img = request.FILES.get('wangeditor-uploaded-image')
        random_data = random.randint(1, 999999)
        if data_img.name:
            with open(f'./apps/community/static/images/{str(random_data)+data_img.name}', 'wb') as f:
                f.write(data_img.read())
                f.close()
            # print(data_img.name)
            return http.JsonResponse({
                "errno": 0,
                "data": {
                    "url": f"http://192.168.44.1:8000/static/images/{str(random_data)+data_img.name}",
                    "alt": data_img.name,
                    "href": f"http://192.168.44.1:8000/static/images/{str(random_data)+data_img.name}"
                }
            })
        else:
            return http.JsonResponse({
                "errno": 1,
                "message": "上传失败"
            })


# 文章视频上传方法
class UploadVideo(View):

    def get(self, request):
        pass

    def post(self, request):
        data_video = request.FILES.get('wangeditor-uploaded-video')
        print(data_video)
        random_data = random.randint(1, 999999)
        if data_video.name:
            with open(f'./apps/community/static/video/{str(random_data) + data_video.name}', 'wb+') as f:
                for chunk in data_video.chunks():  # 分块写入文件
                    f.write(chunk)
                # f.write(data_video.read())
                f.close()
            # print(data_img.name)
            return http.JsonResponse({
                "errno": 0,
                "data": {
                    "url": f"http://192.168.44.1:8000/static/images/{str(random_data) + data_video.name}",
                }
            })
        else:
            return http.JsonResponse({
                "errno": 1,
                "message": "上传失败"
            })


# 保存文章方法
class SetEssay(View):

    def get(self, request):
        pass

    def post(self, request):
        essayAuthor = json.loads(request.body)['essayAuthor']
        essayTitle = json.loads(request.body)['essayTitle']
        essayContent = json.loads(request.body)['essayContent']
        essayTime = json.loads(request.body)['essayTime']
        AllEssay.objects.create(essayAuthor=essayAuthor, essayTitle=essayTitle, essayContent=essayContent, essayTime=essayTime)
        return http.JsonResponse({'state': 'OK'})


# 获取文章
class GetAllEssay(View):

    def get(self, request):
        essay_data = AllEssay.objects.values()
        # print(list(essay_data)[0])
        return http.JsonResponse({'state': 'OK', 'data': list(essay_data)})

    def post(self, request):
        pass


# 获取某一文章
class GetEssay(View):

    def get(self, request):
        pass

    def post(self, request):
        essayId = json.loads(request.body)['essayId']
        essay_data = AllEssay.objects.values().filter(essayId=essayId)
        if essay_data:
            return http.JsonResponse({'state': 'OK', 'data': list(essay_data)})
        else:
            return http.JsonResponse({'state': 'OK', 'data': []})


# 获取用户发表文章
class GetUserEssay(View):

    def get(self, request):
        pass

    def post(self, request):
        essayAuthor = json.loads(request.body)['essayAuthor']
        essay_data = AllEssay.objects.values().filter(essayAuthor=essayAuthor)
        return http.JsonResponse({'state': 'OK', 'data': list(essay_data)})


# 文章点赞
class SupportEssay(View):

    def get(self, request):
        pass

    def post(self, request):
        essayId = json.loads(request.body)['essayId']
        supportAuthor = json.loads(request.body)['supportAuthor']
        isSupport = json.loads(request.body)['isSupport']
        item = Support.objects.values().filter(essayId=essayId, supportAuthor=supportAuthor)
        support_count = Support.objects.values().filter(essayId=essayId, isSupport=True)
        if item:
            Support.objects.filter(essayId=essayId, supportAuthor=supportAuthor).update(isSupport=isSupport)
        else:
            Support.objects.create(essayId=essayId, supportAuthor=supportAuthor, isSupport=isSupport)
        return http.JsonResponse({'state': 'OK', 'support_count': list(support_count)})


# 查看是否点赞并返回点赞数
class GetSupportEssay(View):

    def get(self, request):
        pass

    def post(self, request):
        essayId = json.loads(request.body)['essayId']
        supportAuthor = json.loads(request.body)['supportAuthor']
        item = Support.objects.values().filter(essayId=essayId, supportAuthor=supportAuthor)
        support_count = Support.objects.values().filter(essayId=essayId, isSupport=True)
        return http.JsonResponse({'state': 'OK', 'data': list(item), 'support_count': list(support_count)})


# 增加浏览量
class AddReadEssay(View):

    def get(self, request):
        pass

    def post(self, request):
        essayId = json.loads(request.body)['essayId']
        essayClicks = json.loads(request.body)['essayClicks']
        AllEssay.objects.filter(essayId=essayId).update(essayClicks=essayClicks)
        return http.JsonResponse({'state': 'OK'})


# 评论文章方法
class SetEssayComment(View):

    def get(self, request):
        pass

    def post(self, request):
        essayId = json.loads(request.body)['essayId']
        commentContent = json.loads(request.body)['commentContent']
        commentTimesss = json.loads(request.body)['commentTime']
        commentAuthor = json.loads(request.body)['commentAuthor']
        commentClicks = json.loads(request.body)['commentClicks']
        commentTime = datetime.now().strftime("%Y-%m-%d %H:%M")
        Comment.objects.create(essayId=essayId, commentContent=commentContent, commentTime=commentTime, commentAuthor=commentAuthor, commentClicks=commentClicks)
        return http.JsonResponse({'state': 'OK'})


# 获取文章全部评论
class GetEssayComment(View):

    def get(self, request):
        pass

    def post(self, request):
        essayId = json.loads(request.body)['essayId']
        item = Comment.objects.values().filter(essayId=essayId)
        return http.JsonResponse({'state': 'OK', 'data': list(item)})


# 评论点赞
class SupportComment(View):

    def get(self, request):
        pass

    def post(self, request):
        essayId = json.loads(request.body)['essayId']
        commentId = json.loads(request.body)['commentId']
        supportAuthor = json.loads(request.body)['supportAuthor']
        flag = json.loads(request.body)['flag']
        item_data = Comment.objects.values().filter(essayId=essayId, commentId=commentId)
        if list(item_data):
            addcomment = list(item_data)[0]['commentClicks'] + 1
            decomment = list(item_data)[0]['commentClicks'] - 1
        # flag=1是增加点赞，flag=2是获取点赞， flag=3是修改点赞状态
        if flag == 1:
            supportComment.objects.create(essayId=essayId, commentId=commentId, supportAuthor=supportAuthor, isSupport=True)
            Comment.objects.filter(commentId=commentId, essayId=essayId).update(commentClicks=addcomment)
            allsupport = supportComment.objects.values().filter(essayId=essayId, supportAuthor=supportAuthor)
            return http.JsonResponse({'state': 'OK', 'data': list(allsupport)})
        if flag == 2:
            allsupport = supportComment.objects.values().filter(essayId=essayId, supportAuthor=supportAuthor)
            return http.JsonResponse({'state': 'OK', 'data': list(allsupport)})
        if flag == 3:
            item = supportComment.objects.values().filter(essayId=essayId, commentId=commentId, supportAuthor=supportAuthor)
            isSupport = not (list(item)[0]['isSupport'])
            supportComment.objects.filter(essayId=essayId, commentId=commentId, supportAuthor=supportAuthor).update(isSupport=isSupport)
            if isSupport:
                Comment.objects.filter(commentId=commentId, essayId=essayId).update(commentClicks=addcomment)
            else:
                Comment.objects.filter(commentId=commentId, essayId=essayId).update(commentClicks=decomment)
            allsupport = supportComment.objects.values().filter(essayId=essayId, supportAuthor=supportAuthor)
            return http.JsonResponse({'state': 'OK', 'data': list(allsupport)})


# 删除文章方法
class DeleteEssay(View):

    def get(self, request):
        pass

    def post(self, request):
        essayId = json.loads(request.body)['essayId']
        AllEssay.objects.filter(essayId=essayId).delete()
        Comment.objects.filter(essayId=essayId).delete()
        Support.objects.filter(essayId=essayId).delete()
        supportComment.objects.filter(essayId=essayId).delete()
        return http.JsonResponse({'state': 'OK'})


# 删除评论方法
class DeleteComment(View):

    def get(self, request):
        pass

    def post(self, request):
        commentId = json.loads(request.body)['commentId']
        Comment.objects.filter(commentId=commentId).delete()
        supportComment.objects.filter(commentId=commentId).delete()
        return http.JsonResponse({'state': 'OK'})
