

#死循环
# while True:
#     print("hi")
#
# week_day={"Sunnday":'SUN',"Tursday":"Tus"}

# n=0;
# languages=['c','java','python','c++','js']
# for languages in languages:
#     languages=='js'
#     break;
#     n+=1
#     print(languages)

#range函数
# for i in range(6):
#     print(i)
#
# sum=100;

#continue 在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
#break  在语句块执行过程中终止循环，并且跳出整个循环
#pass  pass是空语句，是为了保持程序结构的完整性。

# languages=['c','java','python','c++','js']
# n = 0;
# for languages in languages:
#     if languages=='java':
#         #continue
#         break
#     n+=1
#     print(languages)
#     print(n)
#
# my_result=[x for x in languages if x=="python"]
# print(my_result)


#列表去重


#定义一个函数
#三角形的边长和面积

def get_area_triangle(width,height):
    return width * height* (1/2)
result=get_area_triangle(1,5)
print(result)

#作业：模拟银行系统登陆，输入错误三次，报错

count=0
Real_Username = "test"
Real_Password = 123456

for i in range(3):
    Password = input("请输入密码:")
    if Real_Username == Real_Username and Password == Real_Password:
        print("登录成功")
        break
    else:
        print("登录失败")
    count += 1
    break

