"""
模块(Module)，是一个Python文件，以.py结尾，模块能定义函数、类和变量，模块里也能包含可执行的代码
模块的作用：模块可以快速地实现一些功能，比如实现和时间相关的功能：time模块
可以认为一个模块就是一个工具包
大白话：模块就是一个Python文件，内含类、函数、变量等，我们可以导入进行使用

语法：[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
常用组合形式如：
import 模块名
from 模块名 import 类、变量、方法等
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名

比如：09_02_文件的写入.py这个文件里的time模块
import time       # import 模块名
                  # import 模块名1, 模块名2, 模块3,....
time.sleep(1000)  # 模块名.功能名()

模块的导入一般写在代码文件的开头位置
"""

import time

# 使用import导入time模块的全部功能，并使用time.sleep方式来调用sleep功能(函数)
# 导入Python内置的time模块(time.py这个代码文件)

print("您好!")
time.sleep(3)  # 通过. 就可以使用模块内的全部功能(其实就是代码：类、变量、函数)
print("我也好!")

print("-------------------------------------------------------------------")
# 使用from导入time的sleep功能(函数)：其实就是只用到time模块下的sleep功能(函数)
# time模块下的其他函数不导入，也就没有啦
# from 模块名 import 功能名
# 功能名()
# 具体实例：

from time import sleep

print("开始")
sleep(2)   # 只用了time模块中的sleep功能
print("结束")

print("-------------------------------------------------------------------")
"""
使用 * 导入time模块的全部功能
* 表示全部的意思，其实与 import time的功能一样，都是将time
模块的所有类导入，但是*的方式，就能直接用sleep(),不需要再
使用time.sleep()的方式了
"""
from time import *
print("开始")
sleep(2)
print("结束")

print("---------------------------------------------------")
# import 模块名 as 别名
# from 模块名 import 功能 as 别名
import time as tt

print("1-linwu")
tt.sleep(3)
print("2-linwu")

from time import sleep as ts

print("1-WULIN")
ts(5)
print("2-WULIN")
