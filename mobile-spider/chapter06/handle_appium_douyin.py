# -*- coding: utf-8 -*-
# @Time    : 2023/1/3 16:18
# @Author  : bruce
# @Email   : d920130d2@163.com
# @File    : handle_appium_douyin.py
# @Software: PyCharm

# appium
import time
from appium import webdriver
# 用来等待元素控件
from selenium.webdriver.support.ui import WebDriverWait
import multiprocessing

"""
  多设备抓取抖音粉丝数据
"""

# 获取尺寸的函数
def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


def handle_douyin(driver):
    while True:
        # 定位的搜索框
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
                "//android.widget.ImageView[@resource-id='com.ss.android.ugc.aweme:id/a5p']")):
            driver.find_element_by_xpath(
                "//android.widget.ImageView[@resource-id='com.ss.android.ugc.aweme:id/a5p']").click()
            driver.find_element_by_xpath(
                "//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a5q']").send_keys("1309040553")

        # 搜索
        driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/a5s']").click()
        # 点击用户标签
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name("android.widget.TextView")):
            driver.tap([(288, 102), (432, 162)])
            # driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.TextView[3]").click()

        # 查看是否有关注标签
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
                "//android.support.v7.widget.RecyclerView[@resource-id='com.ss.android.ugc.aweme:id/kl']/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]")):
            driver.find_element_by_xpath(
                "//android.support.v7.widget.RecyclerView[@resource-id='com.ss.android.ugc.aweme:id/kl']/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        # 查看是否有粉丝
        if WebDriverWait(driver, 10).until(
                lambda x: x.find_element_by_xpath("//android.widget.TextView[@text='粉丝']")):
            driver.find_element_by_xpath("//android.widget.TextView[@text='粉丝']").click()

        time.sleep(1)

        l = get_size(driver)
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.9)
        y2 = int(l[1] * 0.15)

        while True:
            # 粉丝数据滑动到最下面
            if '没有更多了' in driver.page_source:
                break
            elif 'TA还没有粉丝' in driver.page_source:
                break
            else:
                # 初始鼠标位置，从哪开始，结束时鼠标位置，到哪结束
                driver.swipe(x1, y1, x1, y2)
                time.sleep(0.1)

        driver.find_element_by_id("com.ss.android.ugc.aweme:id/jk").click()
        driver.find_element_by_id("com.ss.android.ugc.aweme:id/jk").click()
        driver.find_element_by_xpath(
            "//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a5q']").clear()


def handle_appium(device, port):
    cap = {
        "platformName": "Android",
        "platformVersion": "7.1.2",
        "deviceName": device,
        "udid": device,
        "appPackage": "com.ss.android.ugc.aweme",
        "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
        "noReset": True,
        "unicodekeyboard": True,
        "resetkeyboard": True
    }

    driver = webdriver.Remote('http://localhost:' + str(port) + '/wd/hub', cap)
    # 点击搜索
    try:
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("com.ss.android.ugc.aweme:id/aci")):
            driver.find_element_by_id("com.ss.android.ugc.aweme:id/aci").click()
    except:
        pass

    handle_douyin(driver)


if __name__ == '__main__':
    m_list = []
    # 定义两台虚拟设备
    devices_list = ['127.0.0.1:62001', '127.0.0.1:62025']
    for device in range(len(devices_list)):
        port = 4723 + 2 * device
        m_list.append(multiprocessing.Process(target=handle_appium, args=(devices_list[device], port,)))

    for m1 in m_list:
        m1.start()

    for m2 in m_list:
        m2.join()
