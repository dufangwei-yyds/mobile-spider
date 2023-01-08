# -*- coding: utf-8 -*-
# @Time     : 2022/12/23 15:57
# @Author   : bruce
# @Email    : d920130d2@163.com
# @File     : handle_proxy.py
# @Software : PyCharm
import requests

# 27.221.154.41
url = 'http://ip.hahado.cn/ip'
proxy = {'http': 'http://H211EATS905745KC:F8FFBC929EB7D5A7@http.cla.abuyun.com:9030'}
response = requests.get(url=url, proxies=proxy)
print(response.text)

