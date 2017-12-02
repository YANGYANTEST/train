# python的表达式和语句
# 表达式：是一个或多个操作符组成的序列组成的
# 语句：用来实现生成操作，如循环访问，if判断等

"""
Python中常用的表达式操作符：
x*y,x/y,x+y,x-y,x//也,x%y，
逻辑运算：
x or y,x and y,not x

成员关系运算：
x in y，x not in y

对象实例测试：
x is y，x not is y

比较运算：
x<y,x>y,x<=y,x>=y,x==y,x|=y

位运算：
x|y ，x&y,x^y,x<<y,x>>y

一云运算：
-x , +x,~x

幂运算
x ** y

索引和切片：
x[i],x[i:j],x[i:j:stride]

调用：
x(....)

取属性：
x.attribute

元祖：()
序列：[]
字典：{}

三元选择表达式： x if y else z

匿名函数：lambda args:expression

生成器函数发送协议：yield x

运算优先级：
    (),[],{}
    s[i],s[i::]
    s.attribute
    s(...)函数调用
    +x，-x,~x
    x ** y
    * / // %
    <<,>>
    &
    ^
    |
    <  <=  > >=  ==  |=
    is,not is
    in,not in
    not
    and
    or
    lambda
"""
"""
语句：
    赋值语句
    函数调用
    print 打印对象
    if else elif判断
    for  else序列迭代
    while else 普通循环
    pass 占位符
    break
    continue
    def 函数
    return
    yield
    global 命名空间
    ralse：触发异常
    import
    from 模块属性访问
    class 类
    try/exccept/finally捕捉异常
    del 删除引用
    assert 断言
    with/as 环境管理器

"""
'''
赋值语句：
    隐式赋值：import from def class for 函数参数
    元祖和列表分解赋值：当赋值符号= 的左侧为元祖或列表时，python会按照位置把右边的对象和左边的目标自左而右
    逐一进行配对，个数不同时会触发异常，此时可以切片的方式进行；

    多重目标赋值

    增强赋值: +=  -= *= /= //= %=

'''
l1 = ('Sun', 'Sat', 'Mon')
(x, y, z) = l1
print(l1)
print(y)

a = 9
a += 1
print(a)

