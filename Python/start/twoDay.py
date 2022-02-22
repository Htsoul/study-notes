""" def ducn(a,b):
    c = a-b
    print(c)
ducn(30,70) """

""" def f1():
    a = 10
    def f2():
        nonlocal a
        a+1
        return a
    return f2
ret = f1()
a = ret()
print(a)
b = ret()
print(b) """

""" def func(a,b):
    return a + b
print(func(14,16)) """

""" def func(a,c=30,b):
    return a+b-c
print(func(10,20)) """

""" a = 18
print(bin(a))
print(oct(a))
print(hex(a)) """

""" lst = [48,12,39,101,32,48,24]
a = 10
b = 3
print(pow(a,b))
print(sum(lst))
print(max(a,b))
print(max(lst))
print(min(a,b))
print(min(lst)) """

""" a = '6789sds'
print(hash(a)) """

""" def fun():
    print('你好啊')

def daili(han):
    han()
res = daili(fun) """

""" a = 10
def func():
    global a
    a = 20
func()
print(a) """

""" def func():
    a = 10
    def func1():
        nonlocal a
        a = 20
    func1()
    print(a)
func() """

""" def func():
    a = 10
    def inner():
        print(a)
        return a
    return inner
ret = func()
ret() """


# 装饰器
""" def wapper(func):
    def inner(*args,**kwargs):
        ret =func(*args,**kwargs)
        return ret
    return inner() """

login_statu = False
""" 
def login_verify(fn):
    def inner(*args,**kwargs):
        global login_statu
        if login_statu == False:
            print('还未登录，请先登录！')
            while 1:
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
f3() """


