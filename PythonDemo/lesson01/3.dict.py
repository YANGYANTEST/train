#字典的定义：是一种可变容器模型，且可存储任意类型对象
#字典的每个键值(key==》value)对用冒号（：）分割，每个对之间用逗号（，）分割，整个字典包括在大括号中（｛｝）
#键必须是唯一的，但值不必，支
#值可以取任何数据类型，但键必须是不可变的。如字符串，数字或者元祖


dict={'name':'yangyan','age':22,'class':'First','score':[66,78,82,100]}
print("dict['name]:",dict['name'])
print(dict['age'])
print(dict.keys())
print(dict.values())
student=dict.copy()#复制dict
print(student)
print(student.get('name'))#get方法取key值
print(student.items())
#dict_items([('name', 'yangyan'), ('age', 22), ('class', 'First')])
print(dict['score'][2])#获取score键第三个元素的值


goods={'pro_date':20171031,
       'name':'weilong',
       'address':'shanghai',
       'NO':[17,36,53]
}
#1.打印所有的物品信息
# 2.获取他的生产批次 （第二次生产）
# 3.将物品信息拷贝一份存储在good2字典中
print(goods.items())
print(goods.values())
print(goods['NO'][1])
goods2=goods.copy()
print(goods2)


