'''

1.python中一切皆为对象
2.函数当作参数传递
3.理解函数式编程规范
4.匿名函数
5.高阶函数
'''

x=2
y=x=2
def run(a,b):
    print(a*b)

print(type(run))    #<class 'function'> function本身就是一个对象
print(run.__name__)     #__name__  函数名称

z=run   #函数当作对象------变量z
print(type(z))
print(run(1,2))
print("===================")
print(z(3,5))   #z---函数对象，进行传参


import random
def make_num():
    return random.randint(1,9)

def work(fun,num):  #fun第一个参数实函数对象，第二个是数值
    return fun()*num

result=work(make_num,6) #函数对象当作参数传递
print(result)


#有趣的函数 eval()可以转换为list，dict,set,等类型
print('3 * 3')
print(eval('1*9'))#eval() 打印出字符串的结果
print(type(eval('1*9')))


print("======================")
a_str='[1,2,34]'
print(eval(a_str))
print(type(eval(a_str)))    #list类型

b='{1:3,6:9}'
print(eval(b))

#print(eval("__import__('os).system('dir)"))     #字符串----执行一些指令

from ast import literal_eval
print(literal_eval('(11,33,55,22,55,22)'))  #安全

#zip函数-----内置函数（传递的序列数据类型）
print(list(zip([1,23,4],[5,7,9])))  #zip压缩对象，[(1, 5), (23, 7), (4, 9)] 得到的结果是0索引一起压缩

#如果以上序列里面元素不对应在该如何?
#压缩之后元祖项的个数有短板


#list------sort
#内置sorted
#反转rever
a=[1,2,3,4,5,6]
a.reverse()
print(a)

#递归函数   函数内部去调用函数的自身
def digui(num):
    if not isinstance(num,int):
        raise TypeError("传入的参数类型不是整数")
    if num==1 or num==0:
        return 1
    if num<0:
        raise ValueError("传入的参数不能小于0")
    return num *(digui(num-1))  #递归调用 n*(n-1)
result=digui(10)
print(result)

#递归函数，每调用一次函数，由于空间是有限的。不断增加。到最大极限报错

#高阶函数
class girl():
    def __init__(self,name,age):
        self.name=name
        self.age=age

nv=girl("lucy",22)
print(nv.name)


#函数式编程----编程范式----使用一系列的函数去解决问题（介于面向过程和面向对象之间）
#函数也是对象   函数当作参数传递
#函数式编程的特点：
'''
大量使用函数代替变量进行传递，更加富有逻辑简洁易用

'''

#匿名函数,只是使用一次，多次使用不建议使用
func=lambda x,y:x+y
num=func(2,3)
print(num)


#高阶函数 filter()函数 ,参数1：函数，参数2：序列对象
#作用：当前序列里面每一个元素传递进函数（参数1），返回的结果 True、False，返回true保留，false舍去

#定义函数1：
def fun():
    pass

#使用匿名函数2：filter()满足条件的保留，不满足的去除
f=filter(lambda x:x%2==0,[1,23,4,56,7])
print(type(f))
print(list(f))

#map()函数  参数1：函数对象    参数2：序列对象
m=map(int,['2','5','8'])    #返回map对象
print(list(m))

print(list(map(lambda x:x%2,[1,23,4,56,7])))

#reduce()----处理累计操作，不再是内置函数，返回不再是对象，一般是数值
from functools import reduce
print(reduce(lambda x,y:x+y,[1,23,4,5]))

#函数式编程  1代码更简洁    2数据集 操作，返回都放在一起   3没有写循环代码，减少了临时变量   4体现----要做什么而不是怎么去做 区别
