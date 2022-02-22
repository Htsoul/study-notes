# `Sql`学习

### `Sql`基础语句（增删改查）

+ 增加数据

```sql
INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....)
//增加一行数据
INSERT INTO `users` VALUES('wodiu',123456,'../upload/user-1.png')
//在指定的列中插入数据
INSERT INTO `users` (username, `password`) VALUES ('wodiu', 123456)
```

+ 删除数据

```sql
//删除某行数据
DELETE FROM `users` WHERE id = 1
//删除所有行但不删除表
DELETE FROM `users`
DELETE * FROM `users`
```

+ 更新数据

```sql
//更新某一行中的一个列
UPDATE `users` SET username='diuwo' WHERE id = 1
//更新某一行中的若干列
UPDATE `users` SET username='diuwo',`password`=654321 WHERE id =1
```

+ 查询数据

```sql
SELECT 列名称 FROM 表名称
//查询某一行的所有数据
SELECT * FROM `users` WHERE id = 1
//查询多个字段的数据
SELECT username,`password` From `users`
```

### `distinct`去重复

```SQL
SELECT DISTINCT username FROM `users`
```

### `AND` 和` OR `运算符

```SQL
//AND运算符实例
SELECT * FROM Persons WHERE FirstName='Thomas' AND LastName='Carter'
//OR运算符实例
SELECT * FROM Persons WHERE firstname='Thomas' OR lastname='Carter'
//结合AND和OR运算符
SELECT * FROM Persons WHERE (FirstName='Thomas' OR FirstName='William')
AND LastName='Carter'
```

### ` ORDER BY` 排序语句

```sql
//按照时间排序
SELECT username,avatar FROM `users` ORDER BY time
//按照时间逆序
SELECT username,avatar FROM `users` ORDER BY time DESC
```

### `Drop` 删除表

```sql
DROP table `user`  //删除某个表
```

