import os

import requests
from lxml import etree
from cartoon.models import CartoonMess


url = 'http://www.qiruiyaoye.cn/category/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
}
# proxy = {
#     'http': '101.200.127.149'
# }
# data_list = []


# # 获取漫画数据
def get_img(idx, passage, cartoonName, passageName):
    if not os.path.exists(f'./static/cartoon_resources/{cartoonName}/{passageName}'):
        url2 = 'http://www.qiruiyaoye.cn/chapter/' + str(idx) + '/' + str(passage) + '.html'
        headers2 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        response = requests.get(url2, headers=headers2)
        data = response.content
        html = etree.HTML(data)
        el_list1 = html.xpath('//*[@id="content"]/div[2]/div/div/img')

        os.makedirs(f'./static/cartoon_resources/{cartoonName}/{passageName}')
        print(f'正在下载...{cartoonName}--{passageName}')
        for index, i in enumerate(el_list1):
            img_url = i.xpath('./@data-original')[0]
            res = requests.get(img_url)
            with open(f'./static/cartoon_resources/{cartoonName}/{passageName}/{index}.jpg', 'wb') as f:
                f.write(res.content)
                f.close()

data_list2 = []
# 获取连载漫画
def parse_data2(urls):
    try:
        response = requests.get(urls, headers=headers)
        data = response.content
        # data = data.decode().replace("<!--", "").replace("-->", "")
        # 创建element对象
        html = etree.HTML(data)
        el_list = html.xpath('/html/body/section[2]/div/ul/li/div')
        # print(len(el_list))
        for el in el_list:
            index = el.xpath('./a/@href')[0][6:-1]
            temp = {}
            temp['id'] = index
            temp['title'] = el.xpath("./div//a/text()")[0]
            temp['describe'] = el.xpath("./div/p[2]/text()")[0]
            temp['image'] = 'http://www.qiruiyaoye.cn/upload/book/' + str(index) +'.jpg'
            data_list2.append(temp)
    except Exception as e:
        return 'error'


def run2():
    print('下载图片')
    if (len(data_list2) != 0):
        data_list2.clear()
    # headers
    n = True
    index = 1
    # 发送请求 获取响应
    urls = 'http://www.qiruiyaoye.cn/category/page/1.html'
    while(n):
        index += 1
        # 从响应中提取数据
        tip = parse_data2(urls)
        if(index > 5):
            return data_list2
        else:
            urls = 'http://www.qiruiyaoye.cn/category/page/' + str(index) + '.html'

data_list3 = []
# 获取完结漫画
def parse_data3(urls):
    try:
        response = requests.get(urls, headers=headers)
        data = response.content
        # data = data.decode().replace("<!--", "").replace("-->", "")
        # 创建element对象
        html = etree.HTML(data)
        el_list = html.xpath('/html/body/section[2]/div/ul/li/div')
        # print(len(el_list))
        for el in el_list:
            index = el.xpath('./a/@href')[0][6:-1]
            temp = {}
            temp['id'] = index
            temp['title'] = el.xpath("./div//a/text()")[0]
            temp['describe'] = el.xpath("./div/p[2]/text()")[0]
            temp['image'] = 'http://www.qiruiyaoye.cn/upload/book/' + str(index) +'.jpg'
            data_list3.append(temp)
    except Exception as e:
        return 'error'


def run3():
    if (len(data_list3) != 0):
        data_list3.clear()
    # headers
    n = True
    index = 1
    # 发送请求 获取响应
    urls = 'http://www.qiruiyaoye.cn/category/end/1/'
    while(n):
        index += 1
        # 从响应中提取数据
        tip = parse_data3(urls)
        if(index > 10):
            return data_list3
        else:
            urls = 'http://www.qiruiyaoye.cn/category/end/1/page/' + str(index) + '.html'


# 获取章节页数据
def get_title(id):

    url1 = f'http://www.qiruiyaoye.cn/book/{str(id)}/'
    response = requests.get(url1, headers=headers)
    data = response.content
    html = etree.HTML(data)
    # 漫画简介值
    p_data = []
    idx = 1
    el_list = html.xpath('/html/body/div[1]/section/div[2]/div[2]')
    for el in el_list:
        temp = {}
        temp['id'] = idx
        temp['title'] = el.xpath('./h1/text()')[0]
        temp['author'] = el.xpath('./p[1]/a/text()')[0]
        temp['state'] = el.xpath('./p[2]/span/span/text()')[0]
        temp['update_time'] = el.xpath('./p[2]/span[2]/text()')[0]
        temp['jianjie'] = el.xpath('./p[4]/text()')[0]
        taglist = el.xpath('./p[3]/span/a/text()')
        tag = '、'.join(taglist)
        temp['tag'] = tag
        p_data.append(temp)
        idx += 1
    el_list2 = html.xpath('//*[@id="detail-list-select"]/li/h2/a')
    # 漫画相应地址
    passage_data = []
    idz = 1
    for el in el_list2:
        temp = {}
        temp['id'] = idz
        temp['name'] = el.xpath('./text()')[0]
        str1 = el.xpath('./@href')[0][9:-5]
        list1 = str1.split('/')
        temp['idx'] = list1[0]
        temp['passage'] = list1[1]
        passage_data.append(temp)
        idz += 1

    return p_data, passage_data

# if __name__ == '__main__':
#     # 存连载漫画到数据库
#     data_list2 = run2()
#     for data in data_list2:
#         os.mkdir(f'../static/cartoon_resources/{data.title}')
#         res = requests.get(data.image)
#         with open(f'../static/cartoon_resources/{data.title}/{data.title}.jpg', 'wb') as f:
#             f.write(res.content)
#             f.close()
#         cartoonimg = f'http://192.168.44.1:8000/static/cartoon_resources/{data.title}/{data.title}.jpg'
#         CartoonMess.objects.create(cartoonId=data.id, cartoonName=data.title, cartoonImg=cartoonimg, cartoonState=0)
#
#     # 存完结漫画到数据库
#     data_list3 = run3()
#     for data in data_list2:
#         os.mkdir(f'../static/cartoon_resources/{data.title}')
#         res = requests.get(data.image)
#         with open(f'../static/cartoon_resources/{data.title}/{data.title}.jpg', 'wb') as f:
#             f.write(res.content)
#             f.close()
#         cartoonimg = f'http://192.168.44.1:8000/static/cartoon_resources/{data.title}/{data.title}.jpg'
#         CartoonMess.objects.create(cartoonId=data.id, cartoonName=data.title, cartoonImg=cartoonimg, cartoonState=1)
#
#     # 存漫画简介到数据库
#     data_list_all = data_list2 + data_list3
#     for data in data_list_all:
#         p_data, passage_data = get_title(data.id)
#         CartoonMess.objects.filter(cartoonId=data.id).update(description=p_data[0].jianjie, cartoonState=p_data[0].state, cartoonAuthor=p_data[0].author, updateTime=p_data[0].update_time)
#         for passagelist in passage_data:
#             get_img(passagelist.idx, passagelist.passage, data.title, passagelist.name)
