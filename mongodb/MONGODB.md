# `mongodb`

### 学习网站

+ `mongodb`官网：https://www.mongodb.com/
+ 菜鸟教程：https://www.runoob.com/mongodb/mongodb-tutorial.html

### `mongodb`开启服务

```shell
$ mongod //先输入该命令
$ mongo //再输入此命令
```

### `mongodb` 开启认证状态

```shell
$ cd /user/local/mongodb/bin/ //进入到该文件下
$ cat mongodb.cfg //查看此文件有没有开启认证状态
//如果开启状态则应该有该字段
auth=true
//没有则输入该内容开启
```

###  `mongodb`开启用户名和密码认证

+ 创建管理员

```shell
$ use admin //切入到管理员
$ show users //如果没有任何内容则表示没有用户
$ db.createUser({user:"zhy",pwd:"z123456",roles:["root"]}) //创建超级用户
$ show users //结果如下
#{
        "_id" : "admin.zhy",
        "userId" : UUID("53f0db85-0dac-4ffd-a088-1f19c168877d"),
        "user" : "zhy",
        "db" : "admin",
        "roles" : [
                {
                        "role" : "root",
                        "db" : "admin"
                }
        ],
        "mechanisms" : [
                "SCRAM-SHA-1",
                "SCRAM-SHA-256"
        ]
}#
```

+ 创建普通用户

```shell
$ use admin //切入到管理员
$ db.createUser({user:"test",pwd:"test",roles:[{role:"readWrite",db:"test"}]}) //读写权限
$ show users //结果如下
#Successfully added user: {
	"user" : "test",
	"roles" : [
		{
			"role" : "readWrite",
			"db" : "test"
		}
	]
}#

```

### `mongoose`操作`mongodb`

+ 连接`mongodb`

```javascript
const init = async() => {
    mongoose.connect('mongodb://127.0.0.1:27017/test', {useNewUrlParser:true}, (err)=>{
    if(!err){//连接成功了
       console.log('database connect success');
    }else{
       throw err;
    }
 })
}
init();
```

### 存储数据步骤：

**定义`Schema` (骨架) > 创建`model`（模型）> `Entity`实例化方法** 

+ 定义`Schema` (骨架)

```javascript
const Schema = mongoose.Schema;
const studentsSchema = new Schema({
   name: String,
   age: Number,
   sex: String,
   birthday: Date
});
```

+ 创建`model`（模型）

```javascript
const studentsModel = mongoose.model('students', studentsSchema);
```

+ `Entity`实例化

```javascript
const studentsInstance = new studentsModel();
```

### 数据的增删改查

+ 增加数据

```javascript
//数据的存储
studentsInstance.name = 'ksjjsj';
studentsInstance.age = 50;
studentsInstance.sex = 'man';
studentsInstance.save((err) => {
    if (!err) { //存储成功
        console.log('data save success')
    } else {
        throw err
    }
});
```

+ 修改数据

```javascript
//修改数据
studentsModel.find({ name: 'lcj' }, (err, res) => {
    if (!err) { //查找成功
        const id = res[0]._id;
        studentsModel.findById(id, (err, docs) => {
            docs.age = 18,
                docs.save((err) => {
                    if (!err) {
                        console.log('data update success')
                    } else {
                        throw err
                    }
                })
        })
    } else {
        throw err;
    }
});
```

+ 查询数据

```javascript
//查找数据
studentsModel.find({ age: 50 }, (err, result) => {
    if (!err) { //查找成功
        console.log('data find success');
        console.log(result);
    } else {
        throw err;
    }
});
```

+ 删除数据

```javascript
//删除数据
studentsModel.find({ age: 50 }, (err, result) => {
    if (!err) { //查找成功
        const id = result[0]._id;
        studentsModel.findById(id, (err, docs) => {
            if (!err) { //删除成功
                docs.remove(() => {
                    console.log('data delete success');
                })
            }
        })
    } else {
        throw err;
    }
});
```

