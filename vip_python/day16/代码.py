'''

python修饰器

1.装饰器函数的演变过程
2.函数的嵌套
3.装饰器（被装饰函数带参数，装饰器本身）
4.

'''

# #函数也是对象
# def func(name):
#     print("%s is sleep "%name)
#
# def nake_fun():
#     func('yangyan')
#     print('快起来啦')
#     return 1
# nake_fun()  #第二个函数调用第一个函数
#
# f=func
# f('ben')


#函数之间的增加
# def func():
#     print("开始格式化数据")
#
# def work():
#     print("开始工作")
#
# def up_func(func):
#     print('开始备份数据')
#     func()
#     print('数据格式化完毕')
#     return func
#
# up_func(func)
# up_func(work)
# print("======================")
# b=func   #新执行，在返回fun对象
# b()       #调用fun()


#引入新的语法糖，将增强原有函数的功能，代码更加简洁优雅
#术语：计算机语言增加非常有趣的语法，这种语法对语言的功能没有影响，更加方便程序员去使用。提交程序的可读性 减少代码的出错

# def work(fun):      #第一个函数，装饰函数
#     print("备份")
#     fun()
#     print("完成")
#     return fun
#
# @work       #装饰器
# def fun():          #被装饰函数
#     print("格式化")
#     print("被装饰函数执行")
#
# print('============================')

#fun         #把参数当作对象传入装饰器中  被装饰函数名 ，当作参数传递到装饰函数work
#fun()       #调用fun（）函数



#被装饰函数执行了两次，怎么解决？？-----函数的嵌套

def outer(fun):     #外层函数
    def inner():        #内层函数  inner函数对象的引用放入内存里面
        print("备注")
        fun()
        print("完成")
    return inner


@outer
def func():
    print('格式化')


func()


#被修饰函数带有参数的情况?   内层函数传参数


# def outer(fun):
#     def inner(a,b):
#         print("开始计算")
#         z=fun(a,b)
#         print("返回结束")
#         return z
#     return inner
#
# @outer
# def work(x,y):      #原本函数，有参数
#     print("x+y=%d"%(x+y))
#     return x+y
#
# num=work(2,3)
# print(num)



#装饰器函数内层函数的形参（可变参数有什么好处）

def outer(fun):
    def inner(*args,**kwargs):
        print("开始计算")
        num=fun(*args,**kwargs)
        print("返回结束")
        return num  #内置函数的返回
    return inner    #外置函数的返回

@outer
def func(a,b):
    print("计算的结果为："%(a*b))
    return a*b


bb=func(2,3)
print(bb)















