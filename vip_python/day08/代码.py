

'''
    包的结构
    模块的使用
    模块的导入
    安装第三方模块
    模块的打包
'''
#包结构：如何把普通的目录转变为包结构?___init____py
#注意同一个包结构下面要避免模块的重名
#包名：同一个项目里面避免包名的重复
#模块名：注意同一个包结构下面要避免模块的重名


#模块导入方式：以一个内置函数为咧，math
# import导入：
import math  #模块名称
print(math.sqrt(9))

#2.from math import sqts
from math import sqrt
print(sqrt(9))

#3.from math import * 导入math所有的函数（非私有属性和方法）

#模块名称的概念：每一个模块对象都有一个__name__属性


#两个模块之间的相互导入

name='one_1'
print(name)

def get_name():
    print("我是one模块")
if __name__=='__main__':
    get_name()


#模块之间的相互叉导入的问题：
#1.import 语句放到方法定义的后边
#2. 把import语句一道函数的内部


# 模块的重复导入，从第二次开始不会被重新加载代码，不会执行

