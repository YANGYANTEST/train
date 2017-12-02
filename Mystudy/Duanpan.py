'''
条件测试：
    if条件测试表达式

    python中的真假：
    1、任何非0数字和非空对象都为真
    2、数字0、空对象和特殊对象None均为假
    3、比较和相等测试会递归的应用于数据结构中
    4、返回值为True或False

    组合条件测试:
    x and y 与运算
    x or y 或运算
    not x 非运算

'''
x = 1
y = 3
if x > y:
    print("the max number is %d" % x)
else:
    print("the max number is %d" % y)

name = 'jerry'
if name == 'Tom':
    print("it is %s" % name)
elif name == 'hey':
    print("it is %s" % name)
else:
    print('linda')

# A=X if Y else Z  等价
# if Y :
#     A=X
# else:
#     A=Z


'''
while循环
    while.....else

    break:跳出最内层的循环
    continue：跳到所处的最近层循环 开始处
    pass：点位语句
    else代码块：循环正常终止才会执行，如果循环终止由break跳出导致的。则else不会执行

    练习：逐一显示指定列表中所有的元素
          求100以内所有偶数之和
          逐一显示指定字典的所有键，并于显示结束后说明总键数
          创建一个包含100以内所有奇数的列表
          倒序逐一显示一个列表的所有元素


'''

# count = 0
# while count < len(11):
#     print(l1.count)
#     count += 1
#     count += 1

