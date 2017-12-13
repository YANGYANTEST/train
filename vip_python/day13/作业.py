

#第一题:filter判断[0,False,True,5,{},(2,3)]对应bool值
def fun1():
    data = [0, False, True, 5, {}, (2, 3), ' ']
    a_filter = filter(lambda x: x, data)
    print(list(a_filter))



# 第二题:map实现1-10中所有奇数项的三次方,打印输出结果
def fun2():
    a_map = map(lambda x: x ** 3, range(1, 10, 2))
    print(list(a_map))


# 第三题:reduce实现1-100所有偶数项的和   2,4...100
def fun3():
    from functools import reduce
    num = reduce(lambda x, y: x + y, range(2, 101, 2))
    print(num)


# 第四题:用递归函数实现斐波拉契数列 (兔子繁殖的问题:(理想状态)-->黄金分割线)
def feibolaqie(num): # [0,1,1,2]() ---[1,1,2]()
    if isinstance(num, int):
        if num <= 2:   # 1,2   [1,1]
            return 1
        else:
            return feibolaqie(num - 1) + feibolaqie(num - 2)
    else:
        raise TypeError('传入的参数类型错误')


def fun5(term):
    a_map = map(feibolaqie, range(1, term + 1))  #   (1,2) #
    num_list = list(a_map)
    print(num_list)


if __name__ == '__main__':
    #fun1()
    #fun2()
    #fun3()
    fun5(30)   #
