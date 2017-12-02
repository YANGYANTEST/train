"""
list列表（定义、访问、切片、连接、内置函数）
list是一种有序的集合，可以随时添加和删除其中的元素，
list元素是按照顺序排列的。通常直接用[]把list的所有元素括起来。
eg：list=[a,123,helloword]

列表的访问
student=['张三'，'王二'，'李四']
print(student[-2])
print(student[1])
print(student[3])
"""
student=['张三','王二','李四']
print(student[-2])
print(student[0])
print(student[2])

student=[['张三','王二','李四'],["zhangsan",'wanger','lisi']]
print(student[0][0])
print(type(student[1]))


#列表切片
#截取列表的一部分
distrit=['jingan','wangpu','putuo','zhabei','minhang']
print(distrit[3])#截取第四个字符串
print(distrit[2:5])#截取2-5个字符串
print(distrit[1:])#截取1后面所有的元素
#截取全部
print(distrit[:])
print(distrit[2:-2])
#截取步长
print(distrit[::2])#每隔2个
print(distrit[::-3])#倒序，每隔3个


#列表添加元素
# apppend()方法，把新元素追到list的末尾
List1=[1,2,3,4,5,5]
List1.append(8) #插入一个元素
print(List1) #位置在末尾
print(List1.index(8))#第五个元素


# 列表添加元素
# insert()方法：它接受两个参数，第一个参数是索引号，第二个参数是待添加的新元素
# 将元素添加到原来索引为x的位置，以及后面的所有元素，都自动向后移动一位
L=['linda','sunny','lucy','allen']
L.insert(2,'Bob')
print(L)
#打出结果：['linda', 'sunny', 'Bob', 'lucy', 'allen']


#列表元素的删除
# pop()方法是删除list的最后一个元素，且它还返回这个元素
L=['linda','sunny','lucy','allen']
L.pop()#删除最后一个元素
print(L)

#列表删除元素  del()
L=['linda','sunny','lucy','allen']
del(L[1])#删除第一个元素
print(L)

#列表元素更新，对list中的某一个索引赋值，就可以直接新的元素天花成原来的元素，list包含的元素个素不变
A=['shanghai','hunan','anhui','beijing','guangzhou']
A[2]='hefei'#更新第三个元素
print(A)

#列表函数和方法
"""
函数：
len(list) 列表元素个数
max(list)  返回列表元素最大值
min(list)  返回列表元素最小值
list(seq)  将元组转换为列表

方法：
list.append(obj)  在列表末尾添加新的对象
list.count(obj)   统计某个元素在列表中出现的次数
list.extend(seq)  在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）	
list.index(obj)   从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj)  将对象插入列表
list.pop(obj=list[-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)  移除列表中某个值的第一个匹配项	
list.reverse()    反向列表中元素
list.sort([func]) 对原列表进行排序
list.clear()  清空列表
list.copy()  复制列表
"""

var=[1,2,3,'taobao','baidu',2,'taobao']
print(var.count('taobao'))

r='hello'
list4=['w','a',2,'e']
result=list4.extend(list4)
print(list4)


