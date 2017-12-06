#python的内置函数
#1.和数学计算相关的内置函数
# from xx import aa #不属于内置函数

print(abs(-9))   #abs()取绝对值
print(max(1,45,59,8))    #max()取最大值
print(max(1,23,45,3))   # tuple
print(max([1,2,4,5]))   #list
print(max('a','b','c')) #字符串
print(max(['a','b','c']))

print(len("python!"))

print(2**3)
print(pow(2,3)) #pow()，乘方函数,参数可以为3个


print(pow(2,3,2))   #三个参数，返回0  （2**3）%2-----余数为0

print(list(range(9)))   #包左不包右

print(divmod(8,2))  #返回元祖    divmod（除法，（商，余数））

print(round(3.1415926))      #四舍五入


#2.类型转换的内置函数
#复数（3+4j） 实部+虚部（基本不用）

print(complex(2,3))     #返回复数， 实部+虚部
print(tuple(range(5)))
print(dict(name="yangyan",age=22))
print(bool(4))      #0----False 1--------true

#单个字符和整数之间的转换
# print(ord('s'))        #字符转换成整数
# print(chr(97))          #互逆过程

#callable()函数,判断参数是否可以调用
print(callable(123))    #False
# print(callable(max))
# print(callable(  ))

def func():
    pass
func()
print(callable(func))
print(False+2)

#slice()函数：切片
print([22,34,54][slice(0,1)])
print(range(12)[slice(1,12,1)])

#进制转换
print(oct(20))      #十进制---》八进制
print(bin(20))      #十进制----二进制
print(hex(889))    #十进制----十六进制


#序列操作
print(all(['2'," ",'alina']))
# print(all(False,True,'ben',12))
#print(any(1,3)) #只要有一个为True

#scort函数 scorted函数


#反转函数：
#print(list(reversed(1,2,3,4)))


#面向对象
class Myclass():
    def run(self):
        print("开始跑步")
    def eat(self):
        print("eating")
    def dog_run(self):
        print("小狗跑了")

t=Myclass()
print(hasattr(t,'run'))
print(hasattr(t,'name'))
func=getattr(t,'run')
func()

print(getattr(t,'name','0'))    #第三个参数：默认值（找不到的时候返回0）

print(setattr(t,'name','yang'))


#类型判断,返回TURE huo False
print(isinstance(12,int))
print(issubclass(Myclass,object))

#其他内置函数
print(str(1+3))
print(type(str))
print(repr('1+3'))      #repr函数----面向解释器
print(eval('1+4'))      #eval----计算字符串表达式的值


#compile()函数：字符串编译----字节代码，作用：提高了执行的效率
# code=compile("print(’ben‘)",'','exec')
# eval(code)
#第一个参数：字符串（指令）
#第二个参数：代码文件的名称，‘’（不是从文件获取）
#第三个参数：编译执行代码的关系


code=compile("open('print.py','a',encoding='utf-8').write(’12222‘)",'print.py')
eval(code)




我的名字我的名字我的名字我的名字