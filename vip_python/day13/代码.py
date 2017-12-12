'''

1.self/super
2.多层继承
3.经典类和新式类
4. __slots__/@property # 把函数包装成属性
5.定制类,元类,枚举类
6.Python之魔法方法

'''


#self/super

# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# class Boy(Person):
#     def __init__(self,name,age,sex):
#         super().__init__(name,age,sex)  #super（在子类里面----》super（）------>父类对象）
#         self.sex=sex
#
# p1=Person('yangyan',22)
# p2=Person('chenhong',25)
#
# #多继承
#
# class A():
#     name='yan'
#     age=20
#     id=1
#
# class B():
#     name='lin'
#     age=23
#     id=2
#
# class C(A,B):
#     pass
#
# c1=C()
# print(c1.name)



#经典类和新式类
#py2* 版本里面--class Person():没有任何父类，称为经典类
#py2* 版本里面--class Person(object):新式类
#py3* 版本里面--class Person():--默认继承了object（超类）

#经典类和新式类  多继承的区别
# class A():
#     def func(self):
#         print("a_func")
#
# class B():
#     def func(self):
#         print('b_func')
# class C():
#     pass
#
# class D(A,B):
#     def func(self):
#         print('d_func')
# class E(C,D):
#     pass
#
# e=E()
# e.func()
#py3*版本结果：d_func
#py2*版本结果,a_func

#py3**新式类---广度优先，先找子类，子类没有再找直接的父类
#py2**经典类---深度优先，，先找子类，子类没有，再找子类的上级

# class A():
#     def show(self):
#         print("A")
#
# class B(A):
#     def show(self):
#         print("B")
#
# class C(A):
#     def show(self):
#         print("C")
#
# class D(B,C):
#     pass
#     # def show(self):
#     #     print("D")
#
# d=D()
# d.show()


#__slote__实例对象--动态绑定属性（静态语言很难实现）
# class Person():
#     pass
# p1=Person()
# p1.name='ben'       #对象动态去绑定了属性name
# print(p1.name)
# p2.name='yang'
# print(p2.name)


    #动态绑定方法：
# def func(self,name):    #全局函数，不是类里面的函数
#     self.name=name
#     print(self.name)
#
# p1.func=func    #把函数当作对象传递
#p1.func(p1,'coco')#打印出coco，因为类里面不需要显示去p1

#动态绑定方法另外的方式：
# class Person():
#     pass
#
# p1=Person()
#
# def set_name(self,name):
#     self.name=name
#
# from types import MethodType
# p1.set_name=MethodType(set_name,p1) #MethodType这个函数来实现动态方法
# p1.set_name('alina')    #参数
# print(p1.name)

# p2=Person()
# print(p2.name)  报错，因为p2是另外一个实例对象，不是p1

#动态绑定-----双刃剑--》可好可坏----》打破了原有的规则

#py3*版本  slots属性（以柔克刚）
# class Person():
#     __slots__ =('name','age')
# p=Person()
# p.name='ben'
# p.age=23
# print(p.name,p.age)


#动态特性，非常有意思，但是__slots__作出限制（软措施）


#属性包装

# class Person():
#     age = 1
#
# p = Person()
# p.age = 9
# print(p.age)

class Person():
    age = 1

    def get_age(self):
        return self._age

    def set_age(self, age):
        if not isinstance(age, int):    #类型的限制
            raise ValueError('年龄必须为整数')
        if age < 0 or age > 100:
            raise ValueError('年龄必须在1 - 100')    #数值的限制
        self._age = age
p=Person()
p.set_age(79)
print(p.age)




#属性包装：把函数包装对象的属性---》p.函数名称（）

class Person():
    @property   #装饰器
    def age(self):
        return self._age

    @age.setter #设置函数---属性的赋值（设置属性）
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError('年龄必须为整数')
        if age < 0 or age > 100:
            raise ValueError('年龄必须在1 - 100')
        self._age = age

    @age.deleter    #删除属性
    def age(self):
        del self._age

p=Person()
p.age=66
print(p.age)
del p.age



#枚举类
ONE=1
TWO=2

ONE=88
print(ONE)

#常量：所有的字母全大写
#如何限制？
#意义所在：看起来是常量，还是可以去改变的，封装到枚举类，只能去获取常量而不能修改常量

from enum import Enum,unique

@unique     #做出唯一限制
class Num(Enum):
    ONE=1
    TWO=2

print(Num.ONE.value)
#Num.TWO.value=10    #不能设置属性，值不能被修改，AttributeError: can't set attribute
# print(Num.TWO.value)



#__class__属性
num=97
print(num.__class__)
print(num.__class__.__class__)  #class type(元类)-----用来制造类的类对象

#实例对象------由对应的类模型----元类

#type函数创建类模型

def work(self):
    print("正在工作")
def play(self):
    print("正在玩耍")

Boy=type('Boy',(),{'is_girl':'False',"name":'yang','work':work,'play':play})
print(type(Boy))        #------元类type
boy=Boy()   #创建一个实例
print(type(boy))
print(boy.is_girl)
print(boy.name)
boy.work()
boy.play()


















