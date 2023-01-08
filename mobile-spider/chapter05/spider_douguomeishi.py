# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 10:40
# @Author  : bruce
# @Email   : d920130d2@163.com
# @File    : spider_douguomeishi.py
# @Software: PyCharm

import requests
import json
from multiprocessing import Queue
from handel_mongo import mongo_info
from concurrent.futures import ThreadPoolExecutor

'''
   多线程抓取豆果美食数据-菜谱分类页、菜谱的列表页和详情页
'''

# 创建队列
queue_list = Queue()


# 封装请求函数,相同的请求头
def handel_request(url, data):
    # (.*?):(.*)
    # "$1" : "$2",
    header = {
        "client": "4",
        "version": "6922.2",
        "device": "MI 9",
        "sdk": "22,5.1.1",
        "imei": "355757133953980",
        "channel": "zhuzhan",
        "resolution": "1600*900",
        "dpi": "2.0",
        "brand": "Xiaomi",
        "scale": "2.0",
        "timezone": "28800",
        "language": "zh",
        "cns": "2",
        "carrier": "CMCC",
        "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36",
        "reach": "1",
        "newbie": "0",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "Keep-Alive",
        "Host": "api.douguo.net",
    }

    # 设置代理ip
    # proxy = {'http': 'http://H211EATS905745KC:F8FFBC929EB7D5A7@http.cla.abuyun.com:9030'}
    # response = requests.post(url=url, headers=header, data=data, proxies=proxy)

    response = requests.post(url=url, headers=header, data=data)
    return response


# http://api.douguo.net/recipe/flatcatalogs
# & \n
# (.*?)=(.*)
# "$1" : "$2",
# client=4&_session=1671679333842864394010684761&v=1671677546&_vs=0

# 菜谱分类页面
def handle_index():
    url = 'http://api.douguo.net/recipe/flatcatalogs'
    data = {
        "client": "4",
        "_vs": "0",
    }
    response = handel_request(url=url, data=data)
    index_response_dict = json.loads(response.text)
    for index_item in index_response_dict['result']['cs']:
        for index_item_1 in index_item['cs']:
            for item in index_item_1['cs']:
                # & \n
                # (.*?)=(.*)
                # "$1" : "$2",
                # client=4&_session=1671784359727355757133953980&keyword=月饼&order=3&_vs=400
                data_2 = {
                    "client": "4",
                    "keyword": item['name'],
                    "order": "3",
                    "_vs": "400",
                }
                # 放到队列内部,put方法
                queue_list.put(data_2)


# 线程处理函数,把队列里面的数据get出来
# 菜谱的列表页和详情页
def handle_caipu_list(data):
    print('当前处理的食材: ', data['keyword'])
    caipu_list_url = 'http://api.douguo.net/recipe/v2/search/0/20'
    caipu_list_response = handel_request(url=caipu_list_url, data=data)
    caipu_list_response_dict = json.loads(caipu_list_response.text)
    for item in caipu_list_response_dict['result']['list']:
        caipu_info = {}
        caipu_info['shicai'] = data['keyword']
        if item['type'] == 13:
            caipu_info['user_name'] = item['r']['an']
            caipu_info['shicai_id'] = item['r']['id']
            caipu_info['describe'] = item['r']['cookstory'].replace('\n', '').replace(' ', '')
            caipu_info['caipu_name'] = item['r']['n']
            caipu_info['zuliao_list'] = item['r']['major']
            detail_url = 'http://api.douguo.net/recipe/detail/' + str(caipu_info['shicai_id'])
            # & \n
            # (.*?)=(.*)
            # "$1" : "$2",
            # client=4&_session=1671784359727355757133953980&author_id=0&_vs=2803&_ext={"query":{"kw":"月饼","src":"2803","idx":"3","type":"13","id":"958309"}}
            detail_data = {
                "client": "4",
                "author_id": "0",
                "_vs": "2803",
                "_ext": '{"query":{"kw":' + str(
                    caipu_info['shicai']) + ',"src":"2803","idx":"3","type":"13","id":' + str(
                    caipu_info['shicai_id']) + '}}',
            }
            detail_response = handel_request(url=detail_url, data=detail_data)
            detail_response_dict = json.loads(detail_response.text)
            caipu_info['tips'] = detail_response_dict['result']['recipe']['tips']
            caipu_info['cook_step'] = detail_response_dict['result']['recipe']['cookstep']

            # print(json.dumps(caipu_info, ensure_ascii=False))

            # 把数据存放到mongodb中
            print('当前入库的菜谱是: ', caipu_info['caipu_name'])
            mongo_info.insert_item(caipu_info)
        else:
            continue


if __name__ == '__main__':
    handle_index()

    # 实现多线程抓取,引入线程池
    pool = ThreadPoolExecutor(max_workers=20)
    while queue_list.qsize() > 0:
        pool.submit(handle_caipu_list, queue_list.get())

    # handle_caipu_list(queue_list.get())
