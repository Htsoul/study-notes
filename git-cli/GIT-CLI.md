# `git-cli`

```shell
$ git clone https://github.com.... //拉取远程仓库到本地新建仓库
$ git feth https://github.com... //将远程主机的最新内容拉到本地，用户在检查了以后决定是否合并到工作本机分支中
$ git fetch <远程主机名> <分支名> //只想取回特定分支的更新，可以指定分支名
$ git fetch origin master //取回origin 主机的master 分支
$ git pull https://github.com... //是将远程主机的最新内容拉下来后直接合并,git pull = git fetch + git merge
$ git init //初始化本地仓库
$ git add . //将内容添加到暂存区
$ git commit -m 'update ...' //将暂存区的内容提交到本地仓库
$ git remote add origin https://github.com //将本地仓库与远程仓库关联
$ git branch //查看本地分支
$ git branch -r //查看远程所有分支
$ git branch dev //本地创建dev分支
$ git chechout dev //切换到dev分支
$ git checkout -b test //创建一个test分支并切换到该分支上
$ git branch -d <branchname> //删除本地分支
$ git branch -d -r <branchname> //删除远程分支，删除后还需推送到服务器
$ git push origin:<branchname>  //删除后推送至服务器
$ git branch -m <oldbranch> <newbranch> //重命名本地分支
$ git push -u origin master //将本地的master分支推送到origin主机，同时指定origin为默认主机，后面就可以不加任何参数使用git push了
$ git push origin //将当前分支推送到origin主机的对应分支
$ git branch --unset-upstream master //取消对master的跟踪
```

+ 开发分支`（dev）`上的代码达到上线的标准后，要合并到 `master` 分支

```shell
git checkout dev
git pull
git checkout master
git merge dev
git push -u origin master
```

+ 当`master`代码改动了，需要更新开发分支`（dev）`上的代码

```shell
git checkout master 
git pull 
git checkout dev
git merge master 
git push -u origin dev
```

+ 设置全局环境

```shell
$ git config --global user.email "xxx.gamil.com"
$ git config --global user.name "xxx"
```

+ 不开启代理

```shell
$ git config --global --unset https.proxy
```

+ 开启代理

```shell
$ git config --global https.proxy http://127.0.0.1:9090
```

+ `git`生成`ssh`密钥

```shell
$ ssh-keygen -t rsa -C "xxx.gmail.com"  //rsa
$ ssh-keygen -t ed25519 -C "xxx@gmail.com"  //ed25519
$ cat ~/.ssh/id.xxx.pub
```

