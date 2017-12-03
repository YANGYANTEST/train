# print("hello world")

# a=input("请输入你的名字：")
# print(a)

# name=r'zhangsan\n'
# print(name)

#输出换行

# a="zhangsan\nlisi\nwangwu"
# print(a)
#
# name="zhangsan\n"+"lisi\n"+"wangwu"
# print(name)

#换行\n操作
# a=input('\n\n\n Enter over!!!')
# print(a,end='')

#如果要实现不换行需要在变量末尾加上 end=""：
# print('a',end='')
# print('b',end='')
#
# print('a');print('b');print('c')

import math
from math import *
from math import  log2

#import 模块名
#from 模块名 import 方法（所有的方法是 * ）
import selenium as sm
from selenium import webdriver

#打印出当前的路径
# import sys
# for i in  sys.argv:
#     print(i)

# a=input("请输入a：")
# b=input("请输入b：")
# c=a+b
# #print(a+b)
# if c==6:
#     print(c)
# else:
#     print("......")

#转换为整形，进行相加
# a=int(a)
# b=int(b)
# print(a+b)


#输入三个数，判定他们能不能组成三角形
# a=int(input("请输入a："))
# b=int(input("请输入b："))
# c=int(input("请输入c："))
# if (a > b+c) or (b > a+c) or (c > a+b):
#     print('No')
# else:
#     print('YES')


#方法1：
# user=input("请输入你的用户名：")
# passward=input("请输入你的密码：")
# if user=="admin" and passward=="123456":
#     print('登陆成功！')
# else:
#     print("输入有误，请重新输入！！！")


#方法2：
# if user=="admin":
#     if passward=='123456':
#          print('登陆成功')
#     else:
#          print('密码错误')
# else:
#     print('用户名错误')


#a=100 打印出满分  a=10，输出低分
# a=int(input('a= '))
# if a==100:
#     print('高分')
# elif a==10:
#     print('低分')
# else:
#     print('.....')

#一句话完成2个值的交换
# a=10
# b=2
# a,b=b,a
# print(a)
# print(b)

# a=input('a= ')
# print(type(a))
# print(isinstance(a,int))

#10  1.5  4


#152  8
# a=152/8
# b=152//8
# print(a)
# print(b)

name="hello World,I am Python！"
# print(len(name))
# print(name[23])
# print(name[0:5])
# print(name[-7:])
# print(name[0:12:2])

print(name[:17]+'Ardroid')
print(name[-7:-1]+name[5:])
print(name[:12:2]+name[11:17]+'Ardroid')

'''
python内建函数：
capitalize()将字符串的第一个字符转换为大写
center(width, fillchar)返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
count(str, beg= 0,end=len(string))返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
bytes.decode(encoding="utf-8", errors="strict")Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。

encode(encoding='UTF-8',errors='strict')以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace‘
endswith(suffix, beg=0, end=len(string))检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
expandtabs(tabsize=8)把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。


find(str, beg=0 end=len(string))检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
index(str, beg=0, end=len(string))跟find()方法一样，只不过如果str不在字符串中会报一个异常.
isalnum()如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
salpha()如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
isdigit()如果字符串只包含数字则返回 True 否则返回 False..


islower()如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
isupper()如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
isnumeric()
如果字符串中只包含数字字符，则返回 True，否则返回 False
join(seq)以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串


len(string)返回字符串长度
lower()转换字符串中所有大写字符为小写.
lstrip()截掉字符串左边的空格或指定字符。
maketrans()创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

max(str)   min(str)返回字符串 str 中最大（小）的字母。
split(str="", num=string.count(str))num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串
splitlines([keepends])按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
isdecimal()检查字符串是否只包含十进制字符，如果是返回 true，否则返回 fals


strip([chars])在字符串上执行 lstrip()和 rstrip()
swapcase()将字符串中大写转换为小写，小写转换为大写
title()返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
upper()转换字符串中的小写字母为大写



'''
name='heLLo'
a1=name.capitalize()
print(a1)

