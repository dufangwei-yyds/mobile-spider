##### 项目介绍
1. 项目概述

   ```markdown
   数据抓取,数据存储,数据可视化完整实战流程
   ```

2. 项目目标

   ```markdown
   学会uiautomator2对移动设备进行操控
   学会抓包利器使用
   学会利用python编写移动端自动化抓取脚本
   学会通过atxserver2监控多台移动设备
   学会将数据存储到es
   学会通过kibana进行大数据可视化分析展示
   ```

3. 爬取数据后,能做什么

   ```markdown
   数据分析
   用户画像
   统计系统
   商业竞争

   技能提升
   面试必备
   ```

4. app数据好抓吗?

   ```markdown
   简单: app里的数据比web端更容易抓取,反爬虫也没那么强,大部分也都是http/https协议,
   返回的数据类型大多数为json
   困难: 
   可能需要适当的反编译,分析出加密算法并抓取到信息;
   可能加固,需要脱壳,然后反编译,分析出加密算法并抓取到信息;
   需要破解通过各式各样的签名,证书,设备绑定等方法,找到隐藏加密算法
   ```

5. 爬虫工程师技术储备

   ```markdown
   python爬虫开发经验
   java开发基础
   android开发基础
   app逆向
   app脱壳
   破解加密算法
   ```

6. 项目内容

   ```markdown
   # 项目内容V1
   python <=appium=> android
   
   python 夜神模拟器/genymotion fiddler/mitmproxy/Packet Capture appium docker
   豆果美食 抖音 快手 今日头条 mongoDB
                                                        docker appium <-http通讯-> 抖音
   mongodb =pymongodb=> appium-python-client =http通讯=> docker appium <-http通讯-> 快手
                                                        docker appium <-http通讯-> 今日头条                                         
   
   # 项目内容V2
   uiautomator2
   weditor fiddler mitmproxy ...
   抖音 atxserver2 es  kibana
   
   kibana      atxserver2多设备监控平台-http通信-> Atx-agent(移动设备) -http通信-> 新闻信息
   es            手机屏幕监控          -http通信-> Atx-agent(移动设备) -http通信->短视频信息
                                     -http通信-> Atx-agent(移动设备) -http通信->租房信息
   ```
   
##### u2自动化抓取开发环境搭建
1. 夜神模拟器安装、介绍、设置、安装app

   ```markdown
   # 常见安卓开发模拟器对比
   模拟器名称        支持的操作系统   支持的虚拟机 运行速度  安装apk方式 支持机型 调试难易程度
   google官方的avd   Win/Linux      QEMU       慢      adb       多       复杂
   genumotion       Win/Wac/Winux  VirtualBox 一般    adb/拖拽   少       一般
   夜神模拟器         Win            VirtualBox 快     adb/拖拽    少       简单
   
   # 夜深安卓模拟器
   夜深安卓模拟器(夜神模拟器),是全新一代的安卓模拟器,与传统安卓模拟器相比,基于android4.4.2,
   兼容X68/AMD,在性能、稳定性、兼容性等方面有着巨大优势
   https://www.yeshen.com
   多开 
   设置: root  手机型号  网络设置
   安装app: adb、拖拽
   豆果美食apk 抖音apk 考研帮apk 慕课网apk
   ```

2. appium移动端自动化测试工具安装及介绍

   ```markdown
   # appium移动端自动化测试工具介绍
   appium是一个自动化测试开源工具,支持ios平台和android平台上的原生应用,web应用和混合应用
   appium是一个跨平台的工具: 它允许测试人员在不同的平台(ios,android)使用同一套API来写自动化
   测试脚本,这样大大增加了ios和android测试套件间代码的复用性
   
   # selenium
   appium类库封装标准Selenium客户端类库
   appium客户端类库实现Mobile JSON Wire Protocol、W3C
   appium服务端定义了官方协议的扩展,为appium用户提供方便的接口来执行各种设备操作
   
   # appium特点
   多平台
   appium选择了client/server的设计模式
   appium扩展了WebDriver的协议
   多语言
   
   # appium工作原理
   Appium-client =>  Appium-Server       => 移动设备
   Java-client      appium.dmg              Android模拟器
   Python-client    appiumForWindow.zip     Android真机
   Ruby-cli                                 iOS真机
   ...
   
   # appium下载安装
   appium-1.9.0 (服务端)
   https://github.com/appium/appium-desktop/releases?page=1
   0.0.0.0 4723  => start server v1.9.0
   🔍 => start session
   
   通过node.js安装-不推荐: 
   npm install -g appium
   win10开发者模式
   .net3.5
   windows-10-sdk工具
   WindowsApplicationDriver
   npm install --global --production windows-build-tools
   https://testerhome.com/topics/12988
   
   # appium
   appium是一个开源测试自动化框架,可用于原生,混合和移动web应用程序测试.它使用WebDriver协议驱动iOS,
   Android应用程序 
   
   # appium架构
   # appium-inspector
   Configuration配置环境变量: ANDROID_HOME和JAVA_HOME
   adb connect 127.0.0.1:62001
   Remote Path: /wd/hub
   Automatic Server - Desired Capabilities
   platformName text Android
   platformVersion text  7.1.2
   deviceName text 127.0.0.1:62001
   appPackage text com.tal.kaoyan
   appActivity text com.tal.kaoyan.ui.activity.SplashActivity
   noReset true
   save as kaoyanbang2
   Saved Capability Sets-选中kaoyanbang2-start session
   点击👀 点击Send Keys 输入用户名
   点击Send Keys 输入密码
   点击Tap
   点击刷新按钮
   
   aapt dump badging apk文件名
   aapt dump badging apk文件名 | find "launchable-activity"
   adb shell
   logcat | grep cmp=
   点击考研帮
   
   # Desired Capability
   Desired Capability的功能是配置Appium会话,他们告诉Appium服务器想要自动化的平台和应用程序
   
   # appium实战
   pip3 install Appium-Python-Client
   kaoyanbang_test.py
   ```
   ![](/Users/bruce/Documents/笔记截图/appium架构.png)

3. Android开发工具环境安装

   ```markdown
   # 什么是SDK
   SDK: software development kit 软件开发工具包.是软件开发工程师用于为特定的软件包、软件框架
   硬件平台、操作系统等建立应用软件的开发工具的集合
   Android SDK指的是Android专属的软件开发工具包
   
   # 安装SDK前准备工作
   安装JDK并配置环境变量
   
   # SDK下载安装并配置环境变量
   http://tools.android-studio.org/index.php/sdk
   cd /Users/bruce/android-sdk-macosx/tools
   android -v
   SDK Manager
   Tools => Options => Proxy Settings mirrors.neusoft.edu.cn 80
   => Others Force...打✅
   Packages => Reload
   Tools: Android SDK Tools,Android SDK Platform-tools,Android SDK Build-tools
   Extras: 全部☑️
   Install 23 packages
   
   # Android开发工具使用
   adb 5037
   adb version
   adb devices
   adb -s 127.0.0.1:62001  shell
   # 有root权限
   $ 没有root权限
   adb -s 设备  install apk安装包路径
   adb -s 设备 shell
   cd /data/app
   adb -s 设备  uninstall 包名
   adb connect 127.0.0.1:62001
   adb shell pm list package
   adb push 本地文件路径  夜神模拟器路径
   adb pull 夜神模拟器路径 本地文件路径
   adb shell screencap 夜神模拟器路径
   
   uiautomator
   Android4.3发布的测试工具
   uiautomator是用来做UI测试的,即普通的手工测试,点击每个控件元素看输出的结果是否符合预期
   uiautomator: 一个测试的Java库,包含了创建UI测试的各种API和执行自动化测试的引擎
   uiautomatorviewer: 一个图形界面工具来扫描和分析应用的UI控件,存在在tools目录
   
   uiautomatorviewer升级版
   相关文件替换: 
   cd /d/SDK/tools/lib
   uiautomatorviewer.jar 
   lib中所有文件 
   cd /d/SDK/tools
   com、image中所有文件
   
   uiautomatorviewer连接设备使用
   启动夜神模拟器
   cd /d/SDK/platform-tools
   ./adb.exe connect 127.0.0.1:62001
   cd /d/SDK/tools
   uiautomatorviewer.bat
   ```

4. u2自动化抓取工具概述

   ```markdown
   # UiAutomator
   UiAutomator是Google提供的用来做安卓自动化测试的一个Java库
   基于Accessibility服务

   辅助功能(AccessibilityService)是Android系统提供给的一种服务,本身是继承Service类的,这个服务提供了增强的用户界面,
   旨在帮助残障人士或者可能无法与设备充分交互的人们
   我们可以借助AccessibilityService,可以实现对页面的监听及模拟点击控制等自动化操作

   缺点:
   测试脚本只能使用Java语言
   测试脚本要打包成jar或apk包上传到设备上才能运行

   # UiAutomator2
   希望能够用Python编写代码逻辑
   希望能够在电脑上运行的时候就控制手机
   在手机上运行了一个http rpc服务,将UiAutomator中的功能集成进来,然后再将这些http接口封装成Python库

   优点:
   环境搭建便捷
   UI控件识别有专业工具(webitor),可视化好
   UI自动化编写采用python,学习成本低
   UI自动化脚本运行稳定
   文档是中文的

   https://github.com/openatx/uiautomator2

   uiautomator2支持的环境: android版本4.4+ python3.6
   
   课程开发环境:
   开发环境 win10
   运行环境 ubuntu18.04
   vmware workstation 15 pro
   securecrt version 7.0.0
   pycharm
   安卓模拟器 夜神模拟器V6.6.0
   python3.6.9
   ```

5. u2通信流程概述

   ```markdown
   # uiautomator2
   python      wifi/usb/adb wifi         移动设备 uiautomator-server atx-agent minicap minitouch
   PC端

   运行脚本,并向系统设备发送http请求          移动设备上运行封装了uiautomator2的http服务,解析收到的请求,
                                         并转化成uiautomator2的代码

   # uiautomator
   在移动设备上安装atx-agent(守护进程),随后atx-agent启动uiautomator2服务(默认7912端口)进行监听
   在pc上编写测试脚本并执行(相当于发送http请求到移动设备的server端)
   移动设备通过wifi或usb收到pc上发来的http请求,执行指定的操作

   u2_post.py
   adb devices
   adb shell
   ps | grep atx
   busybox netstat -pt | grep 7956
   ```

6. u2自动化抓取开发环境搭建

   ```markdown
   # VMware WorkStation导入虚拟机,安装SecureCrt连接服务器
   VMware WorkStation导入ubuntu虚拟机文件 (4g 2 20g | user1 imooc-python)
   netstat -an | grep 22
   ifconfig   
   
   # 配置pycharm远程开发环境
   win10编写代码,代码运行在ubuntu,配置pycharm连接ubuntu,可以在win10中使用ubuntu的python环境

   1) 服务器配置Python虚拟环境
   pip3 uninstall virtualenv
   pip3 install virtualenv==20.0.23 -i https://pypi.douban.com/simple
   mkdir u2_project
   python3 -m virtualenv venv
   pip3 freeze
   source venv/bin/activate
   
   2) pycharm
   Python Interpreter => Add Interpreter => On SSH 
   => Connecting to SSH server(New-Host/Port/Username) 
   => Password 
   => Location(服务器工作目录)|Base Interpreter(服务器Python虚拟环境)|Sync folders
   
   # android调试桥(adb)
   命令行窗口,用于通过电脑端与模拟器或设备之间的交互
   
   adb client: 命令行程序"adb"用于从shell或脚本中运行adb命令
   adb server: ADB Server是运行在pc上的一个后台程序
   adbd: 程序"adbd"作为一个后台进程在Android设备或模拟器系统中运行
   
   adb能够用来做什么:
   安装卸载apk、移动设备和pc之间拷贝文件、查看设备上安装的应用信息、文件管理、按键操作...
   
   常见adb应用: 各种刷机工具、各种手机root工具
   
   # Mac/Win10系统安装使用adb(安装夜神模拟器即可使用)
   1) 安装夜神模拟器
   2) Mac配置系统环境变量
   export NOXAPPPLAYER_HOME=/Applications/NoxAppPlayer.app/Contents
   export PATH=$PATH:$NOXAPPPLAYER_HOME/MacOS
   3) Win10配置系统环境变量
   NOX_HOME=D:\Program Files\Nox
   Path=D:\Program Files\Nox\bin
   4) adb基本使用(通过豌豆荚提前安装相关apk文件)
   adb devices
   adb kill-server
   adb install apk安装包路径
   adb install apk安装包路径
   adb shell pm list packages
   adb uninstall com.tal.kaoyan
   adb tcpip 5555
   adb connect 192.168.0.103
   adb shell
   
   5) 注意事项
   不建议使用的手机品牌: 华为系列、荣耀系列
   建议使用的手机品牌: 小米、oppo等
   
   # Ubuntu系统安装使用adb
   1) 下载安装platform-tools-latest-linux.zip、adb、fastboot
   wget https://dl.google.com/android/repository/platform-tools-latest-linux.zip
   sudo wget -O 
   /usr/local/sbin/adb https://raw.githubusercontent.com/NicolasBernaerts/ubuntu-scripts
   /master/android/adb
   sudo wget -O 
   /usr/local/sbin/fastboot https://raw.githubusercontent.com/NicolasBernaerts/ubuntu-scripts
   /master/android/fastboot
   
   sudo cp adb /usr/local/sbin/
   sudo cp fastboot /usr/local/sbin/
   sudo unzip platform-tools_r29.0.6-linux.zip /usr/local/sbin/
   sudo chmod +x /usr/local/sbin/platform-tools/adb /usr/local/sbin/adb 
   sudo chmod +x /usr/local/sbin/platform-tools/fastboot /usr/local/sbin/fastboot
   
   sudo vim /etc/profile
   export PATH=/usr/local/sbin:$PATH
   source /etc/profile
   
   2) win10系统
   adb tcpip 5555
   adb connect 192.168.0.103 (服务器ip地址)
   夜神模拟器-手机与网络-开启网络桥接连接
   
   安装、卸载apk:
   adb install apk安装包路径
   adb shell pm list packages
   adb uninstall com.tal.kaoyan
   ```

7. u2自动化抓取开发环境知识点回顾

   ```markdown
   VMware
   SecureCrt
   
   virtualenv
   pycharm
   
   adb(win: 夜神模拟器 / ubuntu: adb、fastfoot、platform-tools-latest-linux.zip)
   安装apk,卸载adb
   ```

8. 如何连接真实移动设备并安装apk

   ```markdown
   # win10系统 + 向日葵远程工具
   1) adb(夜神模拟器已经安装并配置系统环境变量)可以正常使用
   2) 将android手机通过usb线与win10连接(管理-设备管理器(查看驱动是否安装,未安装会显示!))
   3) 手机开启开发者选项和USB调试(USB连接过可以先操作"撤销USB调试授权",再开启开发者选项和USB调试)
   4) 查看设备列表: adb devices
   
   # 安装apk,卸载adb
   adb install apk安装包路径 -s (指定设备)
   adb install  apk安装包路径
   adb shell pm list packages
   adb uninstall com.tal.kaoyan(apk的包名)
   ```

9. 安装u2和u2项目初始化

   ```markdown
   pip install uiautomator2 -i https://pypi.douban.com/simple
   第一次会在夜神模拟器安装atx-agent: python -m uiautomator2 init   
   
   uiautomator-server: 谷歌原生的uiautomator
   atx-agent: uiautomator的守护进程. atx-agent增强远程控制的功能,依赖minicap和minitouch这两个工具
   
   安装文件所在目录: .uiautomator2/cache/
   ```

10. u2连接移动设备的三种方式

   ```markdown
   # 打开夜神模拟器
   # u2控制移动设备
   https://github.com/openatx/uiautomator2/issues/365
   通过wifi:     通过usb连接手机 手机ip地址
   通过usb:      手机序列号
   通过adb wifi: 192.168.0.103:5555
   adp tcpip 5555  
   adb connect 192.168.0.103
   
   u2_test.py
   
   获取apk包名: aapt dump badging /c/Users/lenovo/Desktop/douyin10.0.apk
   ```

##### u2定位元素方法
1. u2自动化工具基本操作-操作设备

   ```markdown
   # 操作atx-agent
   adb devices
   adb shell
   chmod 755 /data/local/tmp/atx-agent
   data/local/tmp/atx-agent version 
   /data/local/tmp/atx-agent server -d 
   /data/local/tmp/atx-agent server -d --stop
   
   # 操作设备
   u2_device.py
   ```

2. u2自动化工具基本操作-操作app

   ```markdown
   u2_app.py
   ```

3. Activity和控件

   ```markdown
   # Activity
   Activity是用户和应用程序交互的窗口,一个Activity相当于我们实际中的一个网页
   
   # 控件
   TextView 显示文字
   EditText 输入框,可编辑
   ImageView 显示图片
   Button 按钮
   CheckBox 复选框
   RadioButton 单选按钮
   https://blog.csdn.net/weixin_38423829/article/details/80566203
   ```

4. weditor安装启动和介绍

   ```markdown
   # weditor安装
   pip3 install weditor -i https://pypi.tuna.tsinghua.edu.cn/simple/
   
   # weditor启动
   adb devices
   weditor
   http://localhost:17310/
   
   # weditor基本使用
   移动设备界面选取区域
   控件属性区域
   代码展示区域
   层级关系及运行结果展示区域
   
   Android 127.0.0.1:62001  Connect  Dump Hierararchy
   ```

5. Android的布局与控件定位 

   ```markdown
   # 定位工具
   UiSelector: 代表一种搜索标准,可以在当前展示界面上查询和获取特定元素的句柄
   Xpath
  
   # Android的布局与控件
   名称       布局方式
   线性布局    linearLayout
   相对布局    RelativelLayout
   帧布局      FrameLayout
   表格布局    TableLayout
   绝对布局    AbsoluteLayout
   
   线性布局: 按照水平或垂直的顺序将子元素(可以是控件或布局)依次按照顺序排列,每一个元素都位于前面一个元素之后
   线性布局分为两种:水平方向和垂直方向的布局
   相对布局: 按照子元素之间的位置关系完成布局
   帧布局: 好比一块在屏幕上提前预定好的空白区域,可以将一些元素填充在里面
   表格布局: 继承了线性布局
   绝对布局: 通过坐标(x,y)来控制组件如何在屏幕中显示,包括定义组件的坐标(x,y)和定义组件的宽高(width和height)
   
   # 控件
   TextView 显示文字
   EditText 输入框,可编辑
   ImageView 显示图片
   Button 按钮
   CheckBox 复选框
   RadioButton 单选按钮
   
   # 控件属性
   index        int       索引
   instance     int       实例
   class        String    类名
   package      String    包名
   Content desc String    描述
   checkable    boolean   控件勾选状态
   clecked      boolean
   clickable    boolean   控件可点击
   enabled      boolean
   focusable    boolean   焦点
   focused      boolean
   Scrollable   boolean   滚动条
   Long-clickable  boolean  长按
   password     boolean    密码
   selected     boolean    选择状态
   bounds       Rect       范围
   ```

6. UiSelector定位控件

   ```markdown
   u2_selector.py
   
   # text文本选取方式
   text 全文本匹配
   textContains 文本包含
   textMatches 正则表达式
   textStartsWith 起始文本
   
   # description文本选取方式
   description 全文本匹配
   descriptionContains 文本包含
   descriptionMatches 正则表达式
   descriptionStartsWith 起始文本
   
   # className选取方式
   className className匹配
   classNameMatches className正则表达式匹配
   
   # resourceId资源ID选取方式
   resourceId 全资源ID匹配
   resourceIdMatches 正则表达式匹配
   
   # 混合定位方式
   父子节点、兄弟节点
   
   # 坐标定位方式 
   # 控件操作和操作超时
   ```
   
7. 通过U2实现移动设备九宫格解锁

   ```markdown
   hack_lock.py
   ```

8. xpath定位方式

   ```markdown
   # xpath
   XML Path Language,即XML路径语言,它是一门在XML文档中查找信息的语言,同样适用于HTML文档的搜索
   
   u2_xpath.py
   xpath_example.html
   
   # xpath常用规则
   /从当前节点选取直接子节点
   //从当前节点选取子孙节点
   .选取当前节点
   ..选取当前节点的父节点
   @选取属性
   
   # xpath helper的chrome插件
   //li[@class='item-0']
   //*
   //li
   //li[@class='item-1']
   //li/a
   //ul
   //ul//a 
   //ul/a
   //a[@href="https://coding.imooc.com/class/283.html"]/../@class
   //a[@href="https://coding.imooc.com/class/283.html"]/parent::*/@class
   //li[@class='other_item']/a/text()
   //li[@class='item-3']//text()
   //li[@class='item-3']/a/@href
   
   # app控件定位方法
   文字属性定位
   资源ID属性定位
   className定位
   链式调用关系定位
   坐标定位
   xpath定位
   ```

9. 登录考研帮app并滑动考研资讯

   ```markdown
   1) 连接设备
   2) 启动app
   3) 判断是否打开了登录页面
   4) 输入用户名密码,点击登录
   5) 判断是否进入app首页,也就是当前洁面是否有研讯控件,点击研讯按钮
   6) 滑动研讯页面,一般在屏幕中间位置滑动,即我们需要获取到屏幕的尺寸大小
   7) 一直向下滑动,当屏幕出现内容已经全部加载完毕这个提示,停止滑动
   8) 关闭app并清理缓存
   
   u2_kaoyanbang.py
   ```

##### 爬虫必备利器-抓包工具的使用
1. fiddler抓包工具详解-1

   ```markdown
   # 常见app抓包软件对比
   抓包软件名称   支持的操作系统  适用平台       调试难易程度   软件功能程度
   fiddler      win/linux    网页端、app端     一般           多
   mitmproxy    win/mac/linux 网页端、app端    一般           多
   packetCapture 安卓          app端          简单           少
   
   # Fiddler抓包软件介绍
   Fiddler是一个web调试代理平台,可以监控和修改web数据流
   功能强大
   1) 支持IE,Chrome,Safari,Firefox和Opera等浏览器
   2) 可以在iphone、ipad等移动设备上进行连接
   优点
   1) 可以查看所有浏览器、客户端应用或服务之间的web数据流
   2) 手动或自动修改任意的请求和响应
   3) 可以解密HTTPS数据流以便查看和修改
   缺点
   1) fiddler只支持http、https、ftp、websocket数据流等相关协议
   2) 无法监测或修改其他数据,如SMTP、POP3等
   3) fiddler无法处理请求和响应超过2GB的数据
   
   Client <=request/response=>Fiddler(Proxy)<=request/response=> Server
   
   File:
   Capture Traffic
   New Viewer
   Load Archive
   Recent Archives
   Save
   Import Sessions
   Export Session
   Exit
   
   Edit:
   Copy
   Remove
   Select All
   Paste as Sessions
   Mark
   Unlock for Editing
   Find Sessions
   
   Tools:
   Options(
      HTTPS: Capture HTTPS CONNECTs
             Decrypt HTTPS traffic
             from remote clients only
             Actions 安装证书)
      Connections: Fiddler listens on port 8888
   WinINET Options
   Clear WinINET Caches
   Clear WinINET Cookies
   TextWizard
   HOSTS
   
   Proxy SwitchyOmega
   新建情景模式: fiddler-代理协议HTTP-代理服务器192.168.0.108-代理端口8888-应用选项
   切换之fidler情景模式
   清理fiddler抓包工具session,通过火狐浏览器打开网址即可
   
   Rules:
   Hide Image Requests
   Hide CONNECTs
   Automatic Breakpoints
   Require Proxy Authentication
   Apply GZIP Encoding
   Remove All Encodings
   Hide 304s
   Automaticically Authenticate
   User-Agents
   Performance
   
   工具栏:
   WinConfig
   🫧 添加session注释
   Replay 重放
   ✖️ 删除
   Go
   Stream
   Decode
   Keep: All sessions
   Any Process
   Find
   Sava
   📷 快照
   🕙 定时器
   Browse
   Clear Cache
   TextWizard
   
   Fiddler Orchestra Beta
   FiddlerScript
   Log
   Filters
   Timeline
   Statistics
   Inspectors
   AutoResponder
   Composer
   Get Started
   ```
   
2. fiddler抓包工具详解-2

   ```markdown
   # 标识符
   # HTTP状态码
   # 请求头和响应头
   Inspectors-Raw
   
   # 设置断点的两种方式
   基于图形界面
   基于命令行
   
   # 基于图形界面
   Rules-Automatic Breakpoints
   
   # 基于命令行
   bpu 取消所有请求包的拦截
   bpafter https://www.baidu.com 响应后断点设置
   bpbefore https://www.baidu.com 请求前断点设置
   bda 取消所有响应包的拦截
   
   # 网页重定向
   选中一个请求,点击AutoResponder,将选中的请求拖过来
   Rule Editor - Find a file - save
   ```
   ![](/Users/bruce/Documents/笔记截图/标识符.png)
   ![](/Users/bruce/Documents/笔记截图/HTTP状态码.png)
   ![](/Users/bruce/Documents/笔记截图/HTTP状态码2.png)

3. fiddler抓包工具详解-3

   ```markdown
   win10: 
   ipconfig查看ip地址
   
   mac:
   夜神模拟器
   网络桥接模式: 开启  
   安装驱动 
   dhcp
   保存重启夜神模拟器
   选择WiredSSID,长按鼠标左键,修改网络,显示高级选项
   代理: 手动
   代理服务器主机名: 192.168.0.108
   代理服务器端口: 8888
   打开自带浏览器: https://www.baidu.com
   192.168.0.108:8888
   FiddlerRoot certificate安装 设置密码
   
   win10:
   Fiddler
   Tools - Options - HTTPS
      from browser only/from remote clients only 
      Allow remote computers to connect
   清除数据包
   点击Stream Decode  Inspectors Raw
   ```
   
4. mitmproxy抓包工具详解

   ```markdown
   # mitmproxy介绍
   mitmproxy就是用于MITM的proxy
   MITM即中间人攻击(Man-in-the-middle attack)
   
   client -1.Request-> mitmproxy -2.Forwarded Request-> server
   
   1) 和正常的代理一样转发请求,保障服务端与客户端的通信
   2) 拦截请求,修改请求,拦截返回,修改返回
   3) 可以载入自定义python脚本
   
   # mitmproxy安装
   pip3 install mitmproxy
   
   火狐浏览器-SwitchyOmega-新建情景模式mitmproxy-HTTP 0.0.0.0 8080-应用选项
   
   安装证书: http://mitm.it/
   双击mitmproxy-ca-cert.pem即可弹出钥匙串管理页面,然后找到mitmproxy证书,选择始终信任即可
   火狐浏览器网络设置: 手动配置代理HTTP代理0.0.0.0 8080 也将此用于HTTPS
   火狐浏览器隐私与安全:查看证书-认证颁发机构-导入证书-信任
   此时可以访问https的网站,截取数据
   
   # mitmproxy的三个组件
   mitmproxy
   mitmdump
   mitmweb
   
   # mitmproxy移动设备安装证书、移动设备抓包
   mitmproxy -p 8080
   
   夜神模拟器
   网络桥接模式: 开启 
   安装驱动
   dhcp
   保存重启夜神模拟器
   选择WiredSSID,长按鼠标左键,修改网络,显示高级选项
   代理: 手动
   代理服务器主机名: 192.168.0.109
   代理服务器端口: 8080
   打开自带浏览器 https://www.baidu.com
   192.168.0.109:8080
   mitm.it: 下载安装并信任android证书 安全-受信任凭据
   z 清除数据包
   
   # mitmproxy数据包过滤和断点调试
   f
   set view_filter '!(~c 200)'
   f
   set view_filter ''
   f
   set view_filter '~d baidu.com'
   f
   set view_filter '~d qq.com'
   f
   set view_filter '~m post & ~u baidu'
   f
   set view_filter ''
   i
   : set intercept '~d baidu.com & ~m get'
   移动设备访问www.baidu.com
   选中数据包,点击
   e request-headers
   d
   q
   e url
   : flow.set @focus url https://xw.qq.com
   q
   a
   移动设备访问www.baidu.com 回车
   response e
   response-body aaaa
   :wq
   q
   a
   
   # mitmdump-dump的使用
   mitmdump_test.py
   mitmdump -p 8080 -s mitmdump_test.py
   http://httpbin.org/get
   ```
   
5. app无法抓包探秘

   ```markdown
   # app限定系统代理接口
   1) 通过xpose框架,编写xpose破解代码,绕过或更改获取系统代理判定的返回值
   下载xposed apk安装包: 
   https://repo.xposed.info/module/de.robv.android.xposed.installer
   通过刷机刷入xposed框架
   2) proxydroid 破解/root  Proxy Switch: 开启 Host Port: fiddler/mitmproxy
   3) Packet Capture
   Packet Capture是一款免root的app,运行在安卓平台上,用于捕获http/https网络流量嗅探的应用程序
   用于捕获数据包,并记录它们,使用中间人技术对SSL解密,无需root权限,这个软件使用android提供的
   VpnService api,实现中间人攻击
   
   # app启用ssl-pinning技术防止中间人攻击
   JustTrustMe
   
   # app采用双向证书绑定技术
   JustTrustMe欺骗客户端,Fiddler欺骗服务端
   逆向app查看数据接口
   ```
   ![](/Users/bruce/Documents/笔记截图/app抓包.png)
   ![](/Users/bruce/Documents/笔记截图/app抓包-2.png)

##### App应用数据抓取入门(豆果美食fiddler版)
1. 抓取前设置、启动豆果美食app并抓包

   ```markdown
   打开夜神模拟器  
   adb connect 127.0.0.1:62001
   adb devices
   adb install /Users/bruce/workspace/mobile-spider/apk/douguomeishi/douguomeishi.apk
   打开fiddler
   Tools-Options-HTTPS
      Capture HTTPS CONNECTs
      Decrypt HTTPS traffic
      from remote clients only
   Tools-Options-Connections
      8888
      Allow remote computers to connect
   Firefox浏览器代理设置
      SwitchyOmega
        新建情景模式 fiddler: HTTP 192.168.0.108 8888 应用选项
      设置-隐私与安全-证书-证书管理器-证书颁发机构-导入证书并完全信任
      设置-网络设置-连接设置-手动配置代理-192.168.0.108 8888 也将此代理应用于HTTPS
   夜神模拟器代理设置
      自带浏览器打开-www.baidu.com/192.168.0.108:8888/安装相关证书并信任
      自带浏览器-设置-隐私和安全-显示安全警告去掉✅
      设置-安全-用户凭证/信任的凭证查看并信任凭证
   打开豆果美食测试fiddler抓包
   ```

2. 分析fiddler抓取的豆果美食数据包

   ```markdown
   api.douguo.net => Find
   /recipe/flatcatalogs
   /recipe/v2/search/0/20
   /recipe/v2/search/20/20
   ```

3. 编写爬虫脚本

   ```markdown
   项目需求、请求函数编写、请求头伪造
   食材页面解析、队列逻辑编写
   获取菜谱列表数据逻辑编写
   详情页数据抓取逻辑编写
   数据入库逻辑编写
   多线程逻辑编写
   伪装爬虫-编写代理逻辑
   
   分析豆果美食数据包
   通过python多线程-线程池抓取数据
   通过使用代理ip隐藏爬虫
   将数据保存到mongodb中
   
   spider_douguomeishi.py
   handel_mongo.py
   handle_proxy.py
   
   pip3 install pymongo -i https://pypi.tuna.tsinghua.edu.cn/simple/
   
   https://www.mongodb.com/try/download/community
   
   /d/MongoDB/Server/6.0/data/db
   /d/MongoDB/Server/6.0/log
   /d/MongoDB/Server/6.0/mongodb.config
   
   dbpath=D:\MongoDB\Server\6.0\data\db
   logpath=D:\MongoDB\Server\6.0\log\mongod.log
   logappend=true
   journal=true
   quiet=true
   port=27017
   
   ./mongod.exe --dbpath "d:mongodbdatadb"  --logpath "d:mongodblogslog.txt"  --install -serviceName "MongoDB"
   
   localhost:27017
   
   MongoDB Compass工具
   show dbs
   use douguo_meishi
   show collections
   db.douguo_meishi_item.find()
   ```
   
##### 抖音数据抓取实战 (appium+uiautomatorviewer+mitmproxy)
1. 短视频抓取实战介绍 & 解析短视频分享页面数据 & 分享id存储数据库逻辑代码编写

   ```markdown
   抖音号、粉丝数、关注数、点赞数
   
   抖音名人: 昵称、抖音id、分享id、粉丝数、关注数、获赞数、个性签名
   粉丝列表数据: 昵称、抖音id、分享id、粉丝数、关注数、获赞数、个性签名
   
   https://www.douyin.com/share/user/分享id
   handle_share_web.py
   douyin_hot_id.txt
   handle_mongo.py
   ```
   
2. ssl pining技术分析与xposed框架安装

   ```markdown
   # 抖音数据抓取实战-常见问题
   问题常见于真实手机上
   打开抓包工具后应用无法联网
   
   # 什么是SSL pinning
   1) 根据浏览器或操作系统Android自带的证书链
   2) 使用自签名证书
   3) 自签名证书加上SSL Pinning特性
   
   SSL Pinning,即SSL证书绑定,是验证服务器身份的一种方式,是在https协议建立通信时增加的代码逻辑,
   它通过自己的方式验证服务器身份然后决定通信是否继续下去.它唯一指定服务器的身份所以安全性较高
   
   # 解决方案
   安装Xposed框架+JustTruestMe组件
   Xposed是一个框架,它可以改变系统和应用程序的行为,而不接触任何APK.它支持很多模块,每个模块可以用来帮助实现不同的功能
   JustTruestMe是一个用来禁用、绕过SSL证书检查的,基于Xposed模块.JustTruestMe是将APK中所有用于校验SSL证书的API都进行屏蔽
   从而绕过证书检查
   
   # 注意事项
   手机必须获取root权限
   安装xposed框架有手机变砖危险
   手机可以直接刷带有xposed框架的系统
   ```

3. 分析接口数据 & appium模拟滑动操作

   ```markdown
   decode_douyin_fans.py
   mitmdump -s decode_douyin_fans.py -p 8888
   
   连接真实手机
   uiautomatorviewer
   appium
   douyin_appium.py
   ```
   
4. 多设备端并发抓取粉丝数据

   ```markdown
   # 抖音数据抓取实战-多任务端
   运行多台设备(模拟器、手机设备)
   运行多个appium服务
   使用Python多进程/多线程
   
   # 抖音数据抓取实战-注意事项
   1) 夜神模拟器的连接端口
   adb connect 127.0.0.1:62001
   通过任务管理器查找noxvmhandle frontend的PID,通过PID在netstat -ano | findstr "PID"中查找端口占用情况
   第一个模拟器端口是62001,第二个模拟器端口是62025,第三个是62025+1
   2) appium客户端设置udid
   3) appium服务端设置bootstrapPort  Advanced Presets
   
   连接真实手机
   mitmdump -s decode_douyin_fans.py -p 8888
   uiautomatorviewer appium
   handle_appium_douyin.py
   
   指定ip代理: mitmdump --mode upstream:http://http-cla.abuyun.com:9030 --upstream-auth 通行证书:通行密钥 -s decode_douyin_fans.py -p 8888
   ```

5. 视频抓取、signarure加密字段破解

   ```markdown
   test.html
   html_head.txt
   html_foot.txt
   handle_douyin_movie.py
   ```

6. 总结

   ```markdown
   # 抖音数据抓取实战-三大块
   个人主页数据、粉丝数据、视频数据
   
   # 抖音数据抓取实战-个人主页数据
   个人数据界面-TTF字体混淆
   
   # 抖音数据抓取实战-粉丝数据
   appium模拟滑动+mitmdump解析数据
   
   # 抖音数据抓取实战-视频数据
   破解js获取signature
   
   # 抖音数据抓取实战-注意事项
   1) TTF字体数据对应-如果抖音引入TTF字体库发生改变,爬虫需要做相应更改
   2) appium模拟滑动抖音粉丝数据,一般仅能获取5000条粉丝数据
   3) 移动设备设置代理进行抓包后,如遇到无法联网或无法解析https数据时,需要安装xposed框架+justtrustme组件进行屏蔽证书强校验
   4) 在设置多设备、多进程数据抓取时,需要设置appium服务端的bootstrap端口以及客户端的udid字段
   5) 视频数据抓取,需要破解signature字段,使用拼接html文件,解析js https://www.douyin.com/share/user/分享id
   6) 数据抓取时需要加上代理,伪装爬虫
   7) 条件允许最好使用真实移动设备
   ```

##### 打造多任务端app应用数据抓取系统(2019版)
1. 打造多任务端app应用数据抓取系统-架构图

   ```markdown
   mongodb =pymongodb=> appium-python-client =http通讯=> docker appium <-http通讯-> 快手
                                                        docker appium <-http通讯-> 今日头条
   ```
   
2. Docker系统管理

   ```markdown
   # Docker基本概念
   什么是docker hub
   Docker Hub是一个仓库:https://hub.docker.com/
   仓库是集中存放镜像文件的场所
   仓库分为公开仓库Public和私有仓库Private两种形式
   
   docker login
   docker search centos
   docker images
   docker pull centos
   
   什么是镜像 
   linux镜像 docker镜像
   Docker镜像是一个特殊的文件系统,除了提供容器运行时所需的程序、库、资源、配置文件外,还包含了一些为运行时准备的一些配置参数(如匿名卷、
   环境变量、用户等).镜像不包含任何动态数据,其内容在构建之后也不会被改变
   
   什么是容器
   容器是一种轻量级,可移植,自包含的软件打包技术,是一种应用程序,可以在几乎任何地方以相同的方式运行
   开发人员在自己笔记本上创建并测试好的容器,无需任何修改就能在生产系统的虚拟机,物理服务器或公有云主机上运行
   为什么需要容器以及为什么被称为容器
   
   容器的优势,对于开发人员来说,创建一次,可以在任何地方运行,对于运维人员来说,配置一次,可以运行所有应用
   docker的核心组件包括: docker客户端,docker服务器,docker镜像,registry,docker容器
   
   docker客户端
   在linux系统下,Docker Client和Docker daemon、容器直接运行在宿主机上,这意味着容器可直接使用宿主机端口资源,
   不需要在容器和宿主机之间映射端口
   在win或mac系统下,Docker服务运行在linux虚拟机里,Docker client运行在宿主机下跟Docker服务通信.当运行容器里,它用的端口资源
   是虚拟机里的,必须跟宿主机上的端口映射

   docker服务
   docker服务是docker最核心的后台进程,他负责响应来自docker client的请求,然后将这些请求翻译成系统调用完成容器管理操作
   该进程会在后台启动一个API Server,负责接收由docker client发送的请求;接收到的请求将通过docker服务内部的一个路由分发调度,再由
   具体的函数来执行请求
   
   # Docker copy-on-write
   docker run --name centos-test -it centos /bin/bash
   docker ps -a
   
   # 基础命令
   docker run centos pwd
   docker ps -l
   docker ps -a
   docker run centos /bin/bash -c "while true;do sleep 1;done"
   docker run  -d centos /bin/bash -c "while true;do sleep 1;done"
   短ID是长ID的前12个字符
   docker run --name centos-while  -d centos /bin/bash -c "while true;do sleep 1;done"
   docker stop centos-while
   docker stop 短ID
   docker kill 短ID
   docker run  -d centos /bin/bash -c "while true;do sleep 1;echo hello world;done"
   docker attach 长ID
   docker exec -it 短ID bash
   ps -ef
   ps -elf
   exit
   
   attach和exec的区别:
   attach直接进入容器启动命令的终端,不会启动新的进程
   exec则是在容器中打开新的终端,并且可以启动新的进程
   如果想直接在终端中查看启动命令的输出,用attach;其他的情况使用exec
   
   容器运行
   dokcer run -it centos /bin/bash
   docker客户端使用docker命令来运行,run参数表明客户端要运行一个新的容器
   docker客户端要运行一个容器需要告诉docker守护进程的最小参数信息是:
   1) 这个容器从哪个镜像创建,这里是centos,基础的centos镜像
   2) 在容器中要运行的命令,这里是/bin/bash,在容器中运行bash shell
   
   按照顺序,docker做了这些事情:
   1) 拉取centos镜像:docker检查centos镜像是否存在,如果在本地没有该镜像,docker会从docker hub下载.如果镜像已经存在,docker会使用它来创建新的容器
   2) 创建新的容器: 当docker有了这个镜像之后,docker会用它来创建一个新的容器
   3) 分配文件系统并且挂载一个可读写的层:容器会在这个文件系统中创建,并且一个可读写的层被添加到镜像中
   4) 分配网络/桥接接口: 创建一个允许容器和本地主机通信的网络接口
   5) 设置一个IP地址: 从池中寻找一个可用的IP地址并且附加到容器上
   6) 运行你指定的程序: 运行指定的程序
   7) 捕获并且提供应用输出:连接并且记录标准输出、输入和错误让你可以看到你的程序如何运行的
   
   docker start 短ID
   docker restart 短ID
   docker pause 短ID
   docker unpause 短ID
   docker rm 短ID
   docker rm -v $(docker ps -aq -f status=exited)
   docker rmi hello-world
   
   提供服务
   云主机
   IPV4和IPV6
   NAT技术
   
   docker run -d -p 80 httpd
   192.168.0.109:32769
   docker run -d -p 80:80 httpd
   
   docker镜像的创建-docker镜像创建的两种方法
   使用commit命令创建docker镜像
   编写Dockerfile创建docker镜像
   
   docker镜像的创建-使用commit命令创建docker镜像
   docker run --name webserver -d -p 80:80 nginx
   docker exec -it webserver bash
   echo '<h1>Hello,Docker!<h1>' > /usr/share/nginx/html/index.html
   docker diff webserver
   
   docker commit --author "dazhuang" --message "modify default page" webserver  nginx:v2
   docker images
   docker history nginx:v2
   docker ps -a
   docker run --name web2 -d -p 81:80 nginx:v2
   使用docker commit命令虽然可以比较直观的帮助理解镜像分层存储的概念,但是实际环境中并不会这样使用
   由于命令的执行,还有很多文件被改动或添加了.这还仅仅是最简单的操作,如果是安装软件包、编译构建,那么有大量的无关内容被添加进来,如果不小心清理
   将会导致镜像极为臃肿
   此外,使用docker commit意味着所有对镜像的操作都是黑箱操作,生成的镜像也被称为黑箱镜像
   
   docker镜像的创建-编写Dockerfile创建docker镜像
   什么是Dockerfile
   Dockerfile是一个文本文件,其内包含了一条条的指令,每一条指令构建一层,因此每一条指令的内容,就是描述该层应当如何构建
   mkdir mynginx
   touch Dockerfile
   FROM nginx
   RUN echo '<h1>Hello,Docker!<h1>' > /usr/share/nginx/html/index.html
   
   FROM和RUN
   FROM指定基础镜像
   基础镜像是必须指定的.而FROM就是指定基础镜像,因此一个Dockerfile中FROM是必备的指令,并且必须是第一条指令
   RUN执行命令
   RUN指令是用来执行命令行命令的.由于命令行的强大能力,RUN指令在定制镜像时是最常用的指令之一
   
   RUN指令的两种模式
   shell格式: RUN <命令>,就像直接在命令行中输入的命令一样
   exec格式: RUN ["可执行文件","参数1","参数2"],这更像是函数调用中的格式
   不超过127层
   
   docker build -t nginx:v3 .
   docker images
   https://hub.docker.com => create repository => nginxv3 => create
   docker info
   docker tag nginx:v3 450120127/nginxv3:v3
   docker push 450120127/nginxv3:v3
   docker pull 450120127/nginxv3:v3
   ```

3. Docker-appium的使用
   
   ```markdown
   # 在linux系统中安装appium
   https://oxygeneningine.github.io/技术/2017/10/18/install-auto-test-environment-on-centos-7
   
   # 搜索拉取appium镜像 (配置docker加速器)
   docker search appium
   docker pull appium/appium
   
   # github的appium-docker-android项目
   https://github.com/appium/appium-docker-android
   
   # ssh连接docker host
   user: docker
   pass: tcuser
   
   # 创建appium容器 & 设置appium容器连接安卓模拟器
   docker images
   docker ps -a
   docker run --privileged -d -p 4723:4723 --name appium1 appium/appium
   docker ps -a
   启动android模拟器
   adb devices
   adb -s 127.0.0.1:62001 tcpip 5555 
   docker exec -it appium1 adb devices
   docker exec -it appium1 adb connect 172.17.100.15:5555
   docker exec -it appium1 adb devices

   test.py
   docker exec -it appium1 bash
   cd /var/log
   tail -f appium.log
   ```
   
4. 打造多任务端app应用数据抓取系统-实现篇

   ```markdown
   # 任务需求详解
   1) 抓取抖音当前视频的作者数据
   2) 抓取快手当前视频的作者数据
   3) 抓取今日头条推荐板块新闻
   
   decode_data.py
   handle_appium_docker.py
   handle_mongo.py
   
   # 系统搭建步骤
   1) 下载mongodb、appium、450120127/pythonv2镜像 docker pull 450120127/pythonv2
   2) 设置docker toolbox网卡状态到桥接
   3) 设置docker toolbox共享,挂载共享文件夹
   4) 创建并启动相应容器
   
   # 常见报错
   更改虚拟机网络桥接后,虚拟机无法启动
   启动夜神模拟器后,夜神模拟器与docker无法通信,同时重启虚拟机,有如下报错:不能为虚拟电脑1.0打开一个新任务;不能为虚拟电脑h1打开一个新任务
   
   # 解决方法
   升级vitualbox
   安全驱动VirtualBox NDIS6 Bridged Networking Driver:
   VirtualBox NDIS6 Bridged Networking Driver => 安装 => 服务 => 添加 => 从磁盘安装 
   => Oracle/VirtualBox/drivers/network/netlwf/VBoxNetLwf.inf => 确定
   
   下载mongodb、appium、450120127/pythonv2镜像 docker pull 450120127/pythonv2
   设置docker toolbox网卡状态到桥接
   设置docker toolbox共享,挂载共享文件夹
   
   # 会话 python
   ifconfig | more
   ssh连接docker host
   mkdir docker
   /home/docker/docker
   sudo mount -t vboxsf /Users/bruce/workspace/mobile-spider/chapter07 /home/docker/docker
   mount 
   sudo umount /home/docker/docker
   sudo mount -t vboxsf /Users/bruce/workspace/mobile-spider/chapter07 /home/docker/docker
   docker images
   docker run -it -v /home/docker/docker:/root/ --name python 450120127/pythonv2 /bin/bash
   
   # 会话  mitmdump
   docker images
   docker run --rm -it -v /home/docker/docker:/root/ -p 8889:8889 -name mitmdump 450120127/pythonv2 mitmdump -p 8889 -s /root/decode_data.py
   
   # 会话 appium
   docker run --privileged -d -p 4723:4723 --name appium_douyin appium/appium
   docker run --privileged -d -p 4724:4723 --name appium_kuaishou appium/appium
   docker run --privileged -d -p 4725:4723 --name appium_jrtt appium/appium
   
   # 会话 mongodb
   docker run -p 27017:27017 -v /home/docker/docker:/root/ -d --name mongodb mongo
   
   # win10
   开启三个夜神模拟器
   网络桥接模式、安装相应证书fiddler/mitmproxy/mitmproxy、抖音/快手/今日头条apk安装
   adb connect 127.0.0.1:62001
   adb connect 127.0.0.1:62025
   adb connect 127.0.0.1:62026
   
   adb -s 127.0.0.1:62001 tcpip 5555
   adb -s 127.0.0.1:62025 tcpip 5555
   adb -s 127.0.0.1:62026 tcpip 5555
   
   # 会话 appium
   docker ps -a
   docker exec -it appium_douyin adb devices
   docker exec -it appium_douyin adb connect xxxx:5555
   docker exec -it appium_kuaishou adb connect xxxx:5555
   docker exec -it appium_jrtt adb connect xxxx:5555
   
   # 会话 python
   本地修改python文件,此会话python会同步修改
   python handle_appium_docker.py
   
   # 会话  mitmdump
   # 会话 mongodb
   ```
   
##### 抖音数据抓取实战(fiddler+u2+mitmproxy)
1. 短视频抓取需求分析

   ```markdown
   # 需求分析
   抖音当前视频标题
   抖音用户主页
   
   # 需求拆解
   模拟滑动视频和点击发布者
   通过mitmproxy解析返回数据
   
   # app操作流程
   连接设备
   启动app
   判断当前所处页面
   进入发布者个人页面
   滑动视频
   遇到广告
   停止操作
   退出app,清除缓存
   
   # 抓取app返回数据包
   通过fiddler抓取相关接口
   编写mitmdump逻辑抓取返回数据并查看
   
   # 安装vmware tools
   直接拖拽主机文件到虚拟机
   直接使用vmware虚拟机的terminal
   cd /media/hadoop/VMware Tools
   cp VMwareTools-10.3.23-16594550.tar.gz /home/hadoop/app/
   tar -zxvf VMwareTools-10.3.23-16594550.tar.gz
   sudo ./vmware-install.pl
   显示器 加速3D图形 勾选
   图形内存 768MB
   ```
   
2. 通过u2实现滑动短视频

   ```markdown
   weditor+uiautomator2
   handle_douyin.py
   ```

3. 通过mitmproxy解析短视频app返回数据

   ```markdown
   # 接口分析
   1) fiddler处于与移动设备同一个网络下
   2) 网络处于可通信状态
   3) 移动设备安装相关证书并信任
   4) fiddler相关设置(Tools-Options-HTTPS/Connections)
   
   移动设备需要点击到需要抓取的页面
   右上面: 选中要找的包->Inspectors->Raw/Headers
   右下面: Raw/JSON
   
   # 编写mitmdump解析文件 & 运行并查看
   decode_douyin.py
   
   mitmdump -s decode_douyin.py -p 8889
   运行handle_douyin.py
   ```
   
##### 多设备管理atxserver2库(2020版)
1. atxserver2库介绍

   ```markdown
   需求: 
   移动设备(Android和IOS)异地调试
   移动设备管理、重启、关机、网络管理等
   结合设备管理平台完成app UI自动化测试
   异常调试时延迟可接受,画质可接受
   
   atxserver2:
   ATX2是一款可以远程控制Android和IOS设备的设备管理平台
   该平台使用的技术栈为Python3+NodeJS+RethinkDB
   作者:codeskyblue
   
   atxserver2架构: 只支持usb连接
   atxserver2功能
   ```
   atxserver2架构.png
   atxserver2功能.png
   atxserver2功能2.png
   atxserver2功能3.png
   atxserver2功能4.png
   atxserver2功能5.png

2. atxserver2通过pip安装部署

   ```markdown
   安装rethinkdb数据库:https://rethinkdb.com/docs/install/ubuntu/
   下载rethinkdb的deb文件手动安装
   https://github.com/srh/rethinkdb/realeases/tag/v2.3.6.srh.1
   sudo dpkg -i rethinkdb_2.3.6.srh.1.0bionic_and64.deb
   rethinkdb启动
   
   wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
   tar -xf Python-3.8.0.tgz
   cd Python-3.8.0
   ./configure --enable-optimizations
   make -j 4
   sudo make install
   python3.8 --version
   sudo rm -rf /usr/bin/python
   sudo rm -rf /usr/bin/pip
   sudo ln -s /usr/local/bin/pip3.8 /usr/bin/pip
   sudo ln -s /usr/local/bin/python3.8 /usr/bin/python
   
   下载atxserver2项目: git clone https://github.com/openatx/atxserver2.git
   启动atxserver2:
   cd atxserver2
   virtualenv --python=/usr/bin/python venv
   source venv/bin/activate
   sudo pip install -r requirements.txt -i https://pypi.douban.com/simple
   sudo python main.py
   http://192.168.0.101:4000
   
   安装atxserver2-android-provider:
   安装nodejs8
   curl -sL https://deb.nodesource.com/setup_8.x|sudo -E bash -
   sudo apt-get install -y nodejs
   下载atxserver2-android-provider项目
   git clone https://github.com/openatx/atxserver2-android-provider.git
   cd atxserver2-android-provider
   npm install
   virtualenv --python=/usr/bin/python venv
   source venv/bin/activate
   sudo pip install -r requirements.txt -i https://pypi.douban.com/simple
   sudo python main.py --server http://192.168.0.101:4000
   手机连接电脑
   
   设备发现:
   Provider可以通过adb track-devices自动发现已经接入的设备
   minicap,
   minittouch,
   atx-agent,
   app-uiautomator-[test].apk,
   whatsinput-apk
   ```

3. atxserver2多设备管理库的使用

   ```markdown
   rethinkdb:
   设计用来存储JSON文档的分布式数据库,可以通过简单操作实现多机分布式存储.支持表的联合和分组查询

   cd /etc/rethinkdb
   sudo cp default.conf.sample default.conf
   sudo vim default.conf
   bind=0.0.0.0
   sudo cp default.conf instances.d/
   nohup rethinkdb --config-file /etc/rethinkdb/instances.d/default.conf

   192.168.0.101:8080
   Data Explorer
   查询数据库 r.dbList()
   查询数据表 r.db('atxserver2').tableList()
   查询表内数据 
   r.db('atxserver2').table('users') mi
   r.db('atxserver2').table('devices')
   r.db('atxserver2').table('groups')

   192.168.0.101:4000
   用户信息
   设备列表 点击使用
   操控设备
   浏览器打开URL
   快捷入口 Settings 开发者 Wifi
   增加快捷命令
   Terminal:
   pm list packages -3
   ifconfig
   安装管理
   文件管理
   截图
   应用管理
   点击使用多台设备
   
   Ubuntu:
   adb devices
   adb -s 设备id shell
   ifconfig
   ```

4. 实现多任务端app应用数据抓取系统

   ```markdown
   # 多任务端app应用数据抓取使用技术
   atxserver2+u2+mitmproxy (2台设备)  
   
   weditor 
   fiddler接口分析:
   1) fiddler处于与移动设备同一个网络下
   2) 网络处于可通信状态
   3) 移动设备设置fiddler代理、安装相关证书并信任
   4) fiddler相关设置(Tools-Options-HTTPS/Connections)
   
   移动设备需要点击到需要抓取的页面
   右上面: 选中要找的包(json)->Inspectors->Raw/Headers
   右下面: Raw/JSON
   
   python多进程
   
   # 多任务端app应用数据抓取架构
   mitmdump       手机屏幕监控 手机屏幕监控 手机屏幕监控  http通讯   Atx-agent 移动设备 192.168.0.102   http通讯  短视频信息
   192.168.0.101      atxserver2                    http通讯   Atx-agent 移动设备 192.168.0.104   http通讯  快手
                     192.168.0.101                  http通讯   Atx-agent 移动设备 192.168.0.106   http通讯  今日头条       
   
   # 多任务端app应用数据抓取实现
   decode_douyin.py(无需改动)
   handle_douyin.py(主要改动)
   
   移动设备: mitproxy代理开启 192.168.0.101 8889
   ubuntu: 
   nohup rethinkdb --config-file /etc/rethinkdb/instances.d/default.conf &
   
   cd atxserver2
   source venv/bin/activate
   python main.py
   http://192.168.0.101:4000
   
   cd atxserver2-android-provider
   source venv/bin/activate
   python main.py --server http://192.168.0.101:4000
   手机连接电脑
   
   mitmdump -s decode_douyin.py -p 8889
   
   运行handle_douyin.py
   
   http://192.168.0.101:4000 打开链接
   ubuntu: mitmdump
   ```

##### elasticsearch 
1. es介绍和安装

   ```markdown
   ELK Elasticsearch Lohstash Kibana
   Elastic Stack Elasticsearch Lohstash Kibana beats
   
   Elasticsearch:
   是基于java的开源分布式搜索引擎
   分布式、零配置、自动发现、索引自动分片、索引副本机制、restful风格接口、多数据源、自动搜索负载等
   
   Logstash:
   是基于java,开源的用于收集、分析和存储日志的工具
   
   Kibana:
   是基于nodejs,开源的免费的工具
   Kibana可以为Logstash和Elasticsearch提供的日志分析友好的Web界面,可以汇总、分析和搜索重要数据日志
   
   beats:
   elastic公司开源的一款采集系统监控数据的代理agent,是在被监控服务器以上客户端形式运行的数据收集器的统称
   
   Elasticsearch安装:
   https:/www.elastic.co/guide/en/elasticsearch/reference/current/deb.html#install-deb
   wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.7.1-amd64.deb
   sudo dpkg -i elasticsearch-7.7.0-amd64.deb
   cd /usr/share/elasticsearch
   sudo vim /etc/elasticsearch/elasticsearch.yml
   network.host: 0.0.0.0
   cluster.initial_master_nodes: node-1
   启动es
   service elasticsearch start
   /usr/share/elasticsearch/bin/elasticsearch -d
   curl http://localhost:9200
   curl http://192.168.0.101:9200
   ps -ef|grep elasticsearch
   cat /etc/passwd
   192.168.0.101:9200
   ```

2. 数据可视化组件kibana的安装和在es基本的增删改查

   ```markdown
   Elasticsearch术语:
   文档document
   用户存储在es中的数据文档,他是es中存储最小单元
   索引index
   index类比为MySQL的表
   节点Node
   一个node就是esde一个运行实例
   集群cluster
   有一个或多个节点组成,对外提供服务
   
   Kibana安装:
   https:/www.elastic.co/guide/en/kibana/reference/current/deb.html#install-deb
   wget https://artifacts.elastic.co/downloads/kibana/kibana-7.7.1-amd64.deb
   sudo dpkg -i kibana-7.7.0-amd64.deb
   cd /usr/share/kibana
   sudo vim /etc/kibana/kibana.yml
   server.port: 5601
   server.host: "192.168.0.101"
   elasticsearch.hosts: ["http://localhost:9200"]
   il8n.locale: "zh-CN"
   启动es
   service kibana start
   ps -ef|grep elasticsearch
   cat /etc/passwd
   192.168.0.101:5601
   
   es.md
   ```

3. es查询进阶 & es查询排序 & es分页查询 & es布尔查询 & es结果过滤 & es高亮显示 & es聚合函数查询 & es分组查询

   ```markdown
   es.md
   
   Elasticsearch查询:
   查询字符串(query string),简单查询
   通过DSL语句来进行查询
   
   Elasticsearch布尔查询:
   must(and)
   should(or)
   must_not(not)
   filter
   
   查询国别为蜀国和性别为男和年龄为39岁的人
   查询年龄为39岁标签为闭月羞花的人
   查询年龄不为39岁和标签不为闭月羞花和性别不为男的人
   查询年龄大于39岁,国别为魏国的人
   
   must: 与关系  and
   should: 或关系 or
   must_not: 非关系 not
   filter: 过滤条件
   range: 条件筛选范围
   gt: 大于
   gte: 大于等于
   lt: 小于
   lte: 小于等于
   
   Elasticsearch聚合函数:
   Avg平均值
   Max最大值
   Min最小值
   Sum求和

   求吴国所有人年龄的平均值,包括所有男人和女人
   求吴国所有人年龄中最大年龄的人
   求吴国所有人年龄中最小年龄的人
   求吴国所有人年龄的和
   
   Elasticsearch分组查询:
   查询所有人的年龄段,并按照10-20、20-30、30-40、40-50四个分组,并且算出每组的平均年龄10
   ```
   
4. `_doc`是用来做什么的

   ```markdown
   Elasticsearch的type:
   索引在6.x中创建只允许每个索引使用单一类型,类型可以使用任何名称,但只能有一个,首选的类型名称是_doc
   在7.0中,_doc是路径的一个永久部分,它表示端点名称,而不是文档类型
   ```

5. es mappings的三种模式

   ```markdown
   Elasticsearch的mappings:
   映射mappings就是elasticsearch中定义的表结构
   哪些字符串该被视为全文字段
   哪些字段包含数字、日期或地理位置
   定义日期的格式
   自定义规则,用来控制动态添加字段的映射
   
   Elasticsearch字段数据类型:
   简单类型,如文本text、关键字keyword、日期date、整形long、双精度double、布尔boolean或ip
   可以是支持JSON的层次结构性质的类型,如对象或嵌套
   或者一种特殊类型,如geo_point、geo_shape或completion
   
   Mappings的三种类型:
   动态映射(dynamic)
   静态映射
   严格映射(strict)
   
   es.md
   ```

6. es的分词器 & 修改es的分词器

   ```markdown
   数据入库:
   原始文本->分析器(字符过滤器->标准分词器->分词过滤器 分词过滤链-小写、停用词、同义词)->建立倒排索引
   cnblogs.com/Neeo/articles/10593037.html
   
   停用词:
   1. 有些词在文本中出现的频率非常高,但是对文本所携带的信息基本不产生影响
   2. 一些英文,如a、an、the、of
   3. 中文, 如的、了、着、是、标点符号等
   4. 文本经过分词之后,停用词通常被过滤掉,不会被进行索引
   5. 在检索的时候,用户的查询中如果含有停用词,检索系统也会将其过滤掉(因为用户输入的查询字符串也要进行分词处理)
   6. 排除停用词可以加速建立索引的速度,减少索引库文件的大小
   
   默认分词器:
   Standard Analyzer-默认分词器,按词切分,小写处理
   Simple Analyzer-按照非字母切分(符号被过滤),小写处理
   Stop Analyzer-小写处理,停用词过滤
   Whitespace Analyzer-按照空格切分,不转小写
   Keyword Analyzer-不分词,直接将输入当作输出
   Patter Analyzer-正则表达式,默认\W+(非字符分割)
   Language-提供了30多种常见语言的分词器
   Customer Analyzer 自定义分词器
   
   IK分词器: 
   https://github.com/medcl/elasticsearch-analysis-ik/releases
   安装是注意下载IK的版本和elasticsearch的版本要匹配
   
   IK分词器的安装:
   sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.7.0/elasticsearch-analysis-ik-7.7.0.zip
   安装完插件需要重启ES,才能生效
   
   IK有两种颗粒度的拆分:
   ik_smart: 会做最粗粒度的拆分
   ik_max_word: 会将文本做最细粒度的拆分
   
   es.md
   ```
   
7. 倒排索引

   ```markdown
   什么是elasticsearch:
   一个分布式多用户能力的全文搜索引擎
   
   倒排索引:
   Term  => Term       => Posting
   Index    Dictionary    List
   Term 单词
   Term Index 单词索引
   Term Dictionary 单词字典
   Posting List 倒排列表
   
   id    name   gender  age  address
   1     张三      1     22   北京市朝阳区
   2     李四      2     21   上海市徐汇区
   3     王五      1     23   上海市虹口区
   
   name字段:
   Term  Posting List
   张三      1
   李四      2
   王五      3
   
   age字段:
   Term  Posting List
   21       2
   22       1
   23       3
   
   gender字段:
   Term  Posting List
   1       [1,3]
   2         2
   
   address字段:
   Term  Posting List
   北京市   1
   上海市   [2,3]
   徐汇区    2
   虹口区    3
   朝阳区    1
   ```

8. 通过python操作es增删改查 & 通过python操作es批量添加数据

   ```markdown
   pip install elasticsearch==7.7.0 -i https://pypi.douban.com/simple
   elasticsearch_demo.py
   input_some_data.py
   ```
   
##### 数据可视化-kibana 1h42min
1. 向es导入示例数据

   ```markdown
   什么是Kibana:
   Kibana是一个针对ES的开元分析及可视化平台,用来搜索、查看交互存储在ES索引中的数据
   使用Kibana,可以通过各种图表进行高级数据分析及展示

   示例数据: https://www.elastic.co/guide/cn/kibana/current/tutorial-load-dataset.html
   
   es.md
   上传shakespeare_6.0.json、accounts.json、logs.jsonl到ubuntu
   curl -H 'Content-Type: application/x-ndjson' -XPOST '192.168.0.101:9200/shakespeare/_doc/_bulk?pretty' --data-binary @shakespeare_6.0.json
   curl -H 'Content-Type: application/x-ndjson' -XPOST '192.168.0.101:9200/bank/account/_bulk?pretty' --data-binary @accounts.json
   curl -H 'Content-Type: application/x-ndjson' -XPOST '192.168.0.101:9200/_bulk?pretty' --data-binary @logs.jsonl
   把,"_type":"log"替换为空
   ```

2. kibana的index-pattern

   ```markdown
   索引模式(index pattern):
   索引模式是kibana用来从es取数据使用的
   192.168.0.101:5601
   Management-> 索引模式 -> 创建索引模式 -> 定义索引模式 logstash* -> 配置设置 时间筛选字段名称 @timestamp -> 创建索引模式
   url  url.keyword 编辑 格式 URL 保存字段
   ```

3. kibana的discover

   ```markdown
   点击小日历-选择时间 2015-05-17 Update
   十字变小手点击柱形图
   十字选择左外三个柱
   十字选择里面三个柱
   点击下面向右的箭头查询一条数据
   搜索框搜索geo.src.keyword:"CN" Updata
   
   Dev Tools
   GET logstash*/_search
   {
     "query": {
       "match": {
         "geo.src.keyword": "CN"
       }
     }
   }
   点击小板手-自动缩进-拷贝:
   {"match":{"geo.src.keyword":"CN"}}
   
   Discover
   搜索框搜索 {"match":{"geo.src.keyword":"CN"}} KQL关闭 Refresh   Lucene
   
   点击添加筛选-字段@tags 运算符 是  值 warning 保存
   
   点击筛选条件-编辑筛选、排除结果(取反)、暂时禁用、删除、在所有应用固定-Refresh
   
   选定字段-_source
   
   可用字段-tags agent clientip geo.src +
   
   点击下面向右的箭头查询一条数据 表: 鼠标放到@message + 筛留值 - 筛除值 小书-在表中切换列 文档+字段是否存在筛选 JSON
   查看周围文档 查看单个文档
   ```

4. es聚合分析-pipeline

   ```markdown
   pipeline:
   管道聚合分析,支持对聚合分析的结果再次进行聚合分析,支持链式调用
   
   Sibling-结果和现有分析结果同级
   max / min / avg & sum bucket
   stats / extended stats bucket
   percentiles bucket
   
   Parent - 结果内嵌到现有的聚合分析结果之中
   Derivate-求导
   Cumultive Sum-累计求和
   Moving Function-移动平均
   
   聚合分析样例数据.txt
   es.md
   ```

5. kibana的visualize基本图形-折线图

   ```markdown
   Visualize-新建可视化-面积图-选择logstash*
   右边-指标-Y轴
   右边-存储桶-添加X轴-聚合 Date Histogram-最小时间间隔 3h-定制标签 日期-更新
   右边-存储桶-添加-拆分序列-子聚合 词 -字段 geo.src.keyword-更新
   右边-存储桶-X轴/拆分序列折起来-启用/禁用聚合、拖拉选择优先级-更新
   右边-存储桶-添加-拆分图表-行-子聚合 词 -字段 geo.src.keyword-更新
   拆分序列->拆分图表->X轴
   右边-存储桶-添加-拆分图表-字段-子聚合 词 -字段 geo.src.keyword-更新
   右边-指标-Y轴-添加点大小-聚合 唯一计数-字段 clientip.keyword  4%-更新
   右边-指标和轴-图表类型 折线图-模式堆叠
   ```

6. kibana的visualize基本图形-热力图

   ```markdown
   Visualize->新建可视化->热力图->选择logstash*-2015/05/18 00:00:00 - 2015/05/22 23:30:00
   右边-数据-指标、存储桶-X轴-聚合 Date Histogram-最小时间间隔 3h-字段@timestamp-更新
   右边-数据-指标、存储桶-Y轴-子聚合 词 -字段 geo.src.keyword-大小 15-更新
   Y轴-X轴
   选项-颜色模式-黄到红
   ```

7. kibana的visualize基本图形-饼图

   ```markdown
   Visualize->新建可视化->饼图->选择logstash*-2015/05/18 00:00:00 - 2015/05/22 23:30:00
   右边-数据-指标、存储桶-拆分切片-聚合 词 -字段 geo.src.keyword-大小 15-更新
   右边-数据-指标、存储桶-拆分切片-聚合 词 -字段 ip.keyword-大小 5-更新
   选项-显示标签、饼图设置 圆环图
   ```

8. kibana的visualize基本图形-数据表

   ```markdown
   Visualize->新建可视化->数据表->选择logstash*-2015/05/18 00:00:00 - 2015/05/22 23:30:00
   右边-数据-指标、存储桶-拆分行-聚合 Date Histogram-最小时间间隔 每日-字段@timestamp-更新
   右边-数据-指标、存储桶-拆分行-子聚合 词 -字段 geo.src.keyword-大小 5-更新
   选项-每页最大行数 20
   ```

9. kibana的visualize基本图形-仪表盘

   ```markdown
   Visualize->新建可视化->仪表盘图->选择logstash*-2015/05/18 00:00:00 - 2015/05/22 23:30:00
   选项-范围 0-4000 4000-8000 8000-12000 12000-16000-更新
   ```

10. kibana的visualize基本图形-目标图 

   ```markdown
   Visualize->新建可视化->目标图->选择logstash*-2015/05/18 00:00:00 - 2015/05/22 23:30:00
   选项-范围 百分比模式关闭  0-2000 ... 添加范围 ... 18000-20000 -更新
   右边-数据-指标、存储桶-拆分组-聚合 词 -字段 geo.src.keyword-大小 5-更新
   ```

11. kibana的visualize的timelion

   ```markdown
   Timelion:
   Timelion是一个时间序列数据的可视化,可以结合在一个单一的可视化完全独立的数据源.它是由一个简单的表达式语言驱动的,用来检索时间序列数据,
   进行计算,然后可视化结果
   
   Timelion可以解决哪些问题:
   每个唯一用户在一段时间内查看多少页
   本周五和上周五之间的流量有什么不同
   日本百分之几的人口今天来到我的网站
   标准普尔500指数10日移动平均线是多少
   过去两年内收到的所有搜索请求累计总和是多少
   
   数据源设定类:
   .elasticsearch(): 从ES读取数据
   .es(q="querystring",metric="cardinality:uid",index="logstash-*",offset="-1d"):.elasticsearch()的简写
   .graphite(metric="path.to.*.data",offset="-1d"):从graphite读取数据
   .quandl(): 从quandl读取quandl码
   .worldbank_indicators():从worldbank.org读取国家数据
   .wbi():.worldbank_indicators()的简写
   .worldbank():从worldbank.org读取数据
   .wb(): .worldbank()的简写
   
   可视化效果类:
   .bars($width):用柱状图展示数组
   .lines($width,$fill,$show,$steps):用折线图展示数组
   .point():用散点图展示数组
   .color("#c6c6c6"):改变颜色
   .hide():隐藏该数组
   .label("change from %s"):标签
   .legend($position, $column):图例位置
   .static(value=1024,label="1k",offset="-1d", fit="scale"): 在图形上绘制一个固定值
   .value(): .static()的简写
   .title(title="qps"):图标标题
   .trend(mode="linear",start=0,end=-10):采用linear或log回归算法绘制趋势图
   .yaxis($yaxis_number,$min,$max, $position):设置Y轴属性,.yaxis(2)表示第二根Y轴
   
   数据运算类:
   .abs():对整个数组元素求绝对值
   .precision($number):浮点数精度
   .cusum($base):数组元素之和,再加上$base
   .derivative():对数组求导数
   .divide($divisor):数组元素除法
   .multiply($multiplier): 数组元素乘法
   .subtract($term):数组元素减法
   .sum($term):数组元素加法
   .add():同.sum()
   .plus(): 同sum()
   .first(): 返回第一个元素
   .movingaverage($window): 用指定的窗口大小计算移动平均值
   .mvavg():.movingaverage()的简写
   .movingstd($window):用于指定的窗口大小计算移动标准差
   .mvstd():.movingstd()的简写
   .fit($mode): 使用指定的fit函数填充空值,可选项有: average,carry,nearest,none,scale
   .holt(alpha=0.5, beta=0.5, gamma=0.5,season="1w",sample=2):即ES的pipeline aggregation所支持的holt-winters算法
   .log(base=10):对数
   .max(): 最大值
   .min(): 最小值
   .props(): 附加额外属性,比如.props(label=bears!)
   .range(max=10,min=1):保持形状的前提下修改最大值最小值
   .scale_interval(interval="1s"): 在新间隔下再次统计,比如把一个原本5min间隔的date_histogram改为每秒的结果
   .trim(start=1, end=-1):裁剪序列值
   
   逻辑运算类:
   .condition(operator="eq",if=100,then=200):支持eq、ne、lt、gt、lte、gte等操作符,以及if、else、then赋值
   .if(): .condition()的简写
   
   Visualize->新建可视化-Timelion->选择logstash*-2015/05/18 00:00:00 - 2015/05/22 23:30:00
   Timelion表达式:
   .es(index=logstash*,metric=count)
   
   .es(index=logstash*,metric=count,offset=-1d)
   
   .es(index=logstash*,metric=count,offset=-1d),.es(index=logstash*,metric=count)
   
   .es(index=logstash*,metric=count,offset=-1d).label("昨日"),.es(index=logstash*,metric=count).label("今日")
   
   .es(index=logstash*,metric=count,offset=-1d).label("昨日"),.es(index=logstash*,metric=count).label("今日").title("访问统计")
   
   .es(index=logstash*,metric=count,offset=-1d).label("昨日").lines(fill=1,width=0.5),.es(index=logstash*,metric=count).label("今日").title("访问统计")
   
   .es(index=logstash*,metric=count,offset=-1d).label("昨日").lines(fill=1,width=0.5).color(gray),.es(index=logstash*,metric=count).label("今日").title("访问统计")
   
   .es(index=logstash*,metric=count,offset=-1d).label("昨日").lines(fill=1,width=0.5).color(gray),.es(index=logstash*,metric=count).label("今日").title("访问统计").color(#1E90FF)
   
   .es(index=logstash*,metric=count,split=geo.src.keyword:3,)
   
   .es(index=logstash*,q="geo.src.keyword:CN",metric=count,split=machine.os.keyword:3,)
   
   .es(index=logstash*,metric=sum:bytes,offset=-1d).label("昨日"),.es(index=logstash*,metric=sum:bytes).label("今日")
   
   .es(index=logstash*,metric=sum:bytes,offset=-1d).label("昨日"),.es(index=logstash*,metric=sum:bytes).label("今日"),
   .static(1000000).label("告警线").color("red")
   
   .es(index=logstash*).label("请求计数")
   
   .es(index=logstash*).label("请求计数"),
   .es(index=logstash*,
   metric=sum:bytes).label("流量计数")
   
   (.es(index=logstash*).label("请求计数"),
   .es(index=logstash*,
   metric=sum:bytes).label("流量计数"))
   .range(0,10000)
   ```

##### 实时数据图表分析 & 课程总结  
1. 短视频数据解析入库 & 短视频数据分析项目实战

   ```markdown
   # 短视频数据分析项目实战
   nickname.txt
   tag.txt
   个性签名.txt
   handle_data.py

   索引模式: douyin_data*
   192.168.0.101:5601
   Management-> 索引模式 -> 创建索引模式 -> 定义索引模式 douyin_data* -> 配置设置 时间筛选字段名称 crawl_time-> 创建索引模式
   
   Discover
   时间:2020/07/01 07:59:20-2020/08/10 08:53:23 每日
   
   Visualize->新建可视化-垂直条形图->选择douyin_data*-2020/07/01 07:59:20-2020/08/10 08:53:23
   右边-数据-存储桶-X轴-聚合 Date Histogram-最小时间间隔 每日-字段crawl_time-更新
   每天数据抓取分布图
   
   Visualize->新建可视化-饼图->选择douyin_data*-2020/07/01 07:59:20-2020/08/10 08:53:23
   右边-数据-存储桶-拆分切片-聚合 Date Histogram-最小时间间隔 每年-字段birthday-更新
   右边-数据-存储桶-拆分切片-子聚合 词 -字段 gender-大小 5-更新
   gender=>birthday
   选项-饼图设置 圆环图
   年龄和性别分布饼图
   
   Visualize->新建可视化-标签云图->选择douyin_data*-2020/07/01 07:59:20-2020/08/10 08:53:23
   右边-数据-存储桶-标记-聚合 词 -字段 tag.keyword-大小 15-更新
   选项-方向 多个
   标签词云图
   
   Visualize->新建可视化->目标图->选择douyin_data*-2020/07/01 07:59:20-2020/08/10 08:53:23
   选项-范围 百分比模式关闭  0-10000 ... 添加范围 ... 100000-110000 -更新
   右边-数据-存储桶-拆分组-聚合 词 -字段 region.keyword-大小 5-更新
   按地区分布统计
   
   创建仪表板 抖音短视频数据分析(打开 将时间随仪表盘保存)-添加每天数据抓取分布图-添加年龄和性别分布饼图-添加标签词云图-添加按地区分布统计-添加ip和抓取数据分布
   
   # 短视频数据解析入库
   ubuntu远程虚拟环境搭建
   mitmdump_es.py
   
   ubuntu虚拟机与手机处于同一个网络
   1) ubuntu虚拟机 桥接网络
   2) 手机安装mitmproxy证书并信任 mitm.it  手机设置mitmproxy代理 192.168.0.110/[192.168.0.101 8889]
   
   mitmdump -s mitmdump_es.py -p 8889
   GET _cat/indices 
   启动刷新抖音 / 启动handle_douyin.py
   查看mitmdump是否有数据输出
   GET _cat/indices 查看是否有douyin_data_2020-08-09
   GET douyin_data_2020-08-09/_search{
   "query":{
   "match_all":{
   }
   }
   }
   在Kibana中进行数据分析(同上节)
   ```
   
2. 课程总结

   ```markdown
   什么是Uiautomator2
   Uiautomator2的通信流程
   u2自动化抓取环境的搭建
   u2连接移动设备三种方式
   
   定位元素方法
   weditor工具安装和使用
   实战-解锁移动设备九宫格
   实战-考研帮app登陆和滑动考研资讯
   
   Fiddler/mitmproxy抓包工具使用
   App无法抓包探秘
   
   通过u2实现滑动抖音短视频
   通过mitmproxy解析抖音短视频数据
   
   什么是atxserver2库
   实现多任务端app应用抓取系统
   
   ES安装和基本的增删改查
   ES查询进阶
   ES的mappings
   ES的分词
   ES的倒排索引
   通过Python对ES批量添加数据
   
   向ES导入示例数据
   Kibana的index-pattern
   Kibana的Discover
   ES的聚合分析
   Kibana的基本图形
   
   短视频数据解析入库
   实战-抖音短视频数据分析
   ```



















