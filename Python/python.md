# `Python`

## `python`初体验

```python
print('hellow world')
```

`python`检测数据类型

```python
a = '12dsdfd'
print(type(a)) # 结果 str
```

## `python`中的条件与循环

### `if`条件语句

```python
a = int(input('请输入年龄'))
if a>18:
	print('你可以玩LOL')
elif a>10:
    print('你还要快快长大')
else:
    print('快去写作业吧')
# pass占位
if a>18:
	pass  #表示占位 没有任何操作
else:
    print('快去写作业吧')
```

### `while`循环语句

```python
i = 0
while i<=100:
    print(i)
    i = i+1
# 结果 0，1，2，3，4......98，99，100
```

### `for`循环语句

```python
a = [1,2,3,4,5,6,7,8,9]
for i in a:
    print(i) # 结果：1，2，3，4，5，6，7，8，9
    
# range(n) 从0数到n-1,n不可取
for i in range(10):
	print(i) # 结果 0，1，2，3......7，8，9
    
# range(n,m) 从n数到m-1,m不可取
for i in range(6,10):
    print(i) # 结果 6,7,8,9
    
# range(n,m,s) 从n数到m-1,每次间隔为s
for i in range(4,10,2):
    print(i) # 结果 4,6,8
```

## `python`的基础数据类型

### `python`的基础数据类型有:

```python
int
float
bool
str
list
tuple
set
dict
bytes
```

### `python`中的类型转换

```python
a = '10'
print(type(int(a))) # 结果 int
```

### `str`字符类型

#### 字符串格式化

```python
name = '周星驰'
another_name = '星爷'
age = 22
s0 = '我最喜欢的是%s，我喜欢他%s岁时的洒脱，人们都称他为%s' % (name,age,another_name)
s1 = '我最喜欢的是{}，我喜欢他{}岁时的洒脱，人们都称他为{}'.format(name,age,another_name)
s2 = f'我最喜欢的是{name}，我喜欢他{age}岁时的洒脱，人们都称他为{another_name}'
print(s0,s1,s2) # 结果 我最喜欢的是周星驰，我喜欢他22岁时的洒脱，人们都称他为星爷
```

#### 索引与切片

```python
s = '我喜欢周星驰'
#索引
print(s[3])# 结果 周
#切片
print(s[3:6])# 结果 周星驰
```

#### 常规操作

```python
#capitalize()方法可以将字符串首字母变成大写，但必须返回一个新的变量
s = 'python'
S = s.capitalize()
print(s,S) # 结果 python Python

#title()方法可以将字符串中单词的首字母都变成大写
s = 'May you go through mountains and rivers and still feel that the world is worth it'
print(s.title())# 结果 May You Go Through Mountains And Rivers And Still Feel That The World Is Worth It

#lower()方法将所有的字母都转换成小写
#upper()方法将所有的字母都转换成大写
s = 'Can I HElp yoU '
print(s.lower(),s.upper()) # 结果 can i help you    CAN I HELP YOU 

#len()方法匹配字符串的长度
s = 'dsfdsfsdf'
print(len(s)) # 结果 9

#join()方法连接字符
lst = ['java','nodejs','python','golang']
print('_'.join(lst)) # 结果 java_nodejs_python_golang

```

#### 切割和替换

```python
#strip()方法将字符串两端的空格删除
#replace()方法替换字符串中的内容
#split()方法按照提供的字符进行切割，用什么切割就会损失什么
s = '  nodejs_python_java_golang_php_c++'
sp = s.strip()
print(sp) # 结果 nodejs_python_java_golang_php_c++
print(sp.replace('ndoejs','node')) # 结果 node_python_java_golang_php_c++
print(sp.split('_')) # 结果 ['nodejs', 'python', 'java', 'golang', 'php', 'c++']
```

#### 查找和判断

```python
#find()方法可以查找字符串中的内容 返回值是当前字符的索引
#index()方法与find()一样，不同的是查找不到内容时，find()方法返回-1，而index()方法则会报错
s = '12-18k.14薪'
print(s.find('k')) # 结果 5
print(s.index('k')) # 结果 5

#startswith()方法匹配字符串的开头，不能为int类型
#endswith()方法匹配字符串的结尾
s = input('输入你的姓氏')
if s.startswith('马'):
    print('姓马')
else:
    print('不姓马') # 结果 姓马
```

### `list`列表类型

#### 列表的概念

在`python`中用`[]`表示列表，列表和字符串一样有索引和切片

```python
lst = [17,54,89,64,'wodiu']
print(lst[3]) # 结果 64
print(lst[1:4]) # 结果 [54，89，64]
print(lst[::-1]) # 结果 ['wodiu', 64, 89, 54, 17]

```

#### 列表中的`for`循环

```python
#列表中的for循环
lst = [17,54,89,64,'wodiu']
for i in lst:
    print(i) # 结果 17，54，89，64，wodiu
    
# 得到列表的长度
lst = [17,54,89,64,'wodiu']
print(len(lst)) # 结果 5
```

#### 列表的排序

```python
#sort()方法对列表进行升序的排序
#sort(reverse=True)对列表进行逆序的排序
lst = [44,55,77,12,8,32,12,75,46,98,482] # 里面的元素都是int类型
lst.sort()
print(lst)# 结果 [8, 12, 12, 32, 44, 46, 55, 75, 77, 98, 482]
lst.sort(reverse=True) 
print(lst)# 结果 [482, 98, 77, 75, 55, 46, 44, 32, 12, 12, 8]
```

#### 列表的增删改查

+ 列表的增加

```python
lst = list() # 创建一个空的列表
lst.append('wodiu') # 在列表中追加元素 只能追加一个
lst.insert(0,'老大') # 在列表索引为0的地方插入元素
lst.extend(['sds','dsd','sddsf']) #在列表中批量追加元素
print(lst) # 结果 ['老大', 'wodiu', 'sds', 'dsd', 'sddsf']
```

+ 列表的删除

```python
#pop()方法给出被删除的索引，返回删除的元素
lst = [17,54,89,64,'wodiu']
print(lst.pop(4)) # 结果 wodiu
#remove()删除列表中的元素
lst = [17,54,89,64,'wodiu']
lst.remove('wodiu')
print(lst) # 结果 [17, 54, 89, 64]
print(lst.remove('wodiu')) # 结果是None
```

+ 列表的修改

```python
lst = [17,54,89,64,'wodiu']
lst[4] = 45
print(lst) # 结果 [17, 54, 89, 64, 45]
```

+ 列表的查询

```python
# 直接用索引查询
lst = [17,54,89,64,'wodiu']
print(lst[4]) # 结果 wodiu
# 列表操作练习
lst = ['李大大','彭大大','周大大','王大大']
for i in range(len(lst)):
    item = lst[i]
    if item.startswith('王'):
      new_name = '杨'+item[1:]
      lst[i] = new_name
print(lst) # 结果 ['李大大', '彭大大', '周大大', '杨大大']

#列表嵌套
lst = ['wodiu','你是','我是',['你爹','他爹'],'byebyela']
print(lst[3][1]) # 结果 他爹

```

### `tuple`元组类型

在`python`中用`()`表示元组，元组和字符串一样有索引和切片，但是元组固定了某些数据，不允许外界修改

元组如果只有一个元素，需要在元素的后面加上**`,`**

```python
tup = ('hahh','你好啊',45,['wodiu','name','age'],'slery')
tup[3][0] = 'email'
print(tup) # 结果 ('hahh', '你好啊', 45, ['email', 'name', 'age'], 'slery')
```

### `set`集合类型

`set`集合里面的元素是无序的，所以没有索引和切片操作

```python
#集合的表示如下
s = {12,2,3,'fdsf'}
#向s集合中添加元素
s.add('ds')
```

### `dict`字典类型

字典是以键值对的形式存储数据的

字典的表示方式为`{key:value,key:value}`

#### 字典的增改

```python
#创建一个空字典，往里面添数据
dic = dict()
dic['name'] = 'wodiu'
dic['age'] = 18
print(dic) # 结果 {'name': 'wodiu', 'age': 18}
dic['name'] = 'meiko'
print(dic) # 结果 {'name': 'meiko', 'age': 18} 字典中已经有name,再次操作相当于修改
```

#### 字典的查询

```python
#方法一 直接通过key来查询
dic = {'name': 'meiko', 'age': 18}
print(dic['name']) # 结果 meiko 如果key不存在的话会直接报错

#方法二 get()方法中传入key来查询
dic = {'name': 'meiko', 'age': 18}
print(dic.get('age')) # 结果 18 如果key不存在的话返回None
```

#### 字典的删除

```python
#字典的是根据key来删除的
dic = {'name': 'wodiu', 'age': 18}
dic.pop('age')
print(dic) # 结果 {'age': 18}
```

#### 字典的循环和嵌套

```python
# 直接用for循环直接拿到key
dic = {'name': 'meiko', 'age': 18}
for key in dic:
    print(key,dic[key]) # 结果 name meiko age 18
print(list(dic.keys())) # 结果 ['name', 'age'] 把所有的key保存在列表中
print(list(dic.values())) # 结果 ['meiko', 18] 把所有的value保存在列表中

# 直接拿到key和values
dic = {'name': 'meiko', 'age': 18}
for item in dic.items():
    print(item) # 结果 ('name', 'meiko')('age', 18) 结果是元组类型
    
# 更多的是这种形式取字典的值
dic = {'name': 'meiko', 'age': 18}
for k, v in dic.items():
    print(k,v) # 结果 name meiko age 18
    
# 元组和列表都可以进行解包操作
a = 9
b = 4
a,b = (4,9) 
print(a,b) # 结果 4,9
```

### 字符集和编码

```python
# encode('编码')进行编码
# decode('编码')进行解吗
s = '周大大'
print(s.encode('utf-8')) # 结果 b'\xe5\x91\xa8\xe5\xa4\xa7\xe5\xa4\xa7'
s1 = b'\xe5\x91\xa8\xe5\xa4\xa7\xe5\xa4\xa7'
print(s1.decode('utf-8')) # 结果 周大大
```

### 运算符

```python
# 算数运算符
+, -, *, /, 

# 比较运算符
>, <, <=, >=, ==. !=

# 赋值运算符
=, +=, -=, *=

# 逻辑运算符
and, or, not # 优先级：括号>not>and>or

```

### 文件操作

**`open()`方法是打开一个 文件，里面的参数有**

`file`文件路劲   

`mode`表示操作 {

​					`r`:   读取

​					`w`:  写入

​					`rb`:   读取非文本文件

}

```python
f = open(file='my.text',mode='r',encoding='utf-8')
print(f.read()) # 结果 ............

# rendline()读取一行
for line in f:
    print(f.readline().strip()) # 结果 好好学习 byebye
f.close() # 关闭文件操作

f.write('dsdsdsad') # 文件写入方法
```

## 函数

在`python`中用`def`表示函数

```python
def func(a,b):
    return a + b
print(func(14,16)) # 结果 30
```

### 函数参数的概述

参数可以分为实参和形参

+ 实参: 实际在调用的时候传递的参数

```python
def func(a,d,c): # 形参
    return  a + b +c
print(func(30,10,70)) # 实参 

# 实参 也可以是函数,这种模式也称之为代理模式
def fun():
    print('你好啊')
def daili(han):
    han()
res = daili(fun) # 结果 你好啊
```

### 函数默认值

```python
def func(a,b,c=30):
    return a+b-c
print(func(10,20)) # 结果 0  
```

### 内置函数

```python
a = 18
print(bin(a)) # 结果 0b10010 转二进制
print(oct(a)) # 结果 0o22 转八进制
print(hex(a)) # 结果 0x12 转十六进制

lst = [48,12,39,101,32,48,24]
a = 10
b = 3
print(pow(a,b)) # 结果 1000
print(sum(lst)) # 结果 304
print(max(a,b)) # 结果 10
print(max(lst)) # 结果 101
print(min(a,b)) # 结果 3
print(min(lst)) # 结果 12

a = '6789sds'
print(hash(a)) # 结果 -8120130645636155114


```

### `global` `nonlocal`的使用

```python
# global在局部引入全局变量
a = 10
def func():
    global a
    a = 20
func()
print(a) # 结果 20

# nonlocal 在局部引入外层的局部变量
def func():
    a = 10
    def func1():
        nonlocal a
        a = 20
    func1()
    print(a) # 结果 20
func()
```

### 闭包

可以让一个局部变量常驻内存，可以避免全局变量被修改

```python
def func():
    a = 10
    def inner():
        print(a)
        return a
    return inner
ret = func()
ret() # 结果 10
```

### 装饰器

```python
# 基本装饰器写法步骤
def wapper(func):
    def inner(*args,**kwargs):
        ret =func(*args,**kwargs)
        return ret
    return inner()

```

```python
# 实战登录验证
login_statu = False 

def login_verify(fn):
    def inner(*args,**kwargs):
        global login_statu
        if login_statu == False:
            print('还未登录，请先登录！')
            while True:
                username = input('>>>')
                password = input('>>>')
                if username == "admin" and password == "123456":
                    print('登录成功')
                    login_statu = True
                    break
                else:
                    print('登录失败')
        
        ret = fn(*args,**kwargs)
        return ret
    return inner


@login_verify
def f1():
    print('修改信息')
    
@login_verify
def f2():
    print('增加信息')

@login_verify
def f3():
    print('删除信息')

f1()
f2()
f3()
```

### 迭代器

```python
# __iter__()方法是迭代器的标志
# __next__()方法逐一循环
s = '呵呵呵你妈地'
r = s.__iter__()
print(s.__iter__()) # 结果 <str_iterator object at 0x0000028FC9BAECE0>
print(r.__next__()) # 结果 呵
```

## 爬虫

### 爬取b站用户粉丝的用户名

```python
# 爬取b站粉丝的用户名
import requests

url = 'https://api.bilibili.com/x/relation/followers?vmid=420446594&pn=1&ps=20&order=desc'

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}

resp = requests.get(url,headers=headers)

data = dict(resp.json())
resp.close()
""" with open(file='data.json', mode='w', encoding='utf-8') as f:
    f.write(data)
    f.close() """

for i in data['data']['list']:
    print(i['uname'])
```

