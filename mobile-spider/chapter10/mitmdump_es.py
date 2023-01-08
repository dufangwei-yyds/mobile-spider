import json
import time
import datetime
from elasticsearch import Elasticsearch, helpers

# 连接es
es = Elasticsearch(hosts="192.168.0.101:9200")


def handle_time(date_time=None, key=None):
    """处理时间方法"""
    if not date_time:
        date_time = time.time()
        if key == "create_time":
            otherStyleTime = datetime.datetime.utcfromtimestamp(date_time).strftime("%Y-%m-%d %H:%M:%S")
            return otherStyleTime
        elif key == "birthday":
            otherStyleTime = datetime.datetime.utcfromtimestamp(date_time).strftime("%Y-%m-%d")
            return otherStyleTime
    else:
        if isinstance(date_time, float) or isinstance(date_time, int):
            otherStyleTime = datetime.datetime.utcfromtimestamp(date_time).strftime("%Y-%m-%d %H:%M:%S")
            return otherStyleTime
        return date_time


def response(flow):
    """解析10版本抖音app返回数据"""
    # 解析视频数据
    if 'https://aweme-eagle.snssdk.com/aweme/v1/feed' in flow.request.url:
        data_list = []
        # 使用json来loads response.text
        video_response = json.loads(flow.response.text)
        for item in video_response.get("aweme_list"):
            info = {
                "_index": "douyin_data_%s" % handle_time(key="birthday"),
                "_source": {
                    # 用户id
                    "author_user_id": item.get("author_user_id"),
                    # 抖音id
                    "aweme_id": item.get("aweme_id"),
                    # 出生日期
                    "birthday": handle_time(item.get("author", {}).get("birthday"), key="birthday"),
                    # 性别
                    "gender": item.get("author", {}).get("gender"),
                    # 昵称
                    "nickname": item.get("author", {}).get("nickname"),
                    # 归属地
                    "region": item.get("author", {}).get("region"),
                    # 个人描述
                    "person_desc": item.get("author", {}).get("signature"),
                    # 视频创建时间
                    "video_create_time": handle_time(item.get("create_time"), key="create_time"),
                    # 视频描述
                    "video_desc": item.get("desc"),
                    # 音乐信息
                    "mp3_info": item.get("music", {}).get("play_url", {}).get("uri", ""),
                    # 视频分享信息
                    "video_share_info": item.get("share_url"),
                    # 视频转发信息
                    "video_forward_info": item.get("statistics"),
                    # 爬取时间
                    "crawl_time": handle_time(date_time=time.time())
                }
            }
            print(info)
            data_list.append(info)
        # 通过helpers插入数据
        helpers.bulk(es, data_list)
