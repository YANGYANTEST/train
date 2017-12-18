'''
第一题 写一个函数计算1+3+5+9+....97的结果，再写一个装饰器函数，对其装饰，
在运算前，新建一个文件然后结算结果，最后把计算的结果写入到文件中

'''
def outer(fun):
    def inner():
        file=open('yan.py','w',encoding='utf-8')
        result=fun()
        file.write(str(result))
        file.close()
    return inner
@outer
def count():
    return sum(range(1,100,2))
count()


'''
第二题：写一个函数计算传入进来参数的平方，并将结果，写一个带参数的装饰器，将装饰器参数传入被包装的函数
'''

def work(args):
    def outer(fun):
        def inner(*kw):
            print('开始计算')
            a=fun(args)
            print("结束")
            return a
        return inner
    return outer

@work(6)
def func(num):
    if isinstance(num,int):
        return  pow(num,2)
    else:
        print("传入的参数不是整数")

num=func(8)
print(num)
