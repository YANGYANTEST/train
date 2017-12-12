'''
1.文件名称:use.txt
   创建该文件,路径由你自己指定,打开该文件,往里面写入
   str_content = ['tom is boy','\n','you are cool','\n',
                       '今天你怎么还不回来']
   把数据写入到该文件中,注意操作的模式,关闭文件句柄后
   再次打开该文件句柄,然后读取文件中内容,用with代码块
   实现,然后打印输出信息到控制台,注意换行符

 2.with创建一个文件homework.txt,尝试多种操作模式.进行写读操作,注意区别

 3.理解文件句柄,对比read(),readline(),readlines()写一个小例子

 4.准备一张jpg图片,把图片中数据读书出来,并写入到文件my_img.jpg文件中,
    操作完毕后尝试打开my_img.jpg文件看图片显示正不正常
'''

#第一题：
# with open('use.txt','a+',encoding='utf-8')as f:
#     str_content= ['tom is boy','\n','you are cool','\n','今天你怎么还不回来']
#     f.writelines(str_content)
#     f.close()
#
# with open('use.txt','r',encoding='utf-8')as file:
#     for line in file:
#         print(line)

#第二题
# with open('homework.txt','w',encoding='utf-8') as f1:
#     str=['my name is yang','\n','what is your name?']
#     f1.write('hi'+'\n')
#     f1.writelines(str)
#     f1.close()
#
# with open('homework.txt','r',encoding='utf-8')as f2:
#     print(f2.read())
#     print('======================================')
#     for line in f2:
#         print(line)

#第三题
# print('read的用法')
# f3=open('homework.txt','r',encoding='utf-8')
# print(f3.read())

# print('readlines()用法')
# f4=open('homework2.txt','w+',encoding='utf-8')
# str2_content=['hi,yangyan','\n','你好，杨艳']
# f4.writelines(str2_content)
# f4.close()
# with open('homework2.txt','r',encoding='utf-8')as f5:
#     print(f5.readline())
#     f5.close()
#
# print('readlines()方法')
# with open('homework.txt','r',encoding='utf-8')as f6:
#     print(f6.readlines())
#     f6.close()

'''
4.准备一张jpg图片,把图片中数据读书出来,并写入到文件my_img.jpg文件中, 操作完毕后尝试打开my_img.jpg文件看图片显示正不正常
'''
#rb wb :b二进制数据
with open('1.jpg','rb')as img_file:
    data=img_file.read()
with open('2.jpg','wb')as img2_file:
    img2_file.write(data)

