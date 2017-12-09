'''
a_list = [1, 2, 3, 2, 2]
删除a_list中所有的2

2.用内置函数compile创建一个文件xx.py 在文件里写你的名字, 然后用eval函数读取文件中内容, 并打印输出到控制台

3.写一个猜数字的游戏, 给5次机会, 每次随机生成一个整数, 然后由控制台输入一个
数字, 比较大小.大了提示猜大了, 小了提示猜小了.猜对了提示恭喜你, 猜对了.退出程序, 如果猜错了, 一共给5次机会, 5次机会用完程序退出.
'''

a_list = [1,2,3,2,2]
while 2 in a_list:
   a_list.remove(2)
print(a_list)

code = compile("open('123.py','a',encoding='utf-8').write('45678')",'123.py','eval')
eval(code)

import random
num = random.randint(0,100)
print(num)
for i in range(1,6):
   a_num = int(input('请输入一个数字：'))
   if a_num > num:
       print('猜大了')
   elif a_num < num:
       print('猜小了')
   else:
       print('恭喜你，猜对了')
       break

   if i==5:
       print("你的机会全部用完，谢谢")
   else:
       print("还剩下%s次机会" % str(5-i))
print("游戏结束，程序退出")






