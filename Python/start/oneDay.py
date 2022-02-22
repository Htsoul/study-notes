""" a = 10
print(a) """

""" a = int(input('请输入你的年龄'))
print('你的年龄是', a) """

""" a = int(input('请输入你的money'))
if a>800:
    print('足浴')
elif a>400:
    print('吃大餐')
else:
    print('回家吧阿') """

""" a = [1,4,5,7,9,2,6]
for i in a:
    print(i) """

""" i = 0
s = 0
while i<=100:
    print(i)
    i = i+1 """

""" a = '10'
print(type(int(a))) """

""" name = '周星驰'
another_name = '星爷'
age = 22
s0 = '我最喜欢的是%s，我喜欢他%s岁时的洒脱，人们都称他为%s' % (name,age,another_name)
s1 = '我最喜欢的是{}，我喜欢他{}岁时的洒脱，人们都称他为{}'.format(name,age,another_name)
s2 = f'我最喜欢的是{name}，我喜欢他{age}岁时的洒脱，人们都称他为{another_name}'
print(s0,s1,s2)
 """

""" s = '我喜欢周星驰'
print(s[3])
print(s[3:6]) """

""" s = 'python'
S = s.capitalize()
print(s,S) """

""" s = 'May you go through mountains and rivers and still feel that the world is worth it'
print(s.title()) """

""" s = 'Can I HElp yoU '
print(s.lower(),s.upper()) """

""" s = '  nodejs_python_java_golang_php_c++'
sp = s.strip()
print(sp)
print(sp.replace('ndoejs','node'))
print(sp.split('_')) """

""" s = '12-18k.14薪'
print(s.find('k'))
print(s.index('k')) """

""" s = input('输入你的姓氏')
if s.startswith('马'):
    print('姓马')
else:
    print('不姓马') """

""" s = 'dsfdsfsdf'
print(len(s)) """

""" lst = ['java','nodejs','python','golang']
print('_'.join(lst)) """

""" lst = [17,54,89,64,'wodiu']
print(lst[3])
print(lst[1:4])
print(lst[::-1]) """

""" lst = [17,54,89,64,'wodiu']
for i in lst:
    print(i) """

""" lst = [17,54,89,64,'wodiu']
print(len(lst)) """

""" lst = list() # 创建一个空的列表
lst.append('wodiu') # 在列表中追加元素 只能追加一个
lst.insert(0,'老大') # 在列表索引为0的地方插入元素
lst.extend(['sds','dsd','sddsf']) #在列表中批量追加元素
print(lst) """

""" lst = [17,54,89,64,'wodiu']
print(lst.pop(4)) # 结果 wodiu """

""" lst = [17,54,89,64,'wodiu']
lst.remove('wodiu')
print(lst) """

""" lst = [17,54,89,64,'wodiu']
lst[4] = 45
print(lst) # 结果  """

""" lst = ['李大大','彭大大','周大大','王大大']
for i in range(len(lst)):
    item = lst[i]
    if item.startswith('王'):
      new_name = '杨'+item[1:]
      lst[i] = new_name
print(lst) """

""" lst = [44,55,77,12,8,32,12,75,46,98,482]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst) """

""" lst = ['wodiu','你是','我是',['你爹','他爹'],'byebyela']

print(lst[3][0]) """

""" tup = ('hahh','你好啊',45,['wodiu','name','age'],'slery')
tup[3][0] = 'email'
print(tup) """

""" dic = {'node':'20xin'}
print(type(dic)) """

""" dic = dict()
dic['name'] = 'wodiu'
dic['age'] = 18
print(dic) """

""" dic = {'name': 'wodiu', 'age': 18}
dic.pop('age')
print(dic)
 """

""" dic = {'name': 'meiko', 'age': 18}
print(dic['name']) """

""" dic = {'name': 'meiko', 'age': 18}
print(dic.get('age')) """


""" dic = {'name': 'meiko', 'age': 18}
for key in dic:
    print(key,dic[key])
print(list(dic.keys()))
print(list(dic.values())) """

""" a = 9
b = 4
a,b = (4,9) # 结果 
print(a,b) """

""" dic = {'name': 'meiko', 'age': 18}
for item in dic.items():
    print(item) """

""" dic = {'name': 'meiko', 'age': 18}
for k, v in dic.items():
    print(k,v) """

""" s = '周大大'
print(s.encode('utf-8'))
s1 = b'\xe5\x91\xa8\xe5\xa4\xa7\xe5\xa4\xa7'
print(s1.decode('utf-8')) """
""" 
f = open(file='my.text',mode='r',encoding='utf-8')
print(f.read())
for line in f:
    print(f.readline().strip()) """

""" lst = [4,7,8,[9,7,5,3]]
f = open(file='my.json',mode='w',encoding='utf-8')
f.writable(lst)
print(f.read()) """

""" s = '呵呵呵你妈地'
r = s.__iter__()
print(s.__iter__())
print(r.__next__()) """