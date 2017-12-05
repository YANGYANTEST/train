'''
元祖，列表：用[]括起来
'''
list=['Google','baidu',1773]
print(list)

#更新值,没有索引，强制赋值会报错
list[1]=['a','b','c']
print(list)

#删除列表
del list[2]
print(list)

#其他操作
print(len(list))
print('a' in list)

#嵌套列表
a=['a','b','c']
b=[1,2,3]
c=[a,b]
print(c,len(c),c[0],c[0][1])

# a=[1,2,3,4,5,[122,33,44,66,111]]
# print(min(a))

#作业：求出最大值最小值
list2=[1,2,3,45]
list3=[1,2,3,[4,5,6]]
list4=['ww',3,5]
print("min",min(list2),"max",max(list2))
print(min(list3[3]))
print(max(list3[3]))
#print(min(list4),max(list4))#报错




