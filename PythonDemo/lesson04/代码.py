'''
异常处理


'''


# try:
#     a=1/0
# except:
#     print('error')
# else:#没有异常还会执行else
#     print('None')
# finally:#无论有没有异常，都会被执行
#     print('must be execute')


#如何打开文件open('路径','')

#文件异常
# try:
#     fp=open('aaa.txt','w')
#     fp.write('hello word')
# except IOError:
#     print(IOError)
# finally:
#     try:
#      fp.close()
#      print('file is closed')
#     except:
#         print('None Error')


#输入输出异常
try:
    fp=open('aa','r')
    fp.write('333')
    a=input('input a num：')
    c=int(a)
    if c==2:
        b=c/0
except ValueError:
    print("输入错误")
except ZeroDivisionError:
    print('分母不能为零')
except IOError:
    print('其他异常')
finally:
    print('执行完毕')


