# -*- coding: utf-8 -*-
# @Time     : 2023/1/3 9:51
# @Author   : bruce
# @Email    : d920130d2@163.com
# @File     : decode_douyin_fans.py
# @Software : PyCharm

# def response(flow):
#     if 'aweme/v1/user/follower/list/' in flow.request.url:
#         with open('user.txt', 'w') as f:
#             f.write(flow.response.text)

import json
try:
    from chapter06.handle_mongo import save_task
except:
    from handle_mongo import save_task

# 必须的格式
def response(flow):
    # 通过抓包软件获取请求的接口
    if 'aweme/v1/user/follower/list/' in flow.request.url:
        # 数据的解析
        for user in json.loads(flow.response.text)['followers']:
            douyin_info = {}
            douyin_info['share_id'] = user['uid']
            douyin_info['douyin_id'] = user['short_id']
            save_task(douyin_info)


