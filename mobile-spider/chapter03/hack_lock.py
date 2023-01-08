# -*- coding: utf-8 -*-
# @Time     : 2022/12/17 21:12
# @Author   : bruce
# @Email    : d920130d2@163.com
# @File     : hack_lock.py
# @Software : PyCharm

import uiautomator2 as u2

d = u2.connect_usb("127.0.0.1:62001")
# 滑动解锁操作
# 息屏
# d.screen_off()
# 点亮屏幕
# d.screen_on()
# 解锁
# d.unlock()
# 获取屏幕状态
# print(d.info.get("screenOn"))
# home键
# d.press("home")
# 返回键
# d.press("back")
# 左右滑屏
# d.swipe_ext("left")
# d.swipe_ext("right")

# 滑动解锁
# swipe_points
# 息屏
d.screen_off()
# home键
d.press("home")
# 先解锁调出九宫格界面
d.unlock()
# (321, 1282)
# (537, 1282)
# (757, 1286)
# (541, 1501)
# (321, 1720)
# (537, 1720)
# (752, 1712)
d.swipe_points(points=[
    (321, 1282),
    (537, 1282),
    (757, 1286),
    (541, 1501),
    (321, 1720),
    (537, 1720),
    (752, 1712)
], duration=0.2)

# d.screen_off()
