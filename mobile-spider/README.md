# python环境 (python3.11.1)
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

抖音数据抓取实战: appium+uiautomatorviewer

打造多任务端app应用数据抓取系统(2019版)
# docker连接夜神模拟器
启动android模拟器
adb devices
adb -s 127.0.0.1:62001 tcpip 5555 
docker exec -it appium1 adb devices
docker exec -it appium1 adb connect 192.168.0.104:5555
docker exec -it appium1 adb devices
docker exec -it appium1 bash
cd /var/log
tail -f appium.log
# 系统搭建步骤
1) 下载mongodb、appium、450120127/pythonv2镜像 docker pull 450120127/pythonv2
2) 设置docker toolbox网卡状态到桥接
3) 设置docker toolbox共享,挂载共享文件夹
4) 创建并启动相应容器
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
docker run -it -v /Users/bruce/workspace/mobile-spider/chapter07:/root/ --name python 450120127/pythonv2 /bin/bash
# 会话  mitmdump
docker images
docker run --rm -it -v /Users/bruce/workspace/mobile-spider/chapter07:/root/ -p 8889:8889 --name mitmdump 450120127/pythonv2 mitmdump -p 8889 -s /root/decode_data.py
# 会话 appium
docker run --privileged -d -p 4723:4723 --name appium_douyin appium/appium
docker run --privileged -d -p 4724:4723 --name appium_kuaishou appium/appium
docker run --privileged -d -p 4725:4723 --name appium_jrtt appium/appium
# 会话 mongodb
docker run -p 27017:27017 -v /Users/bruce/workspace/mobile-spider/chapter07:/root/ -d --name mongodb mongo
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
docker exec -it appium_douyin adb connect 192.168.0.102:5555
docker exec -it appium_kuaishou adb connect 192.168.0.104:5555
docker exec -it appium_jrtt adb connect 192.168.0.106:5555
# 会话 python
本地修改python文件,此会话python会同步修改
python handle_appium_docker.py
# 会话  mitmdump
# 会话 mongodb




















