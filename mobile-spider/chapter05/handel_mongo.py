# -*- coding: utf-8 -*-
# @Time     : 2022/12/23 10:54
# @Author   : bruce
# @Email    : d920130d2@163.com
# @File     : handel_mongo.py
# @Software : PyCharm

import pymongo
from pymongo.collection import Collection


class connect_mongo(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='192.168.0.110', port=27017)
        self.db_data = self.client['douguo_meishi']

    def insert_item(self, item):
        db_collection = Collection(self.db_data, 'douguo_meishi_item')
        db_collection.insert_one(item)


mongo_info = connect_mongo()
