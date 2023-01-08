# -*- coding: utf-8 -*-
# @Time    : 2022/12/18 17:01
# @Author  : bruce
# @Email   : d920130d2@163.com
# @File    : u2_kaoyanbang.py
# @Software: PyCharm

import time
import uiautomator2 as u2


class HandleKaoyanbang(object):
    def __init__(self, serial="127.0.0.1:62001"):
        # 当前是通过usb方法连接移动设备的
        self.d = u2.connect_usb(serial)
        self.size = self.get_windowsize()
        self.handle_watcher()

    def handle_watcher(self):
        """定义一个监控器"""
        # 用户隐私协议
        self.d.watcher.when('//*[@resource-id="com.tal.kaoyan:id/tip_commit"]').click()
        # 广告
        self.d.watcher.when('//*[@resource-id="com.tal.kaoyan:id/tv_skip"]').click()
        self.d.watcher.when('//*[@resource-id="com.tal.kaoyan:id/guid_image"]').click()
        # 监控器写好之后,要通过start方法来启动
        self.d.watcher.start()

    def get_windowsize(self):
        """获取手机屏幕的大小"""
        return self.d.window_size()

    def close_app(self):
        # 监控器关闭
        self.d.watcher.stop()
        # 退出考研帮app
        self.d.app_stop("com.tal.kaoyan")
        # 清理缓存
        self.d.app_clear("com.tal.kaoyan")

    def handle_kaoyanbang_app(self):
        """启动考研帮app,并实现自动化操作"""
        # aapt
        # weditor
        self.d.app_start(package_name="com.tal.kaoyan")
        # 在点击之前需要判断是否有这个控件
        self.d(text="密码登录").click_exists(timeout=10)
        # 通过找到相关控件之后,文本控件,set_text输入文字
        self.d(resourceId="com.tal.kaoyan:id/login_email_edittext").set_text("13256364859")
        # 输入密码
        self.d(resourceId="com.tal.kaoyan:id/login_password_edittext").set_text("dfw920130")
        # self.d(resourceId="com.tal.kaoyan:id/login_login_btn").click()
        self.d(text="登录").click()

        # 在10秒如果这个界面启动了
        # if self.d.wait_activity("com.tal.kaoyan.ui.activity.HomeTabActivity", timeout=10):
        #     self.d(text="研讯").click_exists(timeout=10)
        #
        #     # 获取到屏幕的中心点,x轴
        #     # 再获取到y轴远方点,获取到y轴近点
        #     x1 = int(self.size[0] * 0.5)
        #     y1 = int(self.size[1] * 0.9)
        #     y2 = int(self.size[1] * 0.15)
        #     while True:
        #         # get toast,是安卓系统的一个信息提示操作
        #         if self.d.toast.get_message(0) == "内容已经全部加载完了":
        #             self.close_app()
        #             return
        #             # 开始滑动研讯
        #         self.d.swipe(x1, y1, x1, y2)

        # 在10秒如果这个界面启动了
        if self.d.wait_activity("com.tal.kaoyan.ui.activity.HomeTabActivity", timeout=10):
            self.d(text="社区").click_exists(timeout=10)

            # 获取到屏幕的中心点,x轴
            # 再获取到y轴远方点,获取到y轴近点
            x1 = int(self.size[0] * 0.5)
            y1 = int(self.size[1] * 0.9)
            y2 = int(self.size[1] * 0.15)
            while True:
                # get toast,是安卓系统的一个信息提示操作
                if self.d.toast.get_message(0) == "没有更多了":
                    time.sleep(15)
                    self.close_app()
                    return
                    # 开始滑动社区信息
                self.d.swipe(x1, y1, x1, y2)


if __name__ == '__main__':
    k = HandleKaoyanbang()
    k.handle_kaoyanbang_app()
