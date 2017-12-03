
'''
pythom 函数
1、为什么要使用函数
2、函数怎么定义？
3、函数怎么调用？，
4、函数的返回值
5、函数的参数（普通参数、默认函数、关键字函数、动态收集函数）
6、匿名函数
'''

# for num in range(1,10):
#     print(num)

#有个任务有20步
#代码的封装---------提高了代码的复用性
# def fun():
#     pass

#def定义函数----代码块里面什么都不做，用pass

'''
python2x与python3的区别？
python3参数不能传入元祖形式；python2 可以
'''
def make(a,b,c):
    pass
print(make(1,2,3))


# func()   ()函数的调用符
#调用：getUserA()        get_user_age()

def func(a,b):
    x=a+1
    y=b+110
    return x,y  #这多个值自动打包进元祖
print(func(9,1))

#特殊情况
def func(a,b,c):
    return a *2,b+4,c*3
x,y,z=func(1,2,3)
print(func(1,2,3))

#函数的参数：首先判断数据的类型
def get_num(num):
    if not isinstance(num,(int,float)):#isinstance内置：第一个参数是否是第二个参数同种类型或者子类型
        raise TypeError("参数类型不对")  #异常处理
    if isinstance(num,float):
        return abs(round(num))    #abs()取绝对值
    if isinstance(num,int):
        if num<0:
            return abs(num)
        else:
            return num
print(get_num(-2.36))

#全局变量和局部变量
def func():
    num=20
    print(num)
func()# num=20

#默认参数：有默认参数，不传参数的话就是默认参数，若传参，则覆盖默认参数
def  get_name(x,y=20):
    return x+y
print(get_num(1))

#参数陷进：
def make_list(s=[]):
    print(id(s))
    s.append('ben')
    return s
print(make_list([1,2,3]))
print(make_list([4,5,6]))

#再看这种情况
print(make_list())      #6749760  ['ben']
print(make_list())      #同上      ['ben','ben']
#默认参数要注意：可变对象的问题？


#关键字参数，用在函数的调用
def func(x,y=1,z=4):
    return x*y*z
func(z=21,y=4,x=22) #关键字参数调用的函数参数的顺序更加灵活

#动态收集函数
def say_hello(massage,*name_list):  #会把多余的参数搜集进()元祖
    for name in  name_list:
        print(massage,name)
say_hello('你好吗','tom','jim','yang')

#一个星号：收集到元祖里面
def get_age(*age):
    print(type(age))
    num=0
    for i in age:
        num+=i
    print(num)
get_age(1)
get_age(1,34,2,13,5,6)

#两个星号:收集参数放dict
def func(**kwargs):
    print(type(kwargs))
    if 'name' in kwargs:
        print('有name参数')
    if  'age' in kwargs:
        print('有age参数')
func(name='ben',age=26,addr='北京')   #调用参数就不固定

a_dict={'name':'ben','age':22,'sex':'boy'}
func(**a_dict)  #传递定义好的字典

#匿名函数(没有名字的函数),没有标识符（函数名），使用场景：仅仅只是用一次（要用多次就普通的函数）
#python定义匿名函数：lambda表达式
lambda x,y:x+y  #lambda表达式
print((lambda x,y:x+y)(4,5))    #冒号之前为参数，冒号之后为结果

func=lambda x,y:x+y #把lambda表达式赋值给func对象，对象可以多次使用，所以可以多次打印
print(func(2,4))
print(func(5,7))





