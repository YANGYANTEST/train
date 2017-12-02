#作业：模拟银行系统登陆，输入错误三次，报错

#方法1：
'''
num = 0
while True:
    name = input('请输入用户名:')
    pwd = input('请输入密码:')
    num +=1
    if num == 3:
        print ("您的账号已被锁定，请联系客服")
        break
        print ("账户或密码错误，请重新输入")
    if name == "yangyan" and pwd == "123456":
        print ("Wclcome\n\tName:%s" %(name))
        break
    else:
        print("用户名和密码错误")
'''

#方法2：
'''
def input_account():
    username=input("please input username")
    password=input("please input password")
    return username,password
def check_result():
    for i in range(3):
        username,password=input_account()
        if username=='root' and password=='root':
            print("Welcome")
        else:
            print("your username and password is wrong")
            continue
    else:
        print("you try more than 3 times,but wrong")
    check_result()
'''
#如何使用两个变量来生成list
#d={'java':99,'c':'99','c++':'99'}



#练习：
#L={'java','c','swift','Python',123}
#现在有list做包含字符串和整数，把list中得大写字母转为小写，推送到List
#1.使用内建得isinstance函数可以判断一个变量是不是字符串
#2.s。lower（）可以将一个大写字母转为小写
#3.增加if语句保证列表生成式正确执行

'''
def get_param(age,*args):
    print(age)
    print(args[1])
get_param('key')
'''

#不定长参数
'''
def get_param(**args):
    for k,v in args.items():
        print("{}：{}".format(k,v))
get_param(name="key",sex="F",age=17)
'''

# school="Beijing Univsuty"
# def get_BD():
#     school="FUDan Univsuty"
#     print(school)
# def get_qinghua():
#     print(school)
# get_qinghua()
#
#
# #递归函数
# def get_fact(n):
#     if n==1:
#         return 1
#     return n*get_fact(n-1)
# result=get_fact(3)
# print(result)
#
#
# #lambda函数
# def square(x):
#     return x*x
# result=square(3)
# print(result)
# def sum_value(x,y):
#     return x+y
# result1=sum_value(3,5)
#
# result=lambda x:x*x
# print(result(3))
#
# result2=lambda x,y:x+y
# print(result2(3,5))


#作业：如果有个列表：
# lista=[1,7,45,78,33,54,89] 不用内建函数，找出这个列表的最大值
#不用内建函数，自定义一个函数，将这个列表排序

lista=[1,7,45,78,33,54,89]
#方法1：
# def max(lista):
#     max_num = lista[0]
#     for a in lista:
#         if a > max_num:
#             max_num = a
#     return max_num
# if __name__ == '__main__':
#     print(max([1,7,45,78,33,54,89]))

#方法2：
# def get_max(obj):
#     maxvalue=obj[0]
#     for i in range(1,len(obj)):
#         if obj[i]>maxvalue:
#             maxvalue=obj[i]
#     return maxvalue
# result=get_max(lista)
# print(result)
#
# #方法3:while方法
# def get_maxx(obj):
#     n=0
#     max_value=0
#     while n<len(obj):
#         if obj[n]>max_value:
#             max_value=obj[n]
#         n+=1
#     return max_value
# print(get_max(lista))


#方法4：冒泡排序法
# def sort_list(obj):
#     for i in  range(len(obj)):
#         for j in range(i):
#             if obj[j]>obj[j+1]:
#                 obj[j],obj[j+1]=obj[j+1],obj[j]
# sort_list(lista)
# print(lista)


#作业：百鸡百钱问题：公鸡5元一只，母鸡3元一只，小鸡3元一只，如何用100元买100只鸡？
'''
公鸡最多20
母鸡最多33
x，cook
y，hen
z，chirld
x+y+z=100
5x+3y+z/3=100
'''
# def get_number_of_chechek():
#     for x in  range(20):
#         for y in range(33):
#             z=100-x-y
#             if 5*x+3*y+z/3==100 and z%3==0:
#                 print("cook:{} chield:{}".format(x,y,z))
# get_number_of_chechek()


# def f(obj1):
#     return obj1*2-1
# def add(x,y,f):
#     return f(x)+f((y))
# print(add(3,5,f))

#map函数
# list1=range(1,5)
# def get_squre(x):
#     return x*x
# result=map(get_squre,list1)
# print(list(result))
#
# result=map(lambda x:x*x,list1)

#reduce函数
# list1=[1,2,3,4]
# from functools import reduce
# def get_value(x,y):
#     return  x*y
# result=reduce(get_value,list1)
# print(result)

#filter函数

# my_list=['lily',' ','lucy']
# def remove_empty(str):
#     return str and str.strip()
# result=filter(remove_empty,my_list)
# print(list(result))


A=['adam','LISA','barT']
def fn(x):
    return x


#作业：过滤大于5，小于10的数
