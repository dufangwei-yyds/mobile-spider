# -*- coding: utf-8 -*-
# @Time    : 2023/1/4 12:05
# @Author  : bruce
# @Email   : d920130d2@163.com
# @File    : decode_data.py.py
# @Software: PyCharm

import json
from handle_mongo import handle_save_data


def response(flow):
    #抖音
    if 'aweme/v1/feed' in flow.request.url:
        douyin_data_dict = json.loads(flow.response.text)
        for douyin_item in douyin_data_dict['aweme_list']:
            douyin_item['item_type'] = 'douyin_item'
            handle_save_data(douyin_item)
    #快手
    elif 'rest/n/feed/hot' in flow.request.url:
        kuaishou_data_dict = json.loads(flow.response.text)
        for kuaishou_item in kuaishou_data_dict['feeds']:
            kuaishou_item['item_type'] = 'kuaishou_item'
            handle_save_data(kuaishou_item)
    #今日头条
    elif 'api/news/feed' in flow.request.url:
        jrtt_data_dict = json.loads(flow.response.text)
        for jinritoutiao_item in jrtt_data_dict['data']:
            jinritoutiao_item['item_type'] = 'jinritoutiao_item'
            handle_save_data(jinritoutiao_item)

