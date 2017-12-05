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
print(callable(123))    #
# print(callable(max))
# print(callable(  ))

def func():
    pass
func()
print(callable(func))


#slice()函数：切片
print([22,34,54][slice(0,1)])
print(range(12)[slice(1,12,1)])