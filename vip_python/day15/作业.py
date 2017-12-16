'''
1.range()，需要生成下面的列表，需要填入什么参数
[3,4,5,6]
[3,6,9,12,15,18]
[-20,200,420,640,860]

2.列表推导式或者生成器表达式完成1-100之间所有偶数之和

3.定义个函数，使用关键字yield创建一个生成器，求1，3，5，7，9各数字的三次方，并把所有的结果放到lis打印输出t里面

4.写出一个自定义的迭代器类（iter）
'''

#第一题
# print(list(range(3,7)))
# print(list(range(3,19,3)))
# print(list(range(-20,861,220)))

#第二题
# print(sum(i for i in range(1,101) if i%2==0))

#第三题
# def gen(n):
#     while n>0:
#         yield n*n*n
#         n-=2
# for num in gen(9):
#     print(num)

    #第四提
class Langyan():
    def __init__(self,id):
        self.id=id
    def __next__(self):
        if self.id==0:
            raise StopIteration("已经没有元素")
        self.id-=1
        return self.id
    def __iter__(self):
        return self
# y=Langyan(8)
# for num in Langyan:
#     print(num)