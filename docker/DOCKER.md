# `   docker`

`docker`官网：https://www.docker.com

### `docker`的说明

+ 不同的应用程序可能会有不同的应用环境，比如`.net`开发的网站和`php`开发的网站依赖的软件就不一样，如果把他们依赖的软件都安装在一个服务器上就要调试很久，而且很麻烦，还会造成一些冲突。比如`IIS`和`Apache`访问端口冲突。这个时候你就要隔离`.net`开发的网站和`php`开发的网站。常规来讲，我们可以在服务器上创建不同的虚拟机在不同的虚拟机上放置不同的应用，但是虚拟机开销比较高。`docker`可以实现虚拟机隔离应用环境的功能，并且开销比虚拟机小，小就意味着省钱了。
+ 你开发软件的时候用的是`Ubuntu`，但是运维管理的都是`centos`，运维在把你的软件从开发环境转移到生产环境的时候就会遇到一些`Ubuntu`转`centos`的问题，比如：有个特殊版本的数据库，只有`Ubuntu`支持，`centos`不支持，在转移的过程当中运维就得想办法解决这样的问题。这时候要是有`docker`你就可以把开发环境直接封装转移给运维，运维直接部署你给他的`docker`就可以了。而且部署速度快。
+ 在服务器负载方面，如果你单独开一个虚拟机，那么虚拟机会占用空闲内存的，`docker`部署的话，这些内存就会利用起来。

### `docker`可以运行什么？

+ 可以在 `Docker` 里面运行数据库吗？当然可以。
+ 可以在 `Docker` 里面运行` Node.js` 网站服务器吗？当然可以。
+ 可以在 `Docker` 里面运行 `API `服务器吗？当然可以。

**Docker 并不在乎你的应用程序是什么、做什么，Docker 提供了一组应用打包、传输和部署的方法，以便你能更好地在容器内运行任何应用。**

### `docker`的安装

+ 安装下载`Docker`依赖的工具

```shell
$ sudo yum install -y yum-utils device-mapper-persistent-data lvm2
```

+ 添加阿里云的软件源

```shell
$ sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```

+ 更新yum缓存

```shell
$ sudo yum makecache fast
```

+ 安装`Docker`（`Docker`版本分为`CE`（社区免费版）和`EE`（企业版，安全`CE`）

```shell
$ sudo yum -y install docker-ce
```

### `docker`的启动

+ 启动`docker`服务

```shell
$ sudo systemctl start docker
```

+ 查看`Docker`是否成功

```shell
$ docker --version
```

+ 设置`docker`开机自启

```shell
$ sudo systemctl enable docker
```

### `Dockerfile`构建自定义容器

`Dockerfile` 是一个文本文档，其中包含组装 `Docker `映像的说明。当我们告诉 `Docker `通过执行`docker build` 命令来构建我们的镜像时，`Docker` 会读取这些指令并执行它们，并作为结果创建一个` Docker `镜像。

+ 在项目根目录下创建`.Dockerfile`文件

+ 构建镜像

```shell
#基础镜像，可以是多个  from
FROM node:16.14.0
#作者
MAINTAINER itsoul
#执行命令，创建文件夹
RUN mkdir -p /usr/src/workPlace_express/expressPro

#将dist目录拷贝到镜像里
COPY ./dist /usr/src/workPlace_express/expressPro/dist/
COPY package.json /usr/src/workPlace_express/expressPro
COPY server.js /usr/src/workPlace_express/expressPro

#指定工作目录
WORKDIR /usr/src/workPlace_express/expressPro

#安装依赖及构建node应用
RUN npm install --save
#配置环境变量
 ENV HOST 0.0.0.0
 ENV PORT 3333
#暴露端口
EXPOSE 3333
#运行程序命令
CMD ["node","app.js"]
```

+ 打包镜像

```shell
$ docker build -t node-test -f node-test.dockerfile . //-t 创建的镜像名  -f指定dockerfile文件
```

###  `Image` 命令

+ 查看全部`images`

```shell
$ docker images
```

+ 拉取一个镜像

```shell
$ docker pull <imageName> //拉取的是远程image
```

+ 删除指定的`image`

```shell
$ docker rmi image的id //也可以是name
```

+ 运行镜像

```shell
$ docker run -d images的id # 运行一个images
-d # 作为守护进程运行
-p 本地端口:docker内端口 # 端口映射
$ docker run -d -p 3000:3000 --name nodeTest node-test  //name or id
```

+ 镜像导出到本地

```shell
$ docker save 镜像id > 本地文件.tar
# 例如：
# docker save f95adbdaa41c > handless_firefox.tar
```

+ 本地导入到`docker`镜像

```shell
$ docker load < 本地文件.tar
# 例如：
# docker load < handless_firefox.tar

```

### `container`命令

+ 显示正在运行的docker

```shell
$ docker ps  //查看当前正在运行的容器
$ docker ps -a  //查看所有容器
```

+ 重启容器

```shell
$ docker start 容器ID
```

+ 停止运行容器

```shell
$ docker stop 容器id # 停止一个docker
```

+ 删除容器

```shell
$ docker rm 容器ID1 容器ID2 容器ID3
```

+ 从本机传输文件到docker容器内部

```shell
$ docker cp 本地内容 容器id://usr/....路径
# 例：docker cp index.html 17adwicm13ji://usr/share
```

+ 从docker容器传输到本机

```shell
$ docker cp 容器id:容器文件路径 本机路径
```

+ 保存容器修改，由于docker在容器内的改动都是暂时的

```shell
$ docker commit -m '备注' 容器id 自定义的repository名称 
# 例：docker commit -m 'test' 17adwicm13ji TestName
```

+ 检查容器信息

```shell
$ docker inspect 容器ID/IMAGE
```

+ 进入容器内部并打开命令行

```shell
$ docker exec -it 容器ID /bin/bash
# 例：docker exec -it f107a3df2958 /bin/bash 
```

+ 重命名容器

```shell
$ docker rename 原容器名  新容器名
```

### `docker`开启`mysql`服务

+ 下载`mysql`镜像

```shell
$ docker pull mysql//下载的是最新版本的mysql
```

+ 创建`mysql`容器

```shell
$ docker run -itd --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql
//--name 给容器指定一个名字
//-e MYSQL_ROOT_PASSWORD=root 配置mysql，用户名root,密码root
```

+ 查看运行的容器

```shell
$ docker ps
```

### `docker`开启`redis`服务

+ 下载`redis`镜像

```shell
$ docker pull redis:6
```

+ 下载`redis`配置文件并修改

```shell
$ wget http://download.redis.io/redis-stable/redis.conf

$ vi /usr/redis/conf/redis.conf

//修改一下内容
bind 127.0.0.1 #注释掉这部分，这是限制redis只能本地访问

protected-mode no #默认yes，开启保护模式，限制为本地访问

daemonize no#默认no，改为yes意为以守护进程方式启动，可后台运行，除非kill进程，改为yes会使配置文件方式启动redis失败

databases 16 #数据库个数（可选）

dir ./ #输入本地redis数据库存放文件夹（可选）

appendonly yes #redis持久化（可选）

requirepass z123456 #登录密码
```

+ 运行`redis`

```shell
$ docker run --name=myredis -d -p 6379:6379 -v /usr/redis/conf:/etc/redis/redis.conf -v /usr/redis/data:/data f1b6973564e9 redis-server /etc/redis/redis.conf --requirepass "z123456"
```

### `docker`开启`mongodb`服务

+ 下载`mongo`镜像

```shell
$ docker pull mongo
```

+ 运行镜像并挂载数据卷

```shell
$ docker run -d --name=mymongo -p 27017:27017 -v /usr/local/mongo:/data/db  5285cb69ea55
```

+ 从`mongo`容器中传输文件到宿主机

```shell
$ docker cp fd71dbe0e1ef:/etc/mongod.conf.orig /usr/local/mongo/conf/
```

### 开放了端口号但是远程还是不能访问

```shell
$ iptables -I INPUT -p tcp --dport 6379 -j ACCEPT
```

