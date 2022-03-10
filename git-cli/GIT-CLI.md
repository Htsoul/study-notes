# `git-cli`

### 初始化仓库，添加提交

```shell
$ git init //初始化本地仓库

$ git add . //将内容添加到暂存区

$ git commit -m 'update ...' //将暂存区的内容提交到本地仓库
```

### 拉取仓库

```shell
$ git clone https://github.com.... //拉取远程仓库到本地新建仓库

$ git feth https://github.com... //将远程主机的最新内容拉到本地，用户在检查了以后决定是否合并到工作本机分支中

$ git fetch <远程主机名> <分支名> //只想取回特定分支的更新，可以指定分支名

$ git fetch origin master //取回origin 主机的master 分支

$ git pull https://github.com... //是将远程主机的最新内容拉下来后直接合并,git pull = git fetch + git merge
```

### `branch`分支

```shell
$ git branch //查看本地分支

$ git branch -r //查看远程所有分支
//推出按q

$ git branch dev //本地创建dev分支

$ git chechout dev //切换到dev分支

$ git checkout source/common  //切换不同仓库的分支

$ git checkout -b test //创建一个test分支并切换到该分支上

$ git branch -d <branchname> //删除本地分支

$ git branch -d -r <branchname> //删除远程分支，删除后还需推送到服务器

$ git push origin:<branchname>  //删除后推送至服务器

$ git branch -m <oldbranch> <newbranch> //重命名本地分支

$ git branch --unset-upstream master //取消对master的跟踪
```

### 关联远程仓库

```shell
$ git remote add origin/source https://github.com //将本地仓库与远程仓库关联
```

### `push`上传修改

```shell
$ git remote -v //查看远程所有关联的仓库

$ git push -u origin master //将本地的master分支推送到origin主机，同时指定origin为默认主机，后面就可以不加任何参数使用git push了

$ git push origin //将当前分支推送到origin主机的对应分支

```

### 版本回退

```shell
$ git reset --merge  //回退到merge之前 
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

### 综合

+ 情景一查看冲突

```shell
$ git diff server/api/controllers/reportController.js
diff --cc server/api/controllers/reportController.js
index df2c4d2c,af7e326a..00000000
--- a/server/api/controllers/reportController.js
+++ b/server/api/controllers/reportController.js
```

解决办法

```shell
$ git commit -am "fix: update reportController sms"
[master-common-5G 7a38b8af] fix: update reportController sms
```

### 设置全局环境

```shell
$ git config --global user.email "xxx.gamil.com"

$ git config --global user.name "xxx"
```

### 代理

+ 不开启代理

```shell
$ git config --global --unset https.proxy
```

+ 开启代理

```shell
$ git config --global https.proxy http://127.0.0.1:9090
```

### 生成`ssh`密钥

```shell
$ ssh-keygen -t rsa -C "xxx.gmail.com"  //rsa

$ ssh-keygen -t ed25519 -C "xxx@gmail.com"  //ed25519

$ cat ~/.ssh/id.xxx.pub
```

### `git-fork`一般流程

1. `fork`主仓库
2. 拉取远程仓库代码

```shell
$ git clone git@52.80.155.217:haiyang.zhou/LiveCenterServer.git
```

3. 关联主仓库

```shell
$ git remote add source http://gitlab.54.12.30.68
```

4. 切换至主仓库的`master`分支

```shell
$ git checkout source/master
```

5. 在主仓库下新建分支`test`

```shell
$ git checkout -b test
```

6. 修改内容
7. `push`到远程仓库

```shell
$ git push origin test
```

8. 在`gitlab`客户端进行`merge request`操作

### `merge`合并时出现冲突

**原因**：主要是因为不同的人对同一文件同一区域进行了修改，需要手动解决冲突

```shell
$ git pull source master-common
From http://52.80.155.217:8100/QuickView/LiveCenterServer
 * branch              master-common -> FETCH_HEAD
Auto-merging config/development.js
CONFLICT (content): Merge conflict in config/development.js
Auto-merging config/production.js
CONFLICT (content): Merge conflict in config/production.js
Auto-merging config/test.js
CONFLICT (content): Merge conflict in config/test.js
Auto-merging serve.js
Auto-merging server/api/controllers/agents.js
CONFLICT (content): Merge conflict in server/api/controllers/agents.js
Auto-merging server/api/controllers/auth.js
CONFLICT (content): Merge conflict in server/api/controllers/auth.js
Auto-merging server/api/controllers/screenCapture.js
CONFLICT (content): Merge conflict in server/api/controllers/screenCapture.js
Auto-merging server/api/controllers/serviceRequests.js
CONFLICT (content): Merge conflict in server/api/controllers/serviceRequests.js
Auto-merging server/api/controllers/statistics.js
CONFLICT (content): Merge conflict in server/api/controllers/statistics.js
Auto-merging server/api/helpers/agentStatus.js
CONFLICT (content): Merge conflict in server/api/helpers/agentStatus.js
diff --cc config/development.js
index 1baa8011,8c1e70a9..00000000
--- a/config/development.js
+++ b/config/development.js
@@@ -6,20 -9,137 +9,146 @@@ module.exports =
      MAIN_SERVER: true,
      customerUrl: 'https://livecenter-h5-test.ikandy.cn/#/',
      s3StaticUrl: 'https://s3.cn-north-1.amazonaws.com.cn/',
:...skipping...
diff --cc config/development.js
index 1baa8011,8c1e70a9..00000000
--- a/config/development.js
+++ b/config/development.js
@@@ -6,20 -9,137 +9,146 @@@ module.exports = 
      MAIN_SERVER: true,
      customerUrl: 'https://livecenter-h5-test.ikandy.cn/#/',
      s3StaticUrl: 'https://s3.cn-north-1.amazonaws.com.cn/',
+     celeryBrokerUrl: 'amqp://txt:itxtrabbit@118.89.172.110:5674/txt_host',
+     celeryResultBackEnd: 'amqp://txt:itxtrabbit@118.89.172.110:5674/txt_host',
      jwtsecret: 'txtechnology',
+     captcha: {
+         appId: "6be4cdaed176efb4bbc6843f6381a56e",
+         appKey: "f7e325a108e7e944051f29a2968cd313"
+     },
+     fsServer: {
+         api: 'http://52.83.100.228:4396/',
+         sip: {
+             "sipServer": "139.159.212.84:5060",
+             "username": "8889043",
+             "password": "1qaz!QAZ"
```

