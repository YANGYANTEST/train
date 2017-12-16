'''
生成器和迭代器
理解可迭代对象，迭代器，生成器对象
列表推导式。生成器表达式
切片的高级用法
'''

#range函数()
print(type(range(1,9)))
print(range(-9))#0 / -9
print(list(range(-9)))  #空列表[]

#可迭代对象
for i in range(9):  #range(9)可迭代对象，
    print(i)
print("===================================")

from collections import Iterable    #可迭代对象
a_str='ben'
b_list=[1,2,3]
c_tuple=(4,5,6)
d_dict={'name':'ben','age':20}

if isinstance(a_str,Iterable):
    print('a_str是可迭代对象')
if isinstance(b_list,Iterable):
    print('b_list是可迭代对象')
if isinstance(c_tuple,Iterable):
    print('c_tuple是可迭代对象')
if isinstance(d_dict,Iterable):
    print('d_dict是可迭代对象')

print("===================================")

#第一个内置函数
# d_dict={'name':'ben','age':20}
# for key,value in d_dict.items():
#     print(key+':'+value)

#第二个参数-----起始角标
for index,item in enumerate([1,2,3],4): #添加一个索引属值----每一个运势取角标
    print(index,item)
print("==================================")

#列表推导式--------返回结果肯定是[]
a_list=range(1,11)      #内置类型转换函数
print(a_list)

print([x*2 for x in range(1,9)])

print([x-1 for x in range(2,10)if x>2])
print([x+y for x in range(1,9) if x%2==0 for y in range(1,9)if y%2!=0])
print("=====================================")

#迭代器,相当于一个容器，每次取出一个数值
#可迭代对象
# from collections import Iterable,Iterator
# a_iter=iter([1,2,3,4,5])
# print(type(a_iter))
# print(isinstance(a_iter,Iterator))  #判断a_iter是不是迭代器对象 返回true False
# print(next(a_iter))
# print(next(a_iter))
# print(next(a_iter))
# print(next(a_iter))

# for item in a_iter:     #迭代器建议使用for循环，因为超出范围的话不会报错，for循环判断容里面的元素
#     print(item)

#自定义迭代器对象：必须满足迭代器协议：__next__(每一次取迭代器元素)   __iter__()
class MakeIter():
    def __init__(self,id):
        self.id=id
    def __next__(self):
        if self.id ==0:
            raise StopIteration("已经没有元素了")
        self.id -=1
        return self.id
    def __iter__(self):
        return self
a_iter=MakeIter(9)
# print(next(a_iter))   #比较麻烦，不建议使用，使用for循环
for num in a_iter:
    print(num)

#切片 第一个参数开始，第二个参数结束，第三个代表步长，负数 从后往前切
num_list=[1,2,3,4,5,6,7,8,9]
print(num_list[1::-1])

#生成器----列表推导式
b_gen=(x for x in range(5))     #方式1
print(type(b_gen))  #generator生成器   生成器对象也属于一种迭代器

#内存的优化 next
print(next(b_gen))

for num in b_gen:
    print(num)

#方式2
def mk_gen(num):
    while num>3:
        yield num       #关键字 + def()-----》生成器yield
        num-=1
m_gen=mk_gen(6)
print(type(m_gen))  #generator生成器对象
for num in m_gen:
    print(num)
    print("代码暂停")