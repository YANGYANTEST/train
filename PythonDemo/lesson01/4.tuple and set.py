"""
Python的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
"""

tuple=('1',1,'wo','666')
#tuple.pop()
#print(tuple) #报错
print(tuple[0])#截取第一个元素
print(tuple)#截取全部
print(tuple[-2])#截取倒序第二个元素
print(tuple[::2])#每隔2个元素截取

#元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下
tup1=('1','2','wo','come')
tup2=('h','i','e')
tup3=tup1+tup2
print(tup3)
#del(tup3)#报错，tup3没有定义
#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
print(len(tup3))#len()方法，计算元素个数
print(tup3*2)# *赋值tup3，不常用
print('1' in(tup3)) #	3 in(1, 2, 3) 判断元素是否存在，存在True，反之False



# 集合set()定义：由于set存储的是无序集合，所以我们无法通过索引来访问
# 访问set的某个元素实际上就是判断一个元素是否在set中
#判断一个元素是否在set中速度很快
#由于set也是一个集合，所以，遍历set和遍历list类型，都可以通过for循环实现

city=['sh','hk','bj','gz','hn']#定义一个列表
city_set=set(city)#定义一个set
print(city_set)
print('sh'in (city_set)) #判断sh元素是否存在city_set，存在True，反之False

#set()运算
baimao=set('baimao')
heimao=set('heimao')
print(baimao & heimao)#交集
print(baimao | heimao)#并集
print(baimao - heimao)#差集

# 列表如何去重？
#方法1:
list1=['a','b','c','d','e','a','b']
list2=[]
for element in list1:
    if not element in list2:
        list2.append(element)
print(list2)

# #方法2：
myset=set(list1)
print(list(myset))


