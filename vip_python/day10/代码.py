'''
什么是错误和异常
常见的异常种类
异常怎么处理
自定义异常
'''

#错误和异常？
#Java 中，try....catch....如果发生异常进行捕获
#python中，try...except...

try:
    file=open('dongnao.py','r')
    print("没有发生异常")
except Exception as e:
    print(e)
else:
    print("异常没有发生")
finally:
    print("不管有无异常，都需要执行的")



#常见的异常错误
'''
NameError:使用了没有定义的变量
ZeroDivisionError : 除数为零异常   5/0
SyntaxError:  python解释器语法错误  : for
IndexError  越界，超出范围
KeyError  	映射中没有这个键
IOError   输入输出错误
AttributeError:位置属性异常
'''
#print(name)  NameError(种类)


#ZeroDivisionError: division by zero
#print(9/0)

#SyntaxError:
# for num in [1,2,3]      #少了个冒号
#     print(num)

#IndexError
# a=[12,34]
# print(a[5])


#KeyError
# b={"name":"akina"}
# print(b["inh"])

#IOError
#f=open('yang.py')

#AttributeError:位置属性异常
# class Myclass():
#     pass   #模型里面没有name属性
# c=Myclass()
# print(c.name)



#分异常捕获：
try:
    x = 24 / 0
    f=open('yangyan.py')    #不能直接操作文件，（调用操作系统的操作方法接口----》操作文件）
    y=int('我不是数字')
except ValueError as e:
    print(1)
except IOError as e:
    print(2)
except ZeroDivisionError as e:
    print(3)
except Exception as e:
    print(e)    #不管哪种异常，都做同样的处理，没有分开
else:
    print("一切正常")
finally:
    print("清除数据")
    print("清除完毕")


#
# try:
#     result=int(input("请输入一个数字："))
#     num=99/0
# except (ValueError,ZeroDivisionError,IOError,Exception)as e:
#     print(e)
# finally:
    print("到此结束")



#函数之间相互调用异常处理


def func():
    try:
         f=open('yan.py')
         print("前面没有发生异常")
    except IOError as e:
        print(e)

def func1():
    try:
         x=22/2
         func()  #调用第一个函数
    except ZeroDivisionError as e:
        print(e)
#
# try:
#     func()
# except ZeroDivisionError as e:
#     print(e)
#     print("被0除")
# except IOError as e:
#     print(e)
#     print("发生ie异常")

func()

#由程序员主动抛出异常，
#强制抛出异常的关键字 raise
# age=22
# if age>20:
#     raise ValueError("哥们，年纪大了，姑娘看不上")


#自定义异常
import sys
class MYEeeor(Exception):#父类异常
    def __init__(self,message): #初始化函数
        self.mess=message
    def __str__(self):
        return self.mess
def run():
    try:
        if len(sys.argv)==1:#sys.argv脚本执行传的参数
            me=MYEeeor("参数的个数不正确")#创建一个实例对象
            raise me
    except Exception as e:
        print(e)

if __name__=='__main__':#主入口
    run()





