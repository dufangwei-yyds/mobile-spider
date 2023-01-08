# -*- coding: utf-8 -*-
# @Time    : 2023/1/4 12:05
# @Author  : bruce
# @Email   : d920130d2@163.com
# @File    : handle_appium_docker.py
# @Software: PyCharm

import multiprocessing
import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


# 获取尺寸的函数
def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


def handle_appium(info):
    cap = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": info['device'],
        "udid": info['device'],
        "appPackage": info['appPackage'],
        "appActivity": info['appActivity'],
        "noReset": True,
        "unicodekeyboard": True,
        "resetkeyboard": True
    }

    # driver = webdriver.Remote('http://192.168.99.100:'+str(port)+'/wd/hub', cap)
    driver = webdriver.Remote('http://192.168.0.109:' + str(info['port']) + '/wd/hub', cap)
    l = get_size(driver)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.15)
    y2 = int(l[1] * 0.9)

    # 抖音
    if info['appPackage'] == 'com.ss.android.ugc.aweme':
        if WebDriverWait(driver, 60).until(
                lambda x: x.find_element_by_xpath("//android.widget.TextView[@text='首页']")):
            while True:
                # 初始鼠标位置，从哪开始，结束时鼠标位置，到哪结束
                driver.swipe(x1, y1, x1, y2)
                time.sleep(3)
    # 快手
    elif info['appPackage'] == 'com.smile.gifmaker':
        if WebDriverWait(driver, 60).until(lambda x: x.find_element_by_xpath(
                "//android.widget.ImageView[@resource-id='com.smile.gifmaker:id/logo']")):
            while True:
                # 初始鼠标位置，从哪开始，结束时鼠标位置，到哪结束
                driver.swipe(x1, y1, x1, y2)
                time.sleep(3)
    # 今日头条
    elif info['appPackage'] == 'com.ss.android.article.news':
        if WebDriverWait(driver, 60).until(
                lambda x: x.find_element_by_xpath("//android.view.View[@content-desc='推荐']")):
            while True:
                # 初始鼠标位置，从哪开始，结束时鼠标位置，到哪结束
                driver.swipe(x1, y1, x1, y2)
                time.sleep(3)


if __name__ == '__main__':
    m_list = []
    # 定义两台虚拟设备
    devices_list = [
        {
            "device": "192.168.0.102:5555",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
            "port": 4723,
            "key": '抖音'
        },
        {
            "device": "192.168.0.104:5555",
            "appPackage": "com.smile.gifmaker",
            "appActivity": "com.yxcorp.gifshow.HomeActivity",
            "port": 4724,
            "key": '快手'
        },
        {
            "device": "192.168.0.106:5555",
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activity.SplashBadgeActivity",
            "port": 4725,
            "key": '今日头条'
        },
    ]
    for device in (devices_list):
        m_list.append(multiprocessing.Process(target=handle_appium, args=(device,)))

    for m1 in m_list:
        m1.start()

    for m2 in m_list:
        m2.join()
