# -*- coding: utf-8 -*-
# @Time     : 2022/12/18 9:43
# @Author   : bruce
# @Email    : d920130d2@163.com
# @File     : u2_xpath.py
# @Software : PyCharm
import uiautomator2 as u2

d = u2.connect_usb("127.0.0.1:62001")
with open("phone.file", 'w', encoding='utf-8') as f:
    # 通过这个方法来获取到控件的源代码文件
    f.write(d.dump_hierarchy())


