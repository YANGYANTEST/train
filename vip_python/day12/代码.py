'''
本节内容：
1.函数,类函数,
2.构造函数与析构函数,垃圾回收机制
3.类的实例对象与类之间的关系
4.面向对象编程三大特性
5.鸭子形态
'''

#函数，模块，模块属性__name__
#注意;函数和调用参数要掉对象，导入执行，解释执行
# def func (name):
#     print('i love %s'%name)
# if __name__ =='__main__':#入口，
#     func('yang')
# else:
#     print('被导入执行')
#
# #type
# print(type(99)==int)
# print(type('ste')==str)
# print(type(88)==type('sjks'))
#
# import types    #types模块---------封装了函数类型对象
# def fun():
#     print('110')
# print(type(fun)==types.FunctionType)
#
#
# print(type(fun)==types.FunctionType)#type---------内置函数（自己定义函数）
# print(type(fun)==types.BuiltinFunctionType)#判断是不是内置函数  false
#
# print(type([x for x in range(22)])==list)  #true  列表推导式，返回list
# print(type(x for x in range(22))==types.GeneratorType)      #false  生成器(GeneratorType)
#
# #匿名函数
# print(type(lambda x:x*2)==types.LambdaType)

#进入面向对象。如何自定义类，class关键字
#注意：在python3版本中，自定义类（）参数默认为空，新式类---自动去继承对象的基类（超类）object
# import time
# class Student():#继承了object
#     #实例对象创建之后初始化数据
#     def __init__(self,name,id,age): #self--指向当前实例对象本身
#         self.name=name
#         self.id=id
#         self.age=age
#         print('%s 正在初始化'%self.name)
#     def __del__(self):
#         print('%s是小可爱'%self.name)
#
#     def get__name(self):
#         print(self.name)
# s1=Student('杨艳',11,23)         #创建实例对象---传递参数
# s1.get__name()
# time.sleep(2)
# print(Student.__class__.__bases__)#__class__:类模型，__bass__父类对象是谁 object

'''
4.__init__ 没有代
注意点：
1.关键字---class
2.类名：首字母大写
3.新式类和经典类码里面显示去调用
'''

#类变量和实例变量

# class Person():
#     age=88
#     def __init__(self,age):
#         self.age=age
#
# person1=Person(51)
# print(type(person1))
# print(Person.age)
# print(person1.age)


#实例方法，类方法，静态党法
# class Student():
#     #实例对象创建之后初始化数据
#     def __init__(self,name,id,age): #self--指向当前实例对象本身
#         self.name=name
#         self.id=id
#         self.age=age
#         print('%s 正在初始化'%self.name)
#
#     def __del__(self):
#         print('%s是小可爱'%self.name)
#
#     def get__name(self):        #实例对象的方法
#         print(self.name)
#
#
#     @classmethod   #数字2同一个键
#     def cls_fun(cls):#cls必须要有这个参数，---类对象（）
#         print('这是类方法')
#         print(cls)
#     @staticmethod
#     def start_up(): #self.cls(没有这两个参数)
#         print("这是静态方法")

#制造对象
# s1=Student('yangyan',28,11)
# s1.get__name()  #实例方法
# s1.cls_fun()    #类方法
# s1.start_up()   #静态方法
#
# #类对象
# Student.cls_fun()#类方法
# Student.start_up()#静态方法
#Student.get__name() #报错，get_name()-----某个实例对象相关

#静态方法直接类名，静态方法名（）--------没有创建某个实例对象

#__函数名次__特殊含义的函数
class Person():
    def __new__(cls, *args, **kwargs):
        print("构造函数初始化之前执行")
        return super().__new__(cls)   #super(超级)父类对象object初始化函数

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("初始化函数是函数之后执行")

    # def __call__(self, *args, **kwargs):
    #     def work():
    #         print('l love you')
    #     return work
        # print("当前对象被调用")
        # return self.name

p1=Person('陈红',25)  #p1创建实例对象本身
# print(p1())#把实例对象当作函数在用
# p1()()



#访问作用域 __name__(具有特殊定义)
class Person():
    _min=10
    __max=99

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __work(self):   #函数名称（没有）
        print("我有私有方法")

class Boy(Person):
    def __init__(self,name,age,sex):
        super().__init__(name,age)
        self.sex=sex

a_person=Person('tom',22)
a_boy=Boy('lucy',13,'女')
print(Person._min)
#print(Person._max)

print(Boy._min)     #子类可以获取（_属性：当前类内部，还有子类可以获取到）
#print(Boy._max)     #私有变量（只能在当前内部使用）

#a_person.__work()   #超出范围


#继承和复写
class Person():
    def sleep(self):
        print("person正在睡觉")

class Boy(Person):
    def sleep(self):
        print("boy正在睡觉")
    def play_game(self):
        print('boy正在打游戏')


p=Person()  #父类
b=Boy()     #子类

p.sleep()   #父类调用
b.sleep()       #子类调用
b.play_game()

print(isinstance(p,Person))
print(isinstance(b,Boy))
print(isinstance(b,Person))
print(isinstance(p,Boy))

print("========================================")

#多态  非类里面的函数（模块的全局函数）

def show(p):
    p.sleep()


p=Person()
b=Boy()

show(p)     #同一个show，结果是不同的形态
show(b)


#鸭子形态:不在乎有没有继承关系，有没有接口方法（有同一样的接口状态就行，sleep）

class Person():
    def sleep(self):
        print("person正在睡觉")

class Boy():
    def sleep(self):
        print("boy正在睡觉")

def show(p):
    p.sleep()

p=Person()
b=Boy()

show(p)
show(b)