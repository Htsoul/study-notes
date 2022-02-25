# `linux-cli`

### `[admin@localhost /]$ ls`根目录下文件详解

+ `/dev`这个目录对所有用户都十分重要，因为在这个目录中包含了所有`Linux`系统中的外部设备，但是存放的并不是外部设备的驱动程序，这一点和`Windows`，`dos`操作系统不同，而是一个访问外部设备的端口/
+ `/bin`存放一些**常用命令**
+ `/etc`要存放了**系统配置**方面的文件
+ `/root`在`linux`下分为两种用户一种是root用户，一种是普通用户，在`root`用户下可以干任何事情
+ `/home`是用户**主目录**，或者是家目录
+ `/tmp`是**临时文档**，对于一些程序，有些文件被用了一次两次不会被用到，这样的文件就会存放在此处。有些`linux`系统会定期对这个目录的文件进行清理，所以一些重要文件不要存放在此处
+ `/lib`根文件系统上程序所需的**共享库**，存放了根文件系统运行时所需的共享文件，这些文件包含了可被许多程序共享的代码，以避免每个程序都有相同的子程序副本，可以使执行文件变得更小，节省空间
+ `/boot`包括了启动`linux`的**核心文件**。在最开始的启动阶段，通过引导程序将内核加载到内存，完成内核的启动（这个时候，虚拟文件 系统还不存在）加载的内核虽然是从硬盘读取的，但是没经过`linux`的虚拟文件系统，这是比较底层的东西来实现的。然后内核自己创建好虚拟文件系统，并且从虚拟文件系统的其他子目录中（如`/sbin`、`/etc`）加载需要在开机启动的其他程序或者服务或者特定的动作
+ `/opt`可择的文件目录。主机**额外安装软件**所摆放的目录。一些自定义软件包或者第三方工具可以安装在这里
+ `/mnt`临时挂载目录。这个目录一般用于存放**挂载储存设备**，比如光驱，磁盘，网络文件系统等，当我们需要挂载某个磁盘设备的时候，可以把吸盘设备挂载到这个目录上去，这样我们可以直接通过访问这个目录来访问该磁盘。一般可以在`mnt`下多建几个子目录，挂载的时候挂载到这些子目录上，因为通常我们可能会挂载很多设备
+ `/srv`存储系统提供的**服务数据**。
+ `/media`**挂载的媒体设备目录**，一般外部设备挂载到这里，例如`cdrom`等。比如我们插入一个U盘，我们会发现，`Linux`自动在这个目录下建立一个`disk`目录，然后把U盘挂载到这个disk目录上，通过访问这个`disk`来访问U盘
+ `/var`**存放不断变化的文件**。此目录下文件 的大小可能会改变，如缓冲文件，日志文件，缓存文件，计划性任务和邮件等
+ `/proc`**特殊文件目录**。这个本身是 一个**虚拟文件系统**，包含了全部虚拟文件。此目录的数据全部在内存中，如系统核心，外部设备，网络状态 ，行程资讯（`process`即进程，可以用`/process `查看进程信息）由于数据都存放在内存中，所以不占据磁盘空间
+ `/sys`**虚拟文件系统**：记录核心系统硬件信息。
+ `/usr`**这个目录中包含了命令库文件和在通常操作不会修改的文件**
  + `/usr/lib`:目标库文件，包括动态链接库加上一些通常不是直接调用的可执行文件的存放位置；
  + `/usr/bin`:用户和管理员的标准命令；
  + `/usr/sbin`:存放`root`超级用户使用的管理程序；
  + `/usr/include`:`C`程序语言编译使用的头文件。`linux`下开发和编译应用程序所需要的头文件一般都存放在这里，通过头文件来使用某些库函数。默认来说这个路径被添加到了环境变量中，这样编译开发程序的时候编译器会自动搜索这个路径，从中找到你的程序中可能包含的头文件；
  + `/usr/local`:安装本地程序的一般默认路径；
  + `/usr/share`:用于存放一些共享的数据；
  + `/usr/src:linux`开放的源代码；

### 添加用户和修改密码

+ 修改`root`用户密码

```shell
$ sudo passwd root
```

+ `root`用户修改普通账户的密码

```shell
$ passwd kali
```

+ 切换账户

```shell
$ su root
```

+ 删除指定账户及其用户文件

```shell
$ userdel kali -r
```

+ 创建用户 `-c`：指定一段注释性描述，`-d`：指定用户主目录，如果此目录不存在，则同时使用-m选项，可以创建主目录。`-g`：指定用户所属的用户组，

```shell
$ useradd -c admin -d /home/admin -m admin -g admin
```

+ 创建用户组

```shell
$ groupadd admin
```

### 更改镜像源

+ 更改镜像源

```shell
$ vi /etc/apt/sources.list
##阿里镜像源##
deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
##end##
$ wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add //清除缓存并更新源
$ apt-get clean && apt-get update -y
```

### 查看`ip`地址

```shell
$ ifconfig
```

```shell
[root@localhost admin]# ifconfig
docker0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        inet6 fe80::42:a6ff:fe94:e217  prefixlen 64  scopeid 0x20<link>
        ether 02:42:a6:94:e2:17  txqueuelen 0  (Ethernet)
        RX packets 67  bytes 8854 (8.6 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 106  bytes 19312 (18.8 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.234.132  netmask 255.255.255.0  broadcast 192.168.234.255
        inet6 fe80::614c:4fe:d186:4d19  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:46:cb:46  txqueuelen 1000  (Ethernet)
        RX packets 10221  bytes 9084698 (8.6 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4013  bytes 512174 (500.1 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 232  bytes 33828 (33.0 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 232  bytes 33828 (33.0 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

//ens33中的inet地址+端口号可以访问linux中开启的服务
```

### `linux`防火墙

+ 对外开放访问端口

```shell
$ firewall-cmd --add-port=8080/tcp --permanent
$ firewall-cmd --reload
```

+ 查看已经开放的端口

```shell
$ firewall-cmd --list-all
```

### `ssh`相关配置

需要linux中已经存在openssl软件

+ 查看`ssh`服务 状态信息

```shell
$ systemctl status sshd.service
//如果是active状态表示开启服务
```

+ 修改ssh配置 文件

```shell
$ vi /etc/ssh/sshd_config
//默认端口是22
```



