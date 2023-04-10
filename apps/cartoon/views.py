import os
import re

import requests
from lxml import etree
from django.shortcuts import render
from django.views import View
from django import http
from cartoon.models import LoveCartoon, HistoryCartoon
from cartoon.models import CartoonMess
import json

from apps.cartoon.resources import main_res
from apps.cartoon.resources import test_download


# 前端main路由资源
class All_cartoonView(View):

    def get(self, request):
        data_list = main_res.cartoon_list
        return http.JsonResponse({'state': 'OK', 'arr': data_list})

    def post(self, request):
        id = json.loads(request.body)['id']
        readTime = json.loads(request.body)['readTime']
        username = json.loads(request.body)['username']
        img, p_data, passage_data = main_res.get_title(id)
        item = HistoryCartoon.objects.values().filter(username=username, cartoonId=id)
        if(item):
            HistoryCartoon.objects.filter(username=username, cartoonId=id).update(readTime=readTime)
        else:
            HistoryCartoon.objects.create(username=username, cartoonName=p_data[0]['title'], cartoonImg=img, description=p_data[0]['jianjie'], cartoonId=id, readTime=readTime)
        return http.JsonResponse({'state': 'OK', 'img_data': img, 'p_data': p_data[0], 'passage_data': passage_data})


# 获取具体漫画图片
class GetImgsView(View):
    def get(self, request):
        pass

    def post(self, request):
        idx = json.loads(request.body)['idx']
        passage = json.loads(request.body)['passage']
        img_data, title, manhua_mess = main_res.get_img(idx, passage)
        return http.JsonResponse({'state': 'OK', 'img_data': img_data, 'title': title, 'manhua_mess': manhua_mess})


# 获取分类漫画资源
class GetType(View):
    def get(self, request):
        data_list_lianzai = main_res.cartoon_list2
        data_list_wanjie = main_res.cartoon_list3
        return http.JsonResponse({'state': 'OK', 'lianzai_arr': data_list_lianzai, 'wanjie_arr': data_list_wanjie})

    def post(self, request):
        pass


# 收藏漫画
class Love_Cartoon(View):
    def get(self, request):
        pass

    def post(self, request):
        username = json.loads(request.body)['username']
        cartoonName = json.loads(request.body)['cartoonName']
        cartoonImg = json.loads(request.body)['cartoonImg']
        description = json.loads(request.body)['description']
        cartoonId = json.loads(request.body)['cartoonId']
        isLove = json.loads(request.body)['isLove']
        item = LoveCartoon.objects.values().filter(username=username, cartoonId=cartoonId)
        if(item):
            LoveCartoon.objects.filter(username=username, cartoonId=cartoonId).update(isLove=isLove)
        else:
            LoveCartoon.objects.create(username=username, cartoonName=cartoonName, cartoonImg=cartoonImg, description=description, cartoonId=cartoonId, isLove=isLove)
        return http.JsonResponse({'state': 'OK'})


# 获取收藏漫画
class GetLoveCartoon(View):
    def get(self, request):
        pass

    def post(self, request):
        username = json.loads(request.body)['username']
        cartoonId = json.loads(request.body)['cartoonId']
        if cartoonId == 10010:
            data = LoveCartoon.objects.values().filter(username=username, isLove=True)
            if data:
                return http.JsonResponse({'state': 'OK', 'data_love': list(data)})
            else:
                return http.JsonResponse({'state': 'OK', 'data_love': []})
        item = LoveCartoon.objects.values().filter(username=username, cartoonId=cartoonId)
        if(item):
            return http.JsonResponse({'state': 'OK', 'isLove': list(item)[0]['isLove'], 'data_love': list(item)[0]})
        else:
            return http.JsonResponse({'state': 'OK', 'isLove': False})


# 获取漫画浏览历史
class GetHistoryCartoon(View):
    def get(self, request):
        pass

    def post(self, request):
        username = json.loads(request.body)['username']
        item = HistoryCartoon.objects.values().filter(username=username)
        if(item):
            return http.JsonResponse({'state': 'OK', 'data_history': list(item)})
        else:
            return http.JsonResponse({'state': 'OK', 'data_history': []})

# 存漫画
class SetCartoon(View):
    def get(self, request):
        print('开始!!')
        # s = '1盛大asd::s523'
        # str = re.sub('[^\u4e00-\u9fa5^a-z^A-Z^0-9]+','',s)
        # print(str)
        # 存连载漫画到数据库
        data_list2 = test_download.run2()
        print(data_list2[0])
        for data in data_list2:
            data_str = re.sub('[^\u4e00-\u9fa5^a-z^A-Z^0-9]+', '', data["title"])
            if not os.path.exists(f'./static/cartoon_resources/{data_str}'):
                os.makedirs(f'./static/cartoon_resources/{data_str}')
                res = requests.get(data['image'])
                with open(f'./static/cartoon_resources/{data_str}/{data_str}.jpg', 'wb') as f:
                    f.write(res.content)
                    f.close()
            # cartoonimg = f'http://192.168.44.1:8000/static/cartoon_resources/{data_str}/{data_str}.jpg'
            # CartoonMess.objects.create(cartoonId=data['id'], cartoonName=data_str, cartoonImg=cartoonimg)

        # 存完结漫画到数据库
        # data_list3 = test_download.run3()
        # for data in data_list2:
        #     data_str = re.sub('[^\u4e00-\u9fa5^a-z^A-Z^0-9]+', '', data["title"])
        #     if not os.path.exists(f'./static/cartoon_resources/{data_str}'):
        #         os.makedirs(f'./static/cartoon_resources/{data_str}')
        #         res = requests.get(data['image'])
        #         with open(f'./static/cartoon_resources/{data_str}/{data_str}.jpg', 'wb') as f:
        #             f.write(res.content)
        #             f.close()
        #     cartoonimg = f'http://192.168.44.1:8000/static/cartoon_resources/{data_str}/{data_str}.jpg'
        #     CartoonMess.objects.create(cartoonId=data['id'], cartoonName=data_str, cartoonImg=cartoonimg, cartoonState=1)

        # 存漫画简介到数据库
        # data_list_all = data_list2 + data_list3
        for data in data_list2:
            data_str = re.sub('[^\u4e00-\u9fa5^a-z^A-Z^0-9]+', '', data["title"])
            p_data, passage_data = test_download.get_title(data['id'])
            # CartoonMess.objects.filter(cartoonId=data['id']).update(description=p_data[0]['jianjie'],
            #                                                      cartoonAuthor=p_data[0]['author'],
            #                                                      cartoonState=p_data[0]['state'],
            #                                                      updateTime=p_data[0]['update_time'])
            print('正在下载...',data_str)
            for index, passagelist in enumerate(passage_data):
                passagelist_str = f'{index}、' + re.sub('[^\u4e00-\u9fa5^a-z^A-Z^0-9]+', '', passagelist['name'])
                test_download.get_img(passagelist['idx'], passagelist['passage'], data_str, passagelist_str)
        print("完成！")
        return http.JsonResponse({'state': 'OK'})


class MobileGetCartoon(View):
    def get(self, request):
        cartoon_list = []
        idx = 1
        all_cartoon_list = os.listdir('./static/cartoon_resources')
        # print(all_cartoon_list)
        for i in all_cartoon_list:
            cartoon_item = os.listdir(f'./static/cartoon_resources/{i}')
            if len(cartoon_item) > 1:
                cartoon_list.append({
                    'cartoonName': i,
                    'id': idx,
                    'cartoonImg': f'http://manyan.w1.luyouxia.net/static/cartoon_resources/{i}/{i}.jpg'
                })
                idx = idx + 1

        return http.JsonResponse({'state': 'OK', 'cartoon_list': cartoon_list})

    def post(self, request):
        pass


class MobileGetImgs(View):
    def get(self, request):
        pass

    def post(self, request):
        cartoonName = json.loads(request.body)['cartoonName']
        cartoon_pages = os.listdir(f'./static/cartoon_resources/{cartoonName}')
        sort_cartoon = []
        for i in cartoon_pages:
            try:
                sort_cartoon.append([int(i.split('、')[0]), i.split('、')[1]])
            except:
                break
        sort_cartoon = sorted(sort_cartoon, reverse=True)
        mulu_data = []
        for i in sort_cartoon:
            mulu_data.append(str(i[0]) + '、' + i[1])
        page = str(sort_cartoon[0][0]) + '、' + sort_cartoon[0][1]
        images = os.listdir(f'./static/cartoon_resources/{cartoonName}/{page}')
        img_list = []
        for i in images:
            img_list.append(int(i.split('.')[0]))
        img_list = sorted(img_list)
        images_data = []
        for i in img_list:
            images_data.append(f'http://manyan.w1.luyouxia.net/static/cartoon_resources/{cartoonName}/{page}/{str(i)}.jpg')
        return http.JsonResponse({'state': 'OK', 'images_data': images_data, 'mulu_data': mulu_data, 'now_page': page})


class MobileNextPage(View):
    def get(self, request):
        pass

    def post(self, request):
        cartoonName = json.loads(request.body)['cartoonName']
        page = json.loads(request.body)['page']
        images = os.listdir(f'./static/cartoon_resources/{cartoonName}/{page}')
        img_list = []
        for i in images:
            img_list.append(int(i.split('.')[0]))
        img_list = sorted(img_list)
        images_data = []
        for i in img_list:
            images_data.append(f'http://manyan.w1.luyouxia.net/static/cartoon_resources/{cartoonName}/{page}/{str(i)}.jpg')
        return http.JsonResponse({'state': 'OK', 'images_data': images_data, 'now_page': page})
