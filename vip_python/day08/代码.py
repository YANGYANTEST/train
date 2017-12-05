

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
#重复导入模块，需要在最后＋  reload()   #参数-----》模块名称


'''
模块相关的特殊：__import___具有相关



'''
# import sys
# print(dir(sys))
#
# sys=__import__('sys')   #参数：一定是字符串
# print(sys)

__import__('os').system('dir')

#del sys.modules   #modules字典结构（模块名称，模块路径）

#除了内置模块和库之外，第三方模块和库

#包管理   安装模块/库
# pip install 模块名称/库名称 （推荐）
#pip uninstall 卸载模块名称/库名称

#easy install 模块名称/库名称（不推荐使用）