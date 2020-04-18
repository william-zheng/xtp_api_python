# Linux下boost.python3库编译说明

## 1. 环境准备

* Linux
* python3.6.5(tar.gz)
* gcc (4.8.5版本)
* boost 1.66.0 (tar.gz)

### 1.1、安装 PYTHON

https://www.python.org/downloads/source/下载python3，（可选其他版本）

![下载Python](https://github.com/william-zheng/xtp_api_python/raw/master/doc/image/build_boost_python_linux_01.png)

存放/home/likunliang/目录下(可选)，
```sh
# 解压
tar -xvf Python-3.6.5.tar.gz
cd /home/likunliang/Python-3.6.5 
# 编译 
./configure --prefix=/usr/local/python3
```

安装先`make` 然后再`make install` 。
创建版本软连接，如有python2等其他版本，可先修改旧版本的软连接

```sh
mv /usr/bin/python /usr/bin/python_bak 
```

创建新的软连接 

```sh
ln -s /usr/local/python3/bin/python3 /usr/bin/python
```

检查python的版本 

```
python -V
```

显示：python-3.6.5

软连接创建成功 。


### 1.2、下载 BOOST 源码

进入官网 http://www.boost.org/，选择最新的版本，这里是1.66.0版本 
下载完成之后，解压

![下载boost](https://github.com/william-zheng/xtp_api_python/raw/master/doc/image/build_boost_python_linux_02.png)

## 2、boost的编译

将boost_1_66_0.tar.gz解压至/home/likunliang/目录下，

```
cd /home/likunliang/boost_1_66_0
./bootstrap.sh --with-python=/usr/local/python3
./b2 --toolset=gcc-4.8.5  --with-python include="/usr/local/python3/include/python3.6m/" --with-thread --with-date_time  --with-chrono
```
（说明：--with-python 里面的python需要是python3版本，通过include参数指定自定义版本的python包含路径）
在boost目录下会生成`stage`文件夹，里面的lib就是C++所需的python3的lib文件。至此boost.python3库编译完成。

![查看结果](https://github.com/william-zheng/xtp_api_python/raw/master/doc/image/build_boost_python_linux_03.png)

![查看结果](https://github.com/william-zheng/xtp_api_python/raw/master/doc/image/build_boost_python_linux_04.png)
