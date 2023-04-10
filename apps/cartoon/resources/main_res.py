# import requests
# from lxml import etree
#
#
# url = 'http://www.qiruiyaoye.cn/category/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
# }
# # proxy = {
# #     'http': '101.200.127.149'
# # }
# data_list = []
#
#
# # 获取所有漫画信息
# def parse_data(urls):
#     try:
#         response = requests.get(urls, headers=headers)
#         data = response.content
#         # data = data.decode().replace("<!--", "").replace("-->", "")
#         # 创建element对象
#         html = etree.HTML(data)
#         el_list = html.xpath('/html/body/section[2]/div/ul/li/div')
#         # print(len(el_list))
#         for el in el_list:
#             index = el.xpath('./a/@href')[0][6:-1]
#             temp = {}
#             temp['id'] = index
#             temp['title'] = el.xpath("./div//a/text()")[0]
#             temp['describe'] = el.xpath("./div/p[2]/text()")[0]
#             temp['image'] = 'http://www.qiruiyaoye.cn/upload/book/' + str(index) +'.jpg'
#             data_list.append(temp)
#     except Exception as e:
#         return 'error'
#
#
# def run():
#     if (len(data_list) != 0):
#         data_list.clear()
#     # headers
#     n = True
#     # 发送请求 获取响应
#     urls = url
#     index = 1
#     while(n):
#         index += 1
#         # 从响应中提取数据
#         tip = parse_data(urls)
#         if(tip == 'error'):
#             return data_list
#         else:
#             urls = 'http://www.qiruiyaoye.cn/category/page/' + str(index) + '.html'
#
#
# cartoon_list = run()
#
#
# data_list2 = []
#
#
# # 获取连载漫画
# def parse_data2(urls):
#     try:
#         response = requests.get(urls, headers=headers)
#         data = response.content
#         # data = data.decode().replace("<!--", "").replace("-->", "")
#         # 创建element对象
#         html = etree.HTML(data)
#         el_list = html.xpath('/html/body/section[2]/div/ul/li/div')
#         # print(len(el_list))
#         for el in el_list:
#             index = el.xpath('./a/@href')[0][6:-1]
#             temp = {}
#             temp['id'] = index
#             temp['title'] = el.xpath("./div//a/text()")[0]
#             temp['describe'] = el.xpath("./div/p[2]/text()")[0]
#             temp['image'] = 'http://www.qiruiyaoye.cn/upload/book/' + str(index) +'.jpg'
#             data_list2.append(temp)
#     except Exception as e:
#         return 'error'
#
#
# def run2():
#     if (len(data_list2) != 0):
#         data_list2.clear()
#     # headers
#     n = True
#     index = 1
#     # 发送请求 获取响应
#     urls = 'http://www.qiruiyaoye.cn/category/end/0/'
#     while(n):
#         index += 1
#         # 从响应中提取数据
#         tip = parse_data2(urls)
#         if(tip == 'error'):
#             return data_list2
#         else:
#             urls = 'http://www.qiruiyaoye.cn/category/end/0/page/' + str(index) + '.html'
#
# cartoon_list2 = run2()
#
# data_list3 = []
#
#
# # 获取完结漫画
# def parse_data3(urls):
#     try:
#         response = requests.get(urls, headers=headers)
#         data = response.content
#         # data = data.decode().replace("<!--", "").replace("-->", "")
#         # 创建element对象
#         html = etree.HTML(data)
#         el_list = html.xpath('/html/body/section[2]/div/ul/li/div')
#         # print(len(el_list))
#         for el in el_list:
#             index = el.xpath('./a/@href')[0][6:-1]
#             temp = {}
#             temp['id'] = index
#             temp['title'] = el.xpath("./div//a/text()")[0]
#             temp['describe'] = el.xpath("./div/p[2]/text()")[0]
#             temp['image'] = 'http://www.qiruiyaoye.cn/upload/book/' + str(index) +'.jpg'
#             data_list3.append(temp)
#     except Exception as e:
#         return 'error'
#
#
# def run3():
#     if (len(data_list3) != 0):
#         data_list3.clear()
#     # headers
#     n = True
#     index = 1
#     # 发送请求 获取响应
#     urls = 'http://www.qiruiyaoye.cn/category/end/1/'
#     while(n):
#         index += 1
#         # 从响应中提取数据
#         tip = parse_data3(urls)
#         if(tip == 'error'):
#             return data_list3
#         else:
#             urls = 'http://www.qiruiyaoye.cn/category/end/1/page/' + str(index) + '.html'
#
# cartoon_list3 = run3()
#
#
# # 获取章节页数据
# def get_title(id):
#
#     url1 = f'http://www.qiruiyaoye.cn/book/{str(id)}/'
#     response = requests.get(url1, headers=headers)
#     data = response.content
#     html = etree.HTML(data)
#     img = 'http://www.qiruiyaoye.cn' + html.xpath('/html/body/div[1]/section/div[2]/div[1]/img/@src')[0]
#     # 漫画简介值
#     p_data = []
#     idx = 1
#     el_list = html.xpath('/html/body/div[1]/section/div[2]/div[2]')
#     for el in el_list:
#         temp = {}
#         temp['id'] = idx
#         temp['title'] = el.xpath('./h1/text()')[0]
#         temp['author'] = el.xpath('./p/a/text()')[0]
#         temp['state'] = el.xpath('./p/span/span/text()')[0]
#         temp['update_time'] = el.xpath('./p/span[2]/text()')[0]
#         temp['jianjie'] = el.xpath('./p[4]/text()')[0]
#         p_data.append(temp)
#         idx += 1
#     el_list2 = html.xpath('//*[@id="detail-list-select"]/li/h2/a')
#     # 漫画相应地址
#     passage_data = []
#     idz = 1
#     for el in el_list2:
#         temp = {}
#         temp['id'] = idz
#         temp['name'] = el.xpath('./text()')[0]
#         str1 = el.xpath('./@href')[0][9:-5]
#         list1 = str1.split('/')
#         temp['idx'] = list1[0]
#         temp['passage'] = list1[1]
#         passage_data.append(temp)
#         idz += 1
#
#     return img, p_data, passage_data
#
#
# # 获取漫画数据
# def get_img(idx, passage):
#     url2 = 'http://www.qiruiyaoye.cn/chapter/' + str(idx) + '/' + str(passage) + '.html'
#     headers2 = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
# }
#     response = requests.get(url2, headers=headers2)
#     data = response.content
#     html = etree.HTML(data)
#     el_list1 = html.xpath('//*[@id="content"]/div[2]/div/div/img')
#     id = 1
#     data_img = []
#     for i in el_list1:
#         temp = {}
#         temp['id'] = id
#         temp['img_address'] = i.xpath('./@data-original')[0]
#         data_img.append(temp)
#         id += 1
#
#     id2 = 1
#     title_img = []
#     el_list2 = html.xpath('/html/body/div[3]/div[2]/div/div[1]/ul/li/h3/a')
#     for el in el_list2:
#         temp2 = {}
#         temp2['id'] = id2
#         temp2['title'] = el.xpath('./text()')[0]
#         temp2['address'] = el.xpath('./@href')[0][11:-5]
#         title_img.append(temp2)
#         id2 += 1
#
#     el_list3 = html.xpath('/html/body/div[2]/div/h1/text()')
#     manhua_mess = el_list3[0]
#     return data_img, title_img, manhua_mess
#
#
# # if __name__ == '__main__':
# #     print(run())
