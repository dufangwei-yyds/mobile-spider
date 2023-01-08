# -*- coding: utf-8 -*-
# @Time    : 2023/1/5 10:21
# @Author  : bruce
# @Email   : d920130d2@163.com
# @File    : decode_douyin.py
# @Software: PyCharm

# 特别注意：
# 在新版本的抖音中，我们是找不到正常的数据返回的
# 当前使用的是10.0版本的抖音app，大家一定要注意
# 个人信息页接口
# https://aweme-eagle.snssdk.com/aweme/v1/user/?user_id=2287425540603423
# https://aweme.snssdk.com/aweme/v1/aweme/post/?user_id=2287425540603423

# 滑动视频的接口
# https://aweme-eagle.snssdk.com/aweme/v1/feed
# https://aweme-eagle.snssdk.com/aweme/v1/feed

import json


def response(flow):
    """解析10版本抖音app返回数据"""
    # 视频
    if 'https://aweme-eagle.snssdk.com/aweme/v1/feed' in flow.request.url:
        # 使用json来loadsresponse.text
        video_response = json.loads(flow.response.text)
        video_list = video_response.get("aweme_list", [])
        for item in video_list:
            print(item.get("desc"), "")

    # 发布者页面
    if 'https://aweme.snssdk.com/aweme/v1/aweme/post/?user_id' in flow.request.url:
        person_response = json.loads(flow.response.text)
        person_info = person_response.get("user", "")
        if person_info:
            info = {
                'nickname': person_info.get("nickname", ""),
                'total_favorited': person_info.get("total_favorited", 0),
                'following_count': person_info.get("following_count", 0),
                'douyin_id': person_info.get("unique_id", ""),
                'follower_count': person_info.get("follower_count", 0)
            }
            print(info)
