### 移动端爬虫环境部署

python版本: python3.10.6

1. 虚拟环境搭建
   
   pip3 install virtualenv==20.0.23 -i https://pypi.douban.com/simple
   
   mkdir mobile-spider
   
   python3 -m virtualenv venv
   
   source venv/bin/activate

3. 更新pip版本
   
   python3 -m pip install --upgrade pip

5. pip安装uiautomator2、Appium-Python-Client、weditor、mitmproxy、elasticsearch以及uiautomator2初始化
   
   pip3 install uiautomator2 -i https://pypi.douban.com/simple
   
   python3 -m uiautomator2 init 

   pip3 install Appium-Python-Client -i https://pypi.douban.com/simple
   
   pip3 install weditor -i https://pypi.tuna.tsinghua.edu.cn/simple/
   
   pip3 install mitmproxy -i https://pypi.tuna.tsinghua.edu.cn/simple/
   
   pip3 install pymongo -i https://pypi.tuna.tsinghua.edu.cn/simple/
   
   pip3 install elasticsearch==7.7.0 -i https://pypi.douban.com/simple
