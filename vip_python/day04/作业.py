'''
第一题:
num_list = [[1,2],[‘tom’,’jim’],(3,4),[‘ben’]]
 1. 在’ben’后面添加’kity’
 2. 获取包含’ben’的list的元素
 3. 把’jim’修改为’lucy’
 4. 尝试修改3为5,看看
 5. 把[6,7]添加到[‘tom’,’jim’]中作为第三个元素
 6.把num_list切片操作:
      num_list[-1::-1]


第二题:
numbers = [1,3,5,7,8,25,4,20,29];
1.对list所有的元素按从小到大的顺序排序
2.求list所有元素之和
3.将所有元素倒序排列
'''

num_list = [[1,2],['tom','jim'],(3,4),['ben']]
num_list.append('kity')#在’ben’后面添加’kity’
print(num_list)
print(num_list[3])#获取包含’ben’的list的元素
num_list[1][1]='lucy'#把’jim’修改为’lucy’
print(num_list)
print(num_list)
num_list[1].append([6,7])
print(num_list)
num_list[-1::-1]
print(num_list)



'''
numbers = [1,3,5,7,8,25,4,20,29];
1.对list所有的元素按从小到大的顺序排序
2.求list所有元素之和
3.将所有元素倒序排列
'''

numbers=[1,3,5,7,8,25,4,20,29]
numbers.sort(reverse=False)#对list所有的元素按从小到大的顺序排序
print(numbers)
print(sum(numbers))#求list所有元素之和
numbers.reverse()#将所有元素倒序排列
print(numbers)
