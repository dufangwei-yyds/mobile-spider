#共享文件的挂载
sudo mount -t vboxsf 共享文件夹名称 目标目录
#创建python容器
docker run -it -v /home/docker/docker/:/root/ --name python 450120127/pythonv2 /bin/bash
#创建mitmproxy容器
docker run --rm -it -v /home/docker/docker/:/root/ -p 8889:8889 --name mitmdump 450120127/pythonv2 mitmdump -s /root/decode_data.py
#创建appium容器
docker run --privileged -d -p 4723:4723 --name appium_douyin appium/appium
docker run --privileged -d -p 4724:4723 --name appium_kuaishou appium/appium
docker run --privileged -d -p 4725:4723 --name appium_jrtt appium/appium
#
docker exec -it container-appium adb devices查看并启动adb服务
docker exec -it container-appium adb connect ip:5555来设置连接

#mongo容器
docker run -p 27017:27017 -v /home/docker/docker:/root/ -d --name mongodb mongo