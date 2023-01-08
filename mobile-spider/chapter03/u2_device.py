# -*- coding: utf-8 -*-
# @Time    : 2022/12/16 21:14
# @Author  : bruce
# @Email   : d920130d2@163.com
# @File    : test.py
# @Software: PyCharm

import uiautomator2 as u2
import time

"""
u2自动化工具-操作设备
"""

# # 通过wifi来进行连接的
d = u2.connect()

# # 查看设备信息
# # print(d.device_info)

# print(d.service("uiautomator").running())
# # 通过start方法启动uiautomator服务
# d.service("uiautomator").start()
# d.service("uiautomator").stop()
# time.sleep(2)
# print(d.service("uiautomator").running())

# 查看atx-agent运行状态,如果atx-agent停止了,我们可以通过connect来唤醒atx-agent
print(d.agent_alive)

# 查看设备信息
print(d.device_info)

# 查看设备的分辨率
print(d.window_size())

# 查看获取到的wifi地址
# 注意: 模拟器获取和真机不同,模拟器获取的是错误的
print(d.wlan_ip)
