# python文件结构
a = 'hello'
b = 3
print(a.islower())  # 判断是否小写
print(a.istitle())  # 判断标题

# python文件结构
"""
1.起始行
#/usr/bin/env python
2.模块文档（文档字符串）
"this is a test module"
3.模块导入
import mys
import os
4.（全局）变量定义
debug=True
5.类定义（着有）
class FooClass(object){
    'Foo class'
     pass
}
6.函数定义（着有）
def test():
    'test function'
    foo=FooClass()
    if defug:
        print('ran test')
7.主程序
if__name__== '__main__':
    test()
"""

# python过程式编程：每个模块都有一个名为_name_的内建变量，此变量值会根据调用模块的方式发生变化，
# 如果此文件被作为模块导入，到_name_的值为模块名称
# 如果此文件被直接执行。到_name_的值为‘_main_’


# python对象特性，比较及核心数据类型
'''
python程序中保存的所有数据都是围绕对象这个概念展开的
  1.程序中存储的所有数据都是对象
  2.每个对象（数据）都有一个身份，一个类型和一个值
   例如：school='shanghai',会以‘shanghai’创建一个字符串对象，其身份是指向它在内存中所处位置的指针（其在内村中的地址），
   而school就是引用这个具体位置的名称
 3.对象的类型也称对象的类别，用于描述对象的内部表示及它支持的方法和操作
 4.创建特定类型的对象时，有时也将该对象称为类型的实例
 5.实例被创建后，其身份和类型就不可改变
   如对象值是可修改的，则称为可变对象
   如对象的值不可修改，则称不可变对象
 6.如果某个对象包含对其他对象的引用，则将其称为容器
 7.大多数对象都拥有大量特有的数据属性和方法
   属性：与对象相关的值
   方法：被调用时将在对象上执行某些操作的函数
   使用点（.）运算符可以访问属性和方法

类：数据和方法组成，数据（私有的）：变量  方法（公共的）：函数
类：实例化成对象
'''

'''
python内置函数id（）可返回一个对象的身份，则该对象在内存中的位置
1.is运算符用于比较两个对象的身份
2、type（）用户返回一个对象的类型
3、对象类型本身也是一个对象，称为对象的类
    该对象的定义是唯一的，且对于某类型的所有实例都是相同的
    所有类型对象都有一个指定的名称，可用于执行类检查，如list，dict
'''
##两个对象的比价：
#  1.值比较，对象中的数据是否相同
#   2.身份比较：两个变量名引用的是否为同一对象
#   3.典型比较，两个对象的典型是否相同
#
num = 5
num2 = 5
num3 = num == num2
num4 = num is num2
print(num3)
print(num4)

"""
核心数据类型：
 数字：int，long，float，complay，bool
 字符：str，unicode
 列表：list
 字典：dict
 元祖：tuple
 文件：file
 其他类型：集合set（），frozenset，类类型，None
 其他文件类工具：pipes，fifos，sockets

 类型转换：
    str()，repr（）或format（）：将非字符整数类型转换字符
    int（）：转化为整数
    list（）：将字符串转为列表
    tuples（），将字串转成元祖
    set()，将字串转换为集合
    frozenset（s）：将字串s转换为不可变集合
    dict（d）创建字典 d必须是key，value的元祖序列
    chr(x);将整数转换为字符
    ord（x）:将整数转换为整数值
    hex（x）：将整数转换为16进制字符
    bin（）：
    oct（）：将整数转换为16进制字符串
"""
l1 = [('a', 1), ('b', b), ('c', 33)]
print(l1)
d1 = dict(l1)
print(d1)

d2 = tuple(l1)
print(d2)

num4 = 7
c1 = chr(num4)
print(type(c1))
print(c1)

"""
数字类型：
    python数字字面量:布尔型。整数。浮点数。复数
        True：1
        False：0
序列类型：
    序列表示索引为非负整数的有序对象集合，包括字符串，列表和元祖
       字符串是字符的
       列表和元祖是任意python对象的序列
    字符和元素属于不可变序列，而列表则支持插入、删除和替换元素
    所有序列都支持迭代

"""
import math

print(math)

'''
字符类型：
    字符串字面量：把文本放入单引号，双引号或三引号中


'''