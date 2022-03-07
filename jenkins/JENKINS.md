# `jenkins`

### `linux`上安装`gitlab`服务

+ 安装依赖项

```shell
$ yum install policycoreutils openssh-server openssh-clients postfix
```

+ 设置`postfix`开机自启，并启动，`postfix`支持`gitlab`发信功能

```shell
$ systemctl enable postfix && systemctl start postfix
```

+ 下载rpm包并安装

```shell
$ wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/gitlab-ce-11.6.10-ce.0.el7.x86_64.rpm
 
$ rpm -i gitlab-ce-11.6.10-ce.0.el7.x86_64.rpm
```

+ 开放`ssh`和`http`服务，然后重新加载防火墙列表

```shell
$ firewall-cmd --add-service=ssh --permanent

$ firewall-cmd --add-service=http --permanent
```

+ 修改`gitlab`配置文件指定服务器`ip`和自定义端口

```shell
$ vim  /etc/gitlab/gitlab.rb
```

+ 重置并启动`gitLab`

```shell
$ gitlab-ctl reconfigure
 
$ gitlab-ctl restart
```

### 安装`jenkins`

```shell
$ wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo

$ rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key

$ yum install -y jenkins
```

### 修改`jenkins`配置文件

```shell
$ vi /etc/sysconfig/jenkins
```

### 启动`jenkins`服务

```shell
$ service jenkins start
```

### 进入`jenkins`首页

在浏览器端输入**`http://192.168.234.133:8080`**即可进入首页

**`192.168.234.133`对应的是虚拟主机上的`ip`地址**

### 查看`jenkins`的初始默认密码

```shell
$ cat /var/lib/jenkins/secrets/initialAdminPassword
```

### 安装插件

登录成功之后会进入到安装插件的步骤

### 系统管理配置

在系统管理中找到配置安全策略，采用安全矩阵

