#print ("hello，小绵羊")

# String1='xiaoming '
# String2="xiaohua"
# print(String1)
# print(String2)

#type:判断类型，如下
# Str="明天开始上班啦！"
# data1=10.0
# data2=4
# date3=5
# LIst={6789}
# myList=[1,2,3,4]
# mydictionary={"Monday":1,"Tuesday":2}
# print(type(str))
# print(type(data1))
# print(type(myList))
# print(type(mydictionary))
# print(data2+date3)
# print(Str+Str(date3))

#练习：定义列表和字典，分别打出第一个字符
# 分别打出第一个字符List=["hello","joy"]#定义列表
# mydict={"name":"john","sex":"boy"}#定义字典
# print(List[0])#输出列表的第一个字符
# print(mydict["name"])#字典用key来取值
# print(mydict.keys())#输出所有键
# print((mydict.values()))#输出所有值

#练习：从键盘输入一行字符串，并打印出来（2x，3x实现）
# Str = input("Pelase input your name \n？")
# Str2 = input("Pelase input your passward")
# print(Str)
# print(Str2)
# print(Str + Str2)
# print(Str2 * 3)


#求整
# print(3//5)
# print(3/5)
# #求余
# print(5%3)

#比较运算符，逻辑运算符（and or not）
# string1=True
# string2=False
# string3=True
# if string1==True and string2==True:
#     print("ok")
# else:
#     print("Not")

#运算符
# num1=5
# num2=3
# num3=4
# num3+=num1#等价 num3+num1
# print(num3)

#成员运算 in, not in

# string1="I am Chinese!"
# if "am" in string1:
#     print("YES")
# else:
#     print("NO")
#
# 内置常量
# mytype=None
# print(type(mytype))

#练习：编写一个程序，输入两个人的成绩，输出两个人成绩的平均值
# str1=input("请输入第一个成绩：")
# str2=input("请输入第二个成绩: ")
# print((str1+str2)/2)

#下标访问,截取字符串的一部分
# var="hell oword"
# print(var[0])
# print(len(var))#打印字符串的长度
# print(var[2:5])#截取2-5的元素
# print(var[0:])#全部截取
# print(var[:])#全部
# print(var[2:-2])#2- -2
# #步长截取
# print(var[::-2]) #倒序，每隔2个
# print(var[::2]) #每隔2个


# my_name="joy"
# my_name.capitalize()#s首字母大写
# my_age=25
# print("my name is {},my age is {}".format(my_name,my_age))
# print("my name is {1},my age is {0}".format(my_name,my_age))
# print("my name is {name},my age is{age}".format(name=my_name,age=my_age))

#字符串的内建函数
initial_string="welcome to China  "
space_string="  "
#captalize() 函数将一个字符串的第一个字母大写
print(initial_string.capitalize())
#endswith(suffix, start=0, end=len(string)) 函数,判断字符串是否是以某字符串结尾的
if initial_string.endswith(" "):
    print("ok")
#find(str, start=0, end=len(string)) 函数,在字符串的某指定位置查找某字符串
if initial_string.find("t"):
    print(initial_string.find("t"))
#index(str, start=0, end=len(string)) 函数,功能上与 find() 相同，只是在未找到子字符串是抛出异常
if initial_string.index("e"):
    print(initial_string.index("e"))
#isspace() 函数,判断该字符串是否只包含空格
if initial_string.isspace():
    print("it is space")
else:
    print("it is not space")
#islower() 函数,判断该字符串中是否只是小写字母
if initial_string.islower():
    print(initial_string.islower())


initial_string="welcome to china  "
score_list=['90','88','98','79']
#join(seq) 函数,用该字符串连接某字符序列(seq)
scores=','.join(score_list)
print(type(scores))
print(scores)

print(len(initial_string))
print(len(score_list))
#
print(initial_string.lstrip())
print(len(initial_string.lstrip()))

print(initial_string.rsplit())
print(len(initial_string.rsplit()))

print(initial_string.strip())
print(len(initial_string.strip()))

if initial_string.isupper():
    print(initial_string.lower())

if initial_string.startswith("H"):
    print(initial_string.replace("H","E"))
    print(len(initial_string("H","E")))
    print(initial_string.replace("H","E").strip())
    print(len(initial_string.replace(("H","E").strip())))

print(type(initial_string))
print(initial_string.split(" "))
print(type(initial_string.split(" ")))

print(u"中秋快乐")



