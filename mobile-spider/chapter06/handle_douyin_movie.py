# -*- coding: utf-8 -*-
# @Time    : 2023/1/3 18:10
# @Author  : bruce
# @Email   : d920130d2@163.com
# @File    : handle_douyin_movie.py
# @Software: PyCharm

import json
import time
# 导入了web自动化包
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import re


class HandleDouyinMovie(object):
    def __init__(self, share_id):
        # 分享ID
        self.share_id = share_id
        self.share_url = 'https://www.douyin.com/share/user/' + self.share_id

        self.header = {
            # "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
        }

    def handle_dytk_tac(self):
        '''
        获取dytk和tac
        :return:
        '''
        # 创建了dytk，tac的正则表达式
        dytk_search = re.compile(r"dytk: '(.*?)'")
        tac_search = re.compile(r"<script>tac=(.*?)</script>")

        # 请求个人分享页,获取dytk和tac
        response = requests.get(url=self.share_url, headers=self.header)

        # dytk,tac正则的调用,以及处理
        self.dytk = re.search(dytk_search, response.text).group(1)

        # 把他封装成js的格式
        self.tac = "var tac=" + re.search(tac_search, response.text).group(1) + ";"

    def handle_html(self):
        # html页面的编写，合成
        with open('html_head.txt', 'r') as f1:
            f1_read = f1.read()

        with open('html_foot.txt', 'r') as f2:
            f2_read = f2.read().replace("&&&", self.share_id)

        # 合成
        with open('test.html', 'w') as f_w:
            f_w.write(f1_read + '\n' + self.tac + '\n' + f2_read)

    def handle_webdriver(self):
        '''
        获取signature值
        :return:
        '''
        # 进行了自动化获取signature
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        douyin_driver = webdriver.Chrome(chrome_options=chrome_options)
        # 需替换成你自己本地路径
        # douyin_driver.get("file://C:\\study\\imooc\\python-appium-app\\douyin\\crawl_douyin_movie\\test.html")
        douyin_driver.get("file:///Users/bruce/workspace/mobile-spider/chapter06/test.html")
        self.signature = douyin_driver.title
        # 浏览器的退出
        douyin_driver.quit()

    def handle_movie(self):
        # 请求JSON的URL
        movie_url = "https://www.douyin.com/aweme/v1/aweme/post/?user_id=" + self.share_id + "&count=21&max_cursor=0&aid=1128&_signature=" + self.signature + "&dytk=" + self.dytk

        # 使用循环来访问请求视频json数据的URL
        while True:
            movie_response = requests.get(url=movie_url, headers=self.header)
            if json.loads(movie_response.text)['aweme_list'] == []:
                time.sleep(1)
                continue
            else:
                # 进行json.loads
                for item in json.loads(movie_response.text)['aweme_list']:
                    video_url = item['video']['play_addr']['url_list'][0]
                    video_response = requests.get(url=video_url, headers=self.header)
                    # 需要使用wb的方法
                    with open('douyin' + str(time.time()) + ".mp4", 'wb') as v:
                        # 不能用使用response.text，必须要使用content
                        v.write(video_response.content)
                print(movie_url)
                break


if __name__ == '__main__':
    douyin = HandleDouyinMovie('88445518961')
    douyin.handle_dytk_tac()
    douyin.handle_html()
    douyin.handle_webdriver()
    douyin.handle_movie()
