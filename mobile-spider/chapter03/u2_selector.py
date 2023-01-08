# -*- coding: utf-8 -*-
# @Time     : 2022/12/17 16:05
# @Author   : bruce
# @Email    : d920130d2@163.com
# @File     : u2_selector.py
# @Software : PyCharm

import uiautomator2 as u2

d = u2.connect_usb("127.0.0.1:62001")

# 可以通过aapt工具来获取包名,是获取的apk的包名,设置这个app的apk
# 包名通过weditor来获取,package:com.android.settings
# 启动设置app
d.app_start(package_name="com.android.settings")

# 全文本匹配,点击
# d(text="更多").click()

# 文本包含
# d(textContains="屏幕").click()

# 传入正则表达式
# d(textMatches=".{2}屏幕.{2}").click()

# 文本起始位置
# d(textStartsWith="设置").click()

# 通过className来获取控件定位时,需要注意层级关系
# d(className="android.widget.TextView")[11].click()
# d(className="android.widget.TextView", instance=10).click()
# d(classNameMatches="android\.widget\.\w{8}", text="蓝牙").click()

# 通过resourceId来定位控件
# 可以选择多个控件,默认选择第一个
# d(resourceId="android:id/title")[5].click()
# 通过实例来进行查找,值和索引是一样的
# d(resourceId="android:id/title", instance=5).click()
# 通过多个条件进行限定
# d(resourceId="android:id/title", text="蓝牙").click()
# 通过正则表达式的方法来获取资源Id,定位控件
# d(resourceIdMatches="android:id\/\w{5}", text="蓝牙").click()

# 链式定位方式
# d(className="android.widget.LinearLayout").child(text="蓝牙").click()
# 完全的链式定位方法,代码非常冗长,不建议使用
# d(className="android.widget.LinearLayout").child(resourceId="android:id/title")[5].click()
# d(className="android.widget.LinearLayout").child_by_text("蓝牙", resourceId="android:id/title").click()
# 这种方法多此一举,不建议使用
# d(resourceId="android:id/title").sibling(resourceId="android:id/title", instance=4).click()

# 这里可以通过坐标点来进行控件的定位
# d.click(156, 829)

# 控件不存在,我们该怎么办
# click找不到控件就抛异常
# d(text="蓝牙1").click(timeout=5)
# click_exists找不到控件就返回
# d(text="蓝牙1").click_exists(timeout=5)
# 在操作之前,通过exists属性判断控件是否存在
# print(d(text="蓝牙1").exists)
# print(d(text="蓝牙1").exists(timeout=5))
# print(d(resourceId="com.android.settings:id/dashboard_container").child(resourceId="android:id/title").count)
for view in d(resourceId="com.android.settings:id/dashboard_container").child(resourceId="android:id/title"):
    print(view.info)







