'''
本节内容：
1.函数,类函数,
2.构造函数与析构函数,垃圾回收机制
3.类的实例对象与类之间的关系
4.面向对象编程三大特性
5.鸭子形态
'''

def tell (name):
    print('i love %s'%name)
if __name__ =='__main__':
    tell()
else:
    print('被导入执行')
