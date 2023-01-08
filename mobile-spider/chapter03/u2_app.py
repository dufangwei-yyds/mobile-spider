import uiautomator2 as u2

"""
u2自动化工具-操作app
"""

# 通过wifi来进行连接的
d = u2.connect()
# 通过app_install方法安装apk,url="xxx.apk"
# d.app_install(data="http://file.mukewang.com/apk/app/152/1670387331/imooc_8.3.3_10102001_android.apk")

# 启动app
# aapt dump badging /c/Users/lenovo/Downloads/imooc_8.3.3_10102001_android.apk
# d.app_start(package_name="cn.com.open.mooc")

# 获取当前前台运行的app的信息
# print(d.app_current())

# d.app_stop("cn.com.open.mooc")

# 获取app详细信息
# print(d.app_info(package_name="cn.com.open.mooc"))

# 清除app缓存
# 尤其是我们后面要进行的视频数据抓取,会产生一定的缓存
# d.app_clear("cn.com.open.mooc")

# 卸载app
# d.app_uninstall("cn.com.open.mooc")

# 获取当前移动设备中所有app信息
# print(d.app_list())

# 获取所有正在运行的app的列表
# print(d.app_list_running())

# 停止所有app
# d.app_stop_all()

# 卸载所有app,第三方app,u2项目包不在之内
# d.app_uninstall_all()
