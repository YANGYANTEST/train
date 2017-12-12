#;python之文件操作
'''
1.文件操作open
2.文件操作的模式
3.文件句柄对象
4.python上下文管理器
5.文件异常处理

'''

#1.文件操作
'''
中间层：操作系统文件操作的接口方法
open----》操作系统文件处理的接口方法------操作文件（提交本地安全）
'''
#f=open('yangyan.py','w')

# import time
# f=open('work.py','w',encoding='utf-8')   #f返回文件对象,
# print(type(f))
# f.write("123345")
# f.write('\n')
# f.write("hello,yang")
# time.sleep(5)
# print("休眠结束，继续执行代码")
# f.close()   #释放文件句柄对象---释放资源
# #注意：出现乱码一定要加入encoding='utf-8'


'''
有些问题需要注意：
1.第一个参数(使用相对路径)如./work.py
2.操作模式
3.如果写入数据出现乱码----编码问题，要加入encoding='utf-8'
4.如果当前文件已经存在呢？存在的话就直接打开，不存在的话就新创建文件
5.模式决定----w（会覆盖原有数据，再写入新数据），不覆盖，追加数据如何操作？
6.写入数据是不是立即写入文件里面？
'''


#第一步：创建文件句柄对象
# file=open('work.py','r')
# result=file.read()  #一次性读取所有的数据，默认留空
# print(result)
# file.close()


'''
注意地方：
1.文件不存在会抛出异常，FileNotFoundError: [Errno 2] No such file or directory: 'wor.py'
2.'w','r'
3.读取的数据可能会出现乱码 
4.读取数据完毕之后，关闭文件句柄对象，释放资源
5.read()，文件句柄对象的方法，read()没有参数，一次性全部读取
'''


#文件读取的第一种方式：read()
#如果修改read函数的参数（有参数）
# file=open('work.py','r')
# result=file.read(5)  #有参数，参数代表读取多少字节数
# print(result)
# file.close()



#文件读取的第二种方式;readline(),读取一行数据
# file=open('work.py','r')
# result=file.readline()  #有参数，参数代表读取多少字节数
# print(result)
# file.close()


#readline()有参数传递进去，读取数据的个数
#readlines()有参数的话，若想打印出第二行内容，参数必须要大于第一行的内容个数

#文件读取的第三种方式：readlines()，返回的是一个列表
# file=open('work.py','r')
# result=file.readlines()
# print(type(result))
# for line in result:
#     print(line,end='')
# file.close()


#文件操作的模式
'''
r模式：读模式
w模式：写模式
a模式：追加模式
r+
w+
a+
'''

#追加模式，a模式
# file=open('work.py','a')
# file.write('\n333')
# file.close()



#r+,如果文件不存在的话，会报错
# file=open('work.py','r+')
# result=file.read()
# file.write('\n999')
# file.close()


#w+,如果当前文件不存在，则自动创建当前名字的文件；当前文件存在，则会覆盖文件里面的数据
# file=open('work.py','w+')
# result=file.read()
# file.write('999')
# file.close()



'''
r+/w+:
1.相同点：都是可读可写的操作
2.不同点：
   1.r+模式，如果当前文件不存在，读写都报错
   2.w+模式，如果当前文件不存在，则自动创建当前名字的文件
            如果当前文件存在，则会覆盖文件里面的数据
'''

#a+
# file=open('work.py','a+')
# file.write('34567')
# file.seek(0)
# file.close()

'''
a+模式：
1.可读可写的操作模式
2.如果当前文件不存在，则创建该文件
3.如果当前已经存在，往文件里面写入的数据则会被追加到末尾

'''


#文件句柄对象（建议使用这种）
# f=open('work.py','r')
# for line in f:  #
#     print(line,end='')

#文件句柄对象优点：
#文件句柄对象是可迭代对象
#通过这种方式去读取数据-----优点：100条数据，很多行 内存小 read()



#close()-----数据的刷新（缓冲区）----->超过容量的时候会把数据写入到文件（没有超过）----调用
#close()----->刷新数据的操作-----关闭文件句柄对象


#上下管理器文件的操作
#with关键字-------上下管理器  (with+内置open()-----文件对象，取别名)
#as----去别名
# with open('work.py','',encoding='utf-8') as f: #f---->open函数返回的对象
#     for line in f:  #内存的优化（文件读取）
#         print(line.strip())

# with open('work.py', 'a+', encoding='utf-8') as f:
#     for line in f:
#         print(line.strip())
#     f.write('\n我加最后一句')

# with open('work.py', 'a+', encoding='utf-8') as f:
#     result_list=["你是谁，’\n",'我是谁','\n',"最后一行数据了"]
#     f.writelines(result_list)
#     f.seek(0)   #有没有数据是文件指针位置所决定，再末尾读取不到数据，移动文件指针的位置
#     for line in f:
#         print(line.strip())
#     f.write('\n我加最后一句')



#errors='ignore 如果遇到编码错误,处理的方式是忽略
# try:
#     f=open('yang.py','r',encoding='utf-8',errors='ignore')
#     conn=f.read()
#     print(conn)
#     f.close()
# except Exception as e:
#     print(e)
# finally:
#     print("byebye")
# print(11111111111)




#a+模式里读数据,不小心读取的是空数据()
with open('work.py','a+',encoding='utf-8')as f6:
      print(f6.tell()) #w文件指针的位置
    # print(f.read()) #读取不到数据
      f6.seek(2) #移动到最前面
      print(f6.read())
      print(f6.tell())