'''
动手完成:
  1.自定义一个异常类,当list内元素长度超过10的时候抛出异常
  2.思考如果对于多种不同的代码异常情况都要处理,又该如何去处理,自己写一个小例子
  3.try-except和try-finally有什么不同,写例子理解区别
  4.写函数，检查传入字典的每一个value的长度，如果大于2，
     那么仅仅保留前两个长度的内容，并将新内容返回给调用者
     dic = {“k1”: "v1v1","k2":[11,22,33}}

'''

import sys
class MyListError(Exception):
    def __init__(self,message):
        super().__init__(self)
        self.mess=message
    def __str__(self):
        return self.mess

try:
    my_list=[]
    for item in range(1,20):
        my_list.append(item)
    if len(my_list)>10:
        raise MyListError("列表长度超过规定长度")
except MyListError as e:
    print(e)
except Exception as e:
    print("Exception")
finally:
    print("程序结束退出！")

#2.思考如果对于多种不同的代码异常情况都要处理,又该如何去处理,自己写一个小例子
def throw_exception(i):
    try:
        if i <0:
            raise ValueError("数值不正确")
    except ValueError as e:
        print("数值不能小于0")
# result=division(6,0)
throw_exception(-8)



#3。try-except和try-finally有什么不同,写例子理解区别
#finally 不管有无异常，都会被执行。except只有异常的时候才会执行
try:
    print(1/0)
except ZeroDivisionError as e:
    print("除数不能为0")
finally:
    print("程序结束")


#4.写函数，检查传入字典的每一个value的长度，如果大于2 那么仅仅保留前两个长度的内容，并将新内容返回给调用者  dic = {“k1”: "v1v1","k2":[11,22,33}}
def funcol(**p_dict):
    #判断当前对象类型是否字典数据类型
    if isinstance(p_dict,dict):
        for key,value in p_dict.items():
            #判断value是list，tupl，str时，截取前面2个字符，如果不是，原样返回
            if isinstance(value,(list,tuple,str)):
                if len(value)>2:
                    p_dict[key]=value[0:2]
        return p_dict
num_dict={'k1':100,'k2':[1,3,5,6]}
# num_dict={'k1':100,'k2':290}
fun_dict=funcol(**num_dict)
print(fun_dict)