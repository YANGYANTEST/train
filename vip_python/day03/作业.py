



#1.在你的command line中打印输出:看看会发生什么？
#print('\\\n\\')  #运行后正显示为两个"\"-----\ 换行 \
#print('!!!!!!!!!')
#print(r'\\\n\\\') #运行后出错，r原始字符串把最后一单引号当做了字符串，导致这个字符内少了一个单引号结束
#print('\\\t\\') #运行后正显示
#print('!!!!!!!!!!!')
#print(r'\\\t\\') #运行后正显示

#2.实现字符串大小写反转的功能

#3.实现字符串倒序,比如输入ben,输出neb

#4.需求：
#content = '   my name is ben   '
#分别去掉左边,右边,两端空格
#将content去掉两端空格后与',my age is 19'拼接
#分别用index查找'my'和用find查找'name'
#判断'my'是否存在于content;然后判断't'是否存在
#将content首先转换大写,然后转换为小写,最后标题化
#截取索引从4开始到结尾的字符子串
#讲content按空格切分


#用':'连接[1,2,3]



print('Ben'.swapcase())

a_str = 'ben'
print(a_str[::-1])


content = '   my name is ben   '
print(content.lstrip())
print(content.rstrip())
print(content.strip())
print(content.strip()+',my age is 19')
print(content.index('my'))
print(content.find('name'))
print('t' in content)
print(content.upper())
print(content.lower())
print(content.title())
print(content[4:20])
print(content.split(' '))



print(','.join(['1','2','3']))






#list
#tuple
#list与tuple对比
#切片



#list数据类型------->列表
#name_list =['ben','q','Alina']
#print(name_list)

#name_list = list('list')
#print(name_list)



#list------->len()      #内置函数
#name_list =[1,'ben',3.14]
#print(len(name_list))


#索引的概念    （从0索引开始）---->
#name_list =[1,'ben',3.14]
#print(name_list[1])

#问题：会不会出现问题------>索引越界的问题
#name_list=[1,'ben',3.14]
#print(name_list[5])

#取最后一个元素
#name_list = [1,'ben',3.14]
#print(name_list[len(name_list)-1])
#这种方式取最后一个元素不科学



#python负索引
#name_list = [1,'ben',3.14]
#print(name_list[-1])


#定义好list之后，又想改变容器里面的元素
#list追加方法------->往最后添加
#name_list = [1,'ben',3.14]
#name_list.append(3+4j)
#print(name_list)


#在第一个和第二个元素之间添加元素
#name_list = [1,'ben',3.14]
#---------->insert插入方法，（插到任意地方）
#name_list = [1,'ben',3.14]
#name_list.insert(1,'Alina')  #给第二个参数，第一个参数位置，第二个参数插入的元素对象

#删除元素
#末尾的元素删除掉(没有参数）
#name_list
#name_list.pop()
#name_list.pop
#print(name_list.pop())      #pop返回的值
#print(name_list)

#有参数  pop()------->可以有参，可以无参
#name_list = [1,'ben',3.14]


