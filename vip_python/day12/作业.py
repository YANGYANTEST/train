# 动手完成:
#   1.自己动手写一个学生类,创建属性名字,年龄,性别,完成
#      __new__,__init__,__str__,__del__，__call__


class Student():  # 新式类(object)--->父类
    # Student类的属性
    name = ''   # 类属性
    age = 0
    sex = ''

    # Student类的行为
    def __new__(cls, *args, **kwargs):  # 构造函数--->制造实例对象(简单),没有额外的属性
        print("我是__new__方法！")
        return super().__new__(cls)   #

    def __init__(self, name, age, sex):  # 初始化的时候添加额外的属性
        self.name = name
        self.age = age
        self.sex = sex
        print("实例对象属性初始化完成！！")

    def __str__(self):    #
        return "我是__str__方法"

    def __del__(self):    # 销毁对象的时候会自动调用
        print("正在销毁实例对象~~~")

    def __call__(self, *args, **kwargs):
        print("call行为被调用~~~")

stu1 = Student("xiaobing", 18, 'woman')
stu1()
print(stu1)

#   2.创建父类Person,属性name,函数eat,run,创建子类Student,学生类
#     继承Person,属性name,age,id,函数eat,study,全局定义一个函数
#     get_name,传入一个Person类的实例参数,分别传入Person和Student
#     两个类的实例对象进行调用.

class Person():
    # 类属性
    name = ''

    # 类行为
    def eat(self):  #
        print("吃饱后，不饿了，就是觉得舒服！")
    def run(self):
        print("正在飞快的向前跑... ...")

class Student(Person):
    age = 0   # 类属性
    id = 0

    def eat(self):
        print("吃饱后，才能更好的学习！！！")
    def study(self):
        print("I'm learning python now!")
#
def get_name(s):
    s.eat()
#
p1 = Person()
stu = Student()

get_name(p1)  # 父类--->
get_name(stu)   # 子类
print("=====================================")

#   3.完成python多态例子   爸爸有辆奥迪,儿子有保时捷
print("使用题2中的Person类和Student类！！")
pepole = Person()
stu2 = Student()
get_name(pepole)
get_name(stu2)

#   4.完成python中鸭子模型例子  #  动态语言里面--->静态语言(多态)
# 没有继承关系--->A(炒股)  B(炒股)--->相同接口    B没有继承A---
 