'''
本章小结：
1.dict字典数据类型
2.set集合数据类型
3.dict/set的区别
'''

#dict字典数据类型  key（唯一性,不可改变）-----value（）
#map的数据类型:key  value(映射类型)
#容器数据类型


dog_dict={'name':'小黄狗','age':20,'sex':'boy'}
print(dog_dict.keys())
print(dog_dict.values())
print(dog_dict['name'])
print(dog_dict['age'])


#遍历所有的数据项：
for item in dog_dict.items(): #items---所有的项
    print(item)
#key关键字的遍历（属性名）
for key in dog_dict.keys(): #key---获取所有的属性名
    print(key)

#value的遍历（）
for value in dog_dict.values():
    print(value)


#判断指定的key是否存在字典中
print('age'in dog_dict)
print(dog_dict.__contains__('name'))#__containe__  包含

#字典其他操作
#dog_dict.pop('name')#移除key关键字
#print(dog_dict)
#dog_dict.popitem()  #不需要参数：随机删除一个数据项
#print(dog_dict)


#构建字典的一个新方法：
a_dict=dict.fromkeys([1,2,3],'goods')
print(a_dict)


#更新和修改字典
dog_dict['name']='tom' #修改/添加。如果存在则代表修改，若没有表达添加
print(dog_dict)

#修改方法2：
a=dog_dict.setdefault('name','jim')
print(a)
print(dog_dict)

#字典的更新方法  update
dog_dict={'name':'jim','age':2}
aa={1,'hes',3.14}
dog_dict.update(aa)
print(dog_dict)
print(aa)


#set集合数据类型：没有value，元素是不能重复，不可修改、

#   不可改变集合
num_set=frozenset({1,2,4,5})        #frozenset-----不可改变的set
print(type(num_set))












