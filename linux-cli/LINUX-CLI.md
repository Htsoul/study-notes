# `linux-cli`

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

