# -*- coding: utf-8 -*-
# @Time     : 2023/1/2 20:02
# @Author   : bruce
# @Email    : d920130d2@163.com
# @File     : handle_mongo.py
# @Software : PyCharm

import pymongo
from pymongo.collection import Collection

"""
   保存数据到mongodb数据库 & 读取douyin_hot_id.txt
"""

client = pymongo.MongoClient(host='192.168.0.110', port=27017)
db = client['douyin']


def send_task():
    with open('douyin_hot_id.txt', 'r') as f:
        f_read = f.readlines()
        for i in f_read:
            task_info = {}
            task_info['share_id'] = i.replace('\n', '')
            task_info['task_type'] = 'share_id'
            print('当前保存的task为%s:' % task_info)
            save_task(task_info)


def save_task(task):
    task_collections = Collection(db, 'douyin_task')
    task_collections.update({'share_id': task['share_id']}, task, True)


def get_task(task_type):
    task_collections = Collection(db, 'douyin_task')
    task = task_collections.find_one_and_delete({'task_type': task_type})
    return task


def delete_task(task):
    pass


def save_data(item):
    data_collections = Collection(db, 'douyin_data')
    data_collections.insert(item)
