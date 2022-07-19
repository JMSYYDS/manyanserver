from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django import http
from django.db import DatabaseError
from django.contrib.auth import login, authenticate, logout

from user.models import User
import json


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
        try:
            user = User.objects.create_user(username=username, password=password, mobile=mobile)
        except DatabaseError:
            return http.JsonResponse({'state': 'error', 'tip': '用户名已注册'})
        count = User.objects.filter(mobile=mobile).count()
        if(count):
            return http.JsonResponse({'state': 'error', 'tip': '手机号已注册'})
        # 实现状态保持
        login(request, user)
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
            return http.JsonResponse({'state': 'error', 'tip': '用户名或密码错误'})
        # 状态保持
        login(request, user)
        us = User.objects.get(mobile = username)
        return http.JsonResponse({'state': 'OK', 'username': str(us)})
