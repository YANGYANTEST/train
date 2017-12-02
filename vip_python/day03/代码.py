
'''
1.编码问题
2.字符串常用内置函数
'''

#pyhton3里面字符串在内存中统一表现为unicode编码

'''
#ASCII编码：英文字母 数字 一些字符 一共127个字符(全部一个字节表示)
1个字符------2的8次方   256
'''

'''
为了解决乱码：
UNICODE编码：解决出现乱码的问题（全世界所有语言一些字符都包含进来）
是2-4个字节（16-32位），最少2个字节，unicode编码是文本字符串在内存中的内在形式
'''

#又出现问题？是不是觉得有点浪费空间？

'''
utf-8编码：在项目里面都是用utf-8编码
好处：
utf-8编码表-----unicode编码表的基础之上做的优化
肯定解决了乱码-----优化：节省了空间（能够用一个字节表式的就用一个字符，不能用1个字符就用多个字符表示）
'''

'''
gbk编码：
python2：
print (len('哈哈'))  输出6
print (len(u'哈哈'))  输出2

python3:只有unicode编码
'''
#编码和解码:
'''
在计算机内存中统一使用unicode编码？

把内存中文本字符串----写入到文件里面或者网络上传播
python3里面的编码和解码：
encode：把unicode-------字节流数据（bytes） #0110
decode：把字节流数据还原为unicode（）
'''
#如下（endode/decode转换）
print('我是奥巴马'.encode('utf-8'))
print(b'\xe6\x88\x91\xe6\x98\xaf\xe5\xa5\xa5\xe5\xb7\xb4\xe9\xa9\xac'.decode('utf-8'))

#byte字节数据
num_byte=bytes([1,2,3]) #内置
print(num_byte)


num_bytes=bytes('ben','ascii')
print(num_bytes)

str='hello word'
print(type(str))

#编码过程
b=str.encode(encoding='utf-8')
print(b)

#解码过程
c=b.decode(encoding='utf-8')
print(c)


#本节重点内容：
'''
python字符串常用的内置函数：
1   ord函数   chr函数：字符---整数的转换
2   len函数：打印元素的长度
3   strip函数:字符串去空格和特殊字符;   
4   字符串连接操作： + *
5   替换操作：  replace('原值'，'替换值' )
6   字符串查找  index()函数,find()函数    
    find 查找 index---find，保证代码的健壮性，index找不到元素会报错，find不会
7   字符串的比较：>=,<=,>,<,==,!=, in ,not in
8   lower()函数:转换成小写； 
    upper():转换成大写
9   大小写之间的转换： swapcase()函数：大写换成小写；小写换成大写
10  首字母大写: capitalize()函数;首字母改成大写
11  标题化字符串:title()：将每个标题进行大写转换
12  print(a_str[::-1])  #将python进行反过来输出
13  字符串的切割：split(),切割返回一个列表
14  join字符串的拼接  join()函数
15  对齐  ljust()：左对齐  rjust()；右对齐  center() 中间对其
16  以字符开头/结束  startswith()函数:判断以什么开头   
                      endswith()函数:判断以什么结束,都是返回False/True类型
                        
17  判断元素是什么类型组合: isalnum()函数：数字或字符  
                            isalphs():全部是字符  
                            isdigit()函数：全部是数字，返回的都是False/True
18  判断是否全部是小写 islower()函数
19  判断是否全部是大写  isupper()函数
20  统计某个字符或者数字出现的次数 count()函数
21  右对齐  zfill()函数，填充 拉伸 不够的步0





'''
#ord函数   chr函数：字符---整数的转换
print(ord('A')) #单个字符---整数转换的过程
print(chr(65))  #整数----单个字符转换的过程

#len函数
print(len('abcd'))
print(len("我是小日本的他爹"))

#如果是一个中文字符，经过utf-8编码之后会占用三个字符
print(len('今天晚上小树林见'.encode('utf-8')))


#字符串的赋值操作
str='ben'
a_str=str
str='yangyan'
print(str)
print(a_str)

#切片
a_str='my name is ben'
print(a_str[1])
print(a_str[-2])
print(a_str[1:3])


#字符串去空格和特殊字符;   strip()函数

a_str='   my name is ben   '
print(a_str.lstrip())   #去掉左边的空格
print(a_str.rstrip())   #去掉右边的空格
print(a_str.strip())    #去掉两端的空格

b_str='.ben,'
print(b_str.lstrip('.').rstrip(','))
print(b_str.rstrip(','))

b='.@ben#!*'
print(b.lstrip('.@').rstrip('#!*'))
print(b.strip('.@#!*'))

#字符串连接操作： + *
print('ben'+' is good boy')
print('ben '*3)
print(('ben'+'hot')*2)

#替换操作：  replace('原值'，'替换值' )
a_str='my name is ben'
b_str=a_str.replace('name','age')
print(b_str)

#字符串查找  index()函数,find()函数
a_str='my name is ben'
print(a_str.index('ben'))
print(a_str.find('ben'))

#find 查找 index---find，保证代码的健壮性，index找不到元素会报错，find不会
#print(a_str.index('python'))
print(a_str.find('python'))

#字符串的比较：>=,<=,>,<,==,!=, in ,not in
print('abc'>'cdas')   #输出False
print('ao'not in 'adc')     #输出True

#字符串大小写的转换： lower()函数:转换成小写； upper():转换成大写
print('Sindy'.lower())
print('sindy'.upper())

#大小写之间的转换： swapcase()函数：大写换成小写；小写换成大写
print('Sindy'.swapcase())

#首字母大写: capitalize()函数;首字母改成大写
print('sinDy'.capitalize())

#标题化字符串:title()：将每个标题进行大写转换
a_str='my name is ben'
print(a_str.title())

a_str='python'
print(a_str[::-1])  #将python进行反过来输出

#字符串的切割：split(),切割返回一份列表
print('my name is  ben'.split(':'))

#join字符串的拼接  join()函数
print(','.join(['my','name' ,'is', ' ben']))

#对齐  ljust()：左对齐  rjust()；右对齐  center() 中间对其
print('python'.ljust(10,'a'))
print('python'.rjust(10,'a'))
print('python'.center(10,'q'))

#以字符，以字符结束
#startswith()函数，判断以什么开头
#endswith()函数，判断以什么结束,都是返回False/True类型
print('python'.startswith('py'))
print('python'.endswith('in'))

#判断元素是什么类型组合， isalnum()函数：数字或字符  isalphs():全部是字符  isdigit()函数：全部是数字，返回的都是False/True
print('ab55'.isalnum()) #数字或者字符
print('aaa'.isalpha())  #是否全部是字符
print('111'.isdigit()) #是否全部是数字

print(''.isspace())

#判断是否全部是小写 islower()函数
print('ben'.islower())

#判断是否全部是大写  isupper()函数
print('ben'.isupper())

#统计某个字符或者数字出现的次数 count()函数
print('hello'.count('l'))

#右对齐  zfill()函数，填充 拉伸 不够的步0
print('ben'.zfill(20))

















