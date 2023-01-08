# -*- coding: utf-8 -*-
# @Time    : 2022/12/16 21:14
# @Author  : bruce
# @Email   : d920130d2@163.com
# @File    : u2_test.py
# @Software: PyCharm

import uiautomator2 as u2
import time

# 通过手机wifi来进行连接: 手机的ip地址
d = u2.connect()
# d = u2.connect_wifi("192.168.0.103")

# 通过手机usb来进行连接: 手机的序列号
# d = u2.connect_usb("127.0.0.1:62001")

# 通过adb_wifi即adb_tcpip模式
# d = u2.connect_adb_wifi("192.168.0.106:5555")

# 获取设备信息
print(d.info)

# 获取详细的设备信息
print(d.device_info)

# 启动手机上的app, 通过aapt工具来获取包名
d.app_start("com.ss.android.ugc.aweme")

# 运行5秒
time.sleep(10)

# 停止抖音app
d.app_stop("com.ss.android.ugc.aweme")








