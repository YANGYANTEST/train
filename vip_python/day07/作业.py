


#1.简述普通参数、默认参数、关键字参数、动态收集参数的区别,理解为主

#2.def foo(x, y, z, *args, **kw):
 #   sum = x + y + z
 #   print(sum)
 #   for i in args:
  #      print(i)
   # print(kw)
#for j in kw.items():
 #       print(j)
#a_tuple = (1,2,3)     此处参数修改为2个看看会怎么样?
#b_dict = {'name': 'jim', 'age': 28, 'add': '上海'}
#foo(*a_tuple, **b_dict)    分析这里会怎么样?



#3.题目:执行分析下代码
 #   def func(a, b, c=9, *args, **kw):
  #       print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
   # func(1,2)
    #func(1,2,3)
   # func(1,2,3,4)
    #func(1,2,3,4,5)
   # func(1,2,3,4,5,6,name='jim')
  #  func(1,2,3,4,5,6,name='tom',age=22)
   # 扩展: 如果把你的函数也定义成  def  get_sum(*args,**kw):pass
    #你的函数可以接受多少参数?


#4.写一个函数函数，计算传入字符串中的数字、字母、空格和其他的个数分别为多少?




def foo(x, y, z, *args, **kw):
    sum = x + y + z
    print(sum)
    for i in args:
        print(i)
    print(kw)
    for j in kw.items():
        print(j)
a_tuple = (1,2,3)
b_dict = {'name': 'Alina', 'age': 22, 'add': '上海'}

foo(*a_tuple, **b_dict)


def func(a, b, c=9, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

func(1,2)
func(1,2,3)
func(1,2,3,4)
func(1,2,3,4,5)
func(1,2,3,4,5,6,name='jim')
func(1,2,3,4,5,6,name='tom',age=22)


def funcl(p):
    digit_number = 0
    space_number = 0
    alpha_number = 0
    else_number = 0
    for i in p:
        if i.isdigit():
            digit_number += 1
        elif i.isspace():
            space_number += 1
        elif i.isalpha():
            alpha_number += 1
        else:
            else_number += 1
    return (digit_number, space_number, alpha_number, else_number)

