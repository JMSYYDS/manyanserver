from django.shortcuts import render
from django.views import View
from django import http
import json

from apps.cartoon.resources import main_res


# 前端main路由资源
class All_cartoonView(View):

    def get(self, request):
        data_list = main_res.cartoon_list
        return http.JsonResponse({'state': 'OK', 'arr': data_list})

    def post(self, request):
        id = json.loads(request.body)['id']
        img, p_data, passage_data = main_res.get_title(id)
        return http.JsonResponse({'state': 'OK', 'img_data': img, 'p_data': p_data[0], 'passage_data': passage_data})


# 获取具体漫画图片
class GetImgsView(View):
    def get(self, request):
        pass

    def post(self, request):
        idx = json.loads(request.body)['idx']
        passage = json.loads(request.body)['passage']
        img_data, title = main_res.get_img(idx, passage)
        return http.JsonResponse({'state': 'OK', 'img_data': img_data, 'title': title})


# 获取分类漫画资源
class GetType(View):

    def get(self, request):
        data_list_lianzai = main_res.cartoon_list2
        data_list_wanjie = main_res.cartoon_list3
        return http.JsonResponse({'state': 'OK', 'lianzai_arr': data_list_lianzai, 'wanjie_arr': data_list_wanjie})

    def post(self, request):
        pass

