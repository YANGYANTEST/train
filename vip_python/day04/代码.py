'''
list：列表
tuple:元祖
list与tuple：列表和元祖
切片
'''

#list数据类型(列表数据类型)
#索引的概念（从0索引开始）
name_list=['ben','a','王菲']
print(name_list[2])

name=list('python')
print(name)
print(len(name))
print(name[1])

#问题:会不会出现问题？索引越界的问题
name_list=[1,'ben',3.14]
print(name_list[len(name_list)-1])#这种方式取最后一个元素不科学
print(name_list[2])
print(name_list[-1])#负索引

#定义好list之后，又想去改变容器里面的元素，怎么操作？
#list追加方法------往最后添加元素
name=[1,'ben',3.14]
name.append('python')#在元素上最后添加元素。append()
print(name)

#我只是在第一个元素和第二个元素之间添加元素，insert(a,b)，第一个参数位置，第二个参数插入元素的对象
name.insert(1,'hi')
print(name)

#删除元素：pop()函数，可有参数。可没有
name.pop()
print(name)
name.pop(1)
print(name
)


#删除指定元素：remove函数
name.remove('ben')
print(name)

#替换元素
name=[1,'ben',3.14]
name[1]='sindy'
print(name)

# 嵌套
name[2]=[1,2,3]
print(name)

#清空元素
age=[1,2,3]
age.clear()
print(age)

#tuple元祖：用(),不能插入/删除，不能重新赋值（里面的值都不能改变）可以用索引，但不能越界
name_tuple=(1,2,3)
print(len(name_tuple))
print()

#tuple特殊的地方：如果当前元祖里面只有一个元素?必须加逗号，
age_tuple=(21,)#一个元素的时候，加逗号，不加逗号就是整数类型
print(age_tuple)
print(type(age_tuple))

#不能重新赋值（里面的值都不能改变）
# name_tuple=(1,2,3)
# name_tuple[-1]=32
# print(name_tuple)

#如果tuple没有元素
name_tuple=()
print(type(name_tuple))


#list和tuple非常相似
#列表内的值可以改变，tuple不可改变，内部嵌套的list内部还是可以改变的
age_tuple=(18,20,33,[44,55])
age_tuple[3][1]=88
print(age_tuple)


'''
list和tuple的区别
相同点:
1.都是序列数据类型
2.容器里面的元素都是有索引概念
3.迭代（对象）-----for item in 对象：此时的对象就是可迭代的
4.元素的类型可以不相同
5.都支持负索引
6.支持切片
7.获取元素的速度接近一个恒定值

不同点：
list-----定义之后还可以改变；tuple定义好之后里面的元素不可改变
list---学这个就够了

list和tuple--------for item in 对象：
name_tuple=(1,2,3)
for name in name_tuple:
    print(name)

'''

name_tuple=(1,2,3)#容器
for name in name_tuple:
    print(name)

#一个新的内置函数：enumerate()函数：每一次循环遍历每一个元素的时候，给每一个元素产生一个新的索引
name=('小黑','小胖子','地瓜','小明')
for index,name in enumerate(name):
    print(index,name)

num_list=[1,2,3]
print(num_list[::-1])
num_list.reverse()#倒序排列
print(num_list)

#sorted()排序，ed表示有返回值
#区别：sort---list（没有返回值），sorted()内置方法，不是list方法，有返回值
num_list.sort(reverse=False)#
print(num_list)

num_list=[1,2,3]
new_list=sorted(num_list,reverse=True)#sorted()排序，ed表示有返回值
print(num_list)
print(new_list)


num_list=[1,2,3,4,5,6,7,8,9]
print(num_list[0:2])    #从谁，到谁结束（包左不包右）
print(num_list[::]) #全部
print(num_list[1:6:2])  #三个参数，前面两个是从谁开始都谁结束（包左不包右），最后一个参数表示步长
print(num_list[:7:-1])  #