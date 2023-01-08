import uiautomator2 as u2
import time
import adbutils
# python的多进程
import multiprocessing


class Douyin(object):
    # 在__init__方法里面连接设备
    def __init__(self, serial="4bf05af7"):
        self.d = u2.connect_usb(serial=serial)
        self.start_app()
        self.handle_watcher()
        self.size = self.get_windowsize()
        # 是用来获取一个初始时间
        self.t0 = time.perf_counter()

    def start_app(self):
        """启动app"""
        self.d.app_start(package_name="com.ss.android.ugc.aweme")

    def stop_app(self):
        """app退出逻辑"""
        # 先关闭监视器
        self.d.watcher.stop()
        self.d.app_stop("com.ss.android.ugc.aweme")
        self.d.app_clear("com.ss.android.ugc.aweme")

    def stop_time(self):
        """停止时间"""
        # 时间是秒
        if time.perf_counter() - self.t0 > 3600:
            return True

    def handle_watcher(self):
        """监视器"""
        # 通知权限
        self.d.watcher.when('//*[@resource-id="com.ss.android.ugc.aweme:id/a4r"]').click()
        # 发现滑动查看更多
        self.d.watcher.when('//*[@text="滑动查看更多"]').click()
        # 添加一个监控器
        self.d.watcher.when('//*[@text="快速进入TA的个人中心"]').click()
        # 专门给乐视手机使用的监控器
        self.d.watcher.when('//*[@text="允许"]').click()
        # 监控器写好之后，一定要记得启动
        self.d.watcher.start(interval=1)

    def get_windowsize(self):
        """获取窗口大小"""
        return self.d.window_size()

    def handle_swipe(self):
        # 滑动
        x1 = int(self.size[0] * 0.5)
        y1 = int(self.size[1] * 0.9)
        y2 = int(self.size[1] * 0.15)
        self.d.swipe(x1, y1, x1, y2)

    def swipe_douyin(self):
        """滑动抖音视频和点击视频发布者头像的操作"""
        # 来判断是否正常的进入到了视频页面
        # 网络情况不好也包含在内了
        if self.d(resourceId="com.ss.android.ugc.aweme:id/yy", text="我").exists(timeout=20):
            while True:
                # 到规定的时间停止循环
                if self.stop_time():
                    self.stop_app()
                    return
                # 查看是不是正常的发布者,看他的头向上有没有加号
                if self.d(resourceId="com.ss.android.ugc.aweme:id/u0").exists:
                    # 是正常的发布者，点击头像
                    self.d(resourceId="com.ss.android.ugc.aweme:id/tw").click()
                    # 返回
                    self.d(resourceId="com.ss.android.ugc.aweme:id/et").click()
                # 可能是广告
                else:
                    self.handle_swipe()

                if self.d(resourceId="com.ss.android.ugc.aweme:id/yy", text="我").exists and \
                        self.d(resourceId="com.ss.android.ugc.aweme:id/u0").exists:
                    # 正常的一个滑动
                    self.handle_swipe()


# subprocess adb devices
def get_devices():
    # 获取到当前操作系统中所连接的移动设备,serial num
    return [d.serial for d in adbutils.adb.device_list()]


# 操控设备的函数
def handle_device(serial):
    d = Douyin(serial)
    # 可以模拟滑动抖音短视频
    d.swipe_douyin()


def main():
    # 多进程启动u2去滑动移动设备,2台设备
    for i in range(len(get_devices())):
        serial = get_devices()[int(i)]
        p = multiprocessing.Process(target=handle_device, args=(serial,))
        # 启动进程
        p.start()


if __name__ == '__main__':
    # d = Douyin()
    # d.swipe_douyin()
    # print(get_devices())
    main()

