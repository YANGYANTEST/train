#列表生成器
def get_squra(max_value):
    my_list=[]
    for x in range(1,max_value):
        my_list.append(x * x)
    return  my_list
print(get_squra(5))


my_list=[x * x for x in range(1,5)]
print(my_list)

#for循环后加if判断，筛选出结果
my_list=[x * x for x in range(1,10) if x%2==0]
print(my_list)


#还可以使用两层循环，可以生成全排列
my_list=[m+n for m in 'ABC' for n in 'XYZ']
print(my_list)


#求下列代码的输出结果(面试题)
mylist=[108,20,78,14,8,2,5,3,11]
result=[x for x in mylist[::2]if x%2==0]
print(result)
"""
这是一个列表生成式，主要考列表生成式是否理解？
列表切片 if for
此题是个基础题
"""
#等价
mylist=[108,20,78,14,8,2,5,3,11]
result=[]
for x in mylist[::2]:
    if x%2==0:
        result.append(x)
print(result)

#列表去重
lista=[2,3,4,2,5,3]
listb=[]
[listb.append(a) for a in lista if a not in listb]
print(listb)

