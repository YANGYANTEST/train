#1.自己写一个字典:
#   name_dict = {'name':'ben','age':22,'sex':'男'}
#   添加,删除,更新,清空操作

name_dict = {'name':'ben','age':22,'sex':'男'}

#name_dict['phone'] = 151
#print(name_dict)

#name_dict.pop('age')
#print(name_dict)

#name_dict.clear()
#print(name_dict)

#num_dict ={1:22,2:'Alina',3:'Aron'}
#name_dict.update(num_dict)
#print(name_dict)


#   num1_set= {3,5,1,2,7}
#   num2_set = {1,2,3,11}
#  并分别进行&,|,^,-运算

#num1_set= {3,5,1,2,7}
#num2_set = {1,2,3,11}
#print(num1_set & num2_set)
#print(num1_set | num2_set)
#print(num1_set ^ num2_set)
#print(num1_set - num2_set)

#3.整数字典:
#   num_dict = {'a':13,'b':22,'c':18,'d':24}
#  按照dict中value从小到大的顺序排序
num_dict = {'a':13,'b':22,'c':18,'d':24}
new_dict = sorted(num_dict.items(), key=lambda d:d[0])
print(new_dict)





# 1.用while和for两种循环求计算1+3+5.....+45+47+49的值
# 2.代码实现斐波那契数列(比如前30个项)


result =0
n = 49
while n >0:
    result +=n
    n -=2
print(result)

result =0
for num in range(1,50,2):
    result +=num
print(result)

lists = [0,1]
for n in range(1,29):
    item = lists[len(lists)-1] + lists[len(lists)-2]
    lists.append(item)
print(lists)



