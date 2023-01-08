import random
import time
import struct
import socket
from elasticsearch import Elasticsearch, helpers

# 连接es
es = Elasticsearch(hosts="192.168.0.101:9200")

# 读取昵称列表
with open("nickname.txt", "r", encoding="utf-8") as f:
    nickname = f.readlines()

# 读取个性签名列表
with open("个性签名.txt", "r", encoding="utf-8") as f:
    gexing = f.readlines()

# 读取tag列表
with open("tag.txt", "r", encoding="utf-8") as f:
    tag_list = f.readlines()


# 获取设备IP地址
def get_random_ip():
    RANDOM_IP_POOL = ['192.168.0.222/29']
    str_ip = RANDOM_IP_POOL[random.randint(0, len(RANDOM_IP_POOL) - 1)]
    str_ip_addr = str_ip.split('/')[0]
    str_ip_mask = str_ip.split('/')[1]
    ip_addr = struct.unpack('>I', socket.inet_aton(str_ip_addr))[0]
    mask = 0x0
    for i in range(31, 31 - int(str_ip_mask), -1):
        mask = mask | (1 << i)
    ip_addr_min = ip_addr & (mask & 0xffffffff)
    ip_addr_max = ip_addr | (~mask & 0xffffffff)
    return socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))


def handle_date(a1, a2, key):
    """处理时间方法"""
    start = time.mktime(a1)
    end = time.mktime(a2)
    t = random.randint(start, end)
    date_touple = time.localtime(t)
    date = None
    if key == "hms":
        date = time.strftime("%Y-%m-%dT%H:%M:%S", date_touple)
    elif key == "bir":
        date = time.strftime("%Y-%m-%d", date_touple)
    return date


# 向es插入数据
def insert_data():
    data_list = []
    for item in range(0, 1000):
        info = {
            "_index": "douyin_data",
            "_source": {
                # 用户id
                "author_user_id": random.randint(10000000000, 99999999999),
                # 抖音id
                "aweme_id": random.randint(6800000000000000000, 6899999999999999999),

                # 出生日期
                # "birthday": handle_date(a1=(1970, 1, 1, 0, 0, 0, 0, 0, 0), a2=(2012, 12, 31, 23, 0, 59, 0, 0, 0),
                #                         key="bir"),
                "birthday": handle_date(a1=(1970, 1, 1, 8, 0, 0, 3, 1, 0), a2=(2012, 12, 31, 23, 0, 59, 0, 0, 0),
                                        key="bir"),
                # 1970 1 1 8 0 0 3 1 0

                # 性别
                "gender": random.randint(0, 2),
                # 昵称
                "nickname": random.choice(nickname).strip(),
                # 归属地
                "region": random.choice(["AU", "CN", "CA", "CH", "IA", "JP", "US"]),
                # 用户描述
                "person_desc": random.choice(gexing).strip(),
                # 视频创建时间
                "video_create_time": handle_date(a1=(2020, 5, 1, 0, 0, 0, 0, 0, 0), a2=(2020, 8, 8, 23, 0, 59, 0, 0, 0),
                                                 key="hms"),
                # 设备IP
                "device_ip": get_random_ip(),
                # 抓取时间
                "crawl_time": handle_date(a1=(2020, 7, 1, 0, 0, 0, 0, 0, 0), a2=(2020, 8, 9, 23, 0, 59, 0, 0, 0),
                                          key="hms"),
                # 视频评论下载信息
                "statistics": {
                    "comment_count": random.randint(1, 99999),
                    "digg_count": random.randint(1, 99999),
                    "download_count": random.randint(1, 999),
                    "forward_count": random.randint(1, 99),
                    "lose_comment_count": 0,
                    "lose_count": 0,
                    "play_count": 0,
                    "share_count": random.randint(1, 99),
                    "whatsapp_share_count": 0
                },
                # 视频标签
                "tag": random.choice(tag_list).strip()
            }
        }
        # print(info)
        data_list.append(info)
    # 通过helpers插入数据
    helpers.bulk(es, data_list)


for i in range(50000):
    insert_data()
