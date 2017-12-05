#1.
#新建一个python项目mysite, 建立一级包名为: myapp
#在myapp中建立两个模块one.py / two.py
#在one.py写入name =‘tom’
#在two.py中一个函数打印输出one.py中name变量
#并在两个模块中判断是否是在执行模块还是被导入模块
#在two.py中使用reload

#3
#把two.py文件打包

#3.
#写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于6, 如果大于6, 截取前4位, 否则直接打印输出



def func(content):
    if isinstance(content, (str,list,tuple)):
        if len(content)> 6:
            print(content[:4])
        else:
            print(content)
    else:
        print("输入有误！")
func((1,2,3))