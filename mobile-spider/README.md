# python环境部署 (python3.10.6)
pip3 install virtualenv==20.0.23 -i https://pypi.douban.com/simple
mkdir mobile-spider
python3 -m virtualenv venv
source venv/bin/activate

python3 -m pip install --upgrade pip
pip3 install uiautomator2 -i https://pypi.douban.com/simple
pip3 install Appium-Python-Client -i https://pypi.douban.com/simple
python -m uiautomator2 init 
pip3 install weditor -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip3 install mitmproxy -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip3 install pymongo -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install elasticsearch==7.7.0 -i https://pypi.douban.com/simple























