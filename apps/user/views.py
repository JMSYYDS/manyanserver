import os.path

from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django import http
from django.db import DatabaseError
from django.contrib.auth import login, authenticate, logout

from user.models import User
import json
import base64


# 注册类
class RegisterView(View):

    def get(self, request):
        pass

    def post(self, request):
        username = json.loads(request.body)['username']
        password = json.loads(request.body)['password']
        mobile = json.loads(request.body)['mobile']
        if not all([username, password, mobile]):
            return http.HttpResponseForbidden('缺少必传参数')
        count = User.objects.filter(mobile=mobile).count()
        if (count == 1):
            return http.JsonResponse({'state': 'error', 'tip': '手机号已注册'})
        try:
            user = User.objects.create_user(username=username, password=password, mobile=mobile)
        except DatabaseError:
            return http.JsonResponse({'state': 'error', 'tip': '用户名已注册'})
        # 实现状态保持
        login(request, user)
        with open(f'./apps/user/static/imgs/headimg.jpeg', 'rb') as f1:
            with open(f'./apps/user/static/headImg/{username}.png', 'wb') as f:
                f.write(f1.read())
                f.close()
            f1.close()
        return http.JsonResponse({'state': 'OK', 'username': username})


# 登录类
class LoginView(View):

    def get(self, request):
        pass

    def post(self, request):
        username = json.loads(request.body)['username']
        password = json.loads(request.body)['password']
        if not all([username, password]):
            return http.HttpResponseForbidden('缺少必传参数')

        # 认证用户:使用账号查询用户是否存在
        user = authenticate(username=username, password=password)
        if user is None:
            return http.JsonResponse({'state': 'error', 'tip': '手机号或密码错误'})
        # 状态保持
        login(request, user)
        us = User.objects.get(mobile=username)

        return http.JsonResponse({'state': 'OK', 'username': str(us)})


# 退出登录
class LoginOutView(View):

    def get(self, request):
        logout(request)
        return http.JsonResponse({'state': 'OK'})


# 用户上传头像
class UploadHeadView(View):

    def get(self, request):
        pass

    def post(self, request):
        username = json.loads(request.body)['username']
        base64_data = json.loads(request.body)['base64_data']
        data = base64_data.split(',')[1]
        image_data = base64.b64decode(data)
        with open(f'./apps/user/static/headImg/{username}.png', 'wb') as f:
            f.write(image_data)
            f.close()
        if(base64_data):
            User.objects.filter(username=username).update(
                head_img=base64_data
            )
        else:
            return http.JsonResponse({'state': 'error'})
        return http.JsonResponse({'state': 'OK'})


# 用户获取头像
class GetHeadImgView(View):

    def post(self, request):
        username = json.loads(request.body)['username']
        try:
            user = User.objects.get(username=username)
            if(user.head_img):
                return http.JsonResponse({'state': 'OK', 'img_data': user.head_img})
            else:
                return http.JsonResponse({'state': 'error', 'img_data': ''})
        except Exception:
            return http.JsonResponse({'state': 'error', 'message': '没有头像'})


# 修改昵称
class UpdateUsername(View):

    def post(self, request):
        username = json.loads(request.body)['username']
        newusername = json.loads(request.body)['newusername']
        User.objects.filter(username=username).update(username=newusername)
        path = 'E:/virtualenv/django_project/bookmanager01/apps/user'
        os.rename(f'{path}/static/headImg/{username}.png', f'{path}/static/headImg/{newusername}.png')
        return http.JsonResponse({'state': 'OK'})


# 修改密码
class UpdatePassword(View):

    def post(self, request):
        username = json.loads(request.body)['username']
        password = json.loads(request.body)['password']
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        return http.JsonResponse({'state': 'OK'})
