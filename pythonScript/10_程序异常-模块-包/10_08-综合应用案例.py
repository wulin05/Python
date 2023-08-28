"""
演示异常、模块、包的综合案例
需求：
    创建一个自定义包，名称为：my_utils(我的工具)
在包内提供2个模块：
    str_util.py(字符串相关工具，内含：)
    ・ 函数：str_reverse(s),接受传入字符串，将字符串反转返回
    ・ 函数：substr(s, x, y),按照下标x和y，对字符串进行切片
    file_util.py(文件处理相关工具，内含)
    ・ 函数：print_file_info(file_name),接收传入文件的路径，打印文件的全部内容
           ，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
    ・ 函数：append_to_file(file_name, data),接收文件路径以及传入数据，将数据
            追加写入到文件中
"""
import fileinput

# 使用下列两种方式导入功能(函数）
"""
方式一 中如果最后使用 as stl、as fil 别名的方式,那么调用的时候就非常方便了
pythonScript.my_utils.str_util 这么长的一段就可以用 stl 代替了
file_util 这个也可以用 fil 代替了
即,可以写成(仅各取一个)：
print(stl.str_reverse("曾经沧海难为水"))
fil.print_file_info("D:/以前の資料/Python/pythonScript/10_程序异常-模块-包/file.txt")
"""

import pythonScript.my_utils.str_util            # as stl
from pythonScript.my_utils import file_util      # as fil

print(pythonScript.my_utils.str_util.str_reverse("曾经沧海难为水"))
print(pythonScript.my_utils.str_util.substr("曾经沧海难为水", 2, 5))

file_util.print_file_info("D:/以前の資料/Python/pythonScript/10_程序异常-模块-包/file.txt")
file_util.append_to_file("D:/以前の資料/Python/pythonScript/10_程序异常-模块-包/file.txt", "\n调用插入1")



# 方式二：
# from pythonScript.my_utils import *
#
# print(str_util.str_reverse("再见,王小偌!"))
# print(str_util.substr("再见,王小偌!", 1, 4))
#
# file_util.print_file_info("D:/以前の資料/Python/pythonScript/10_程序异常-模块-包/file.txt")
# file_util.append_to_file("D:/以前の資料/Python/pythonScript/10_程序异常-模块-包/file.txt", "调用插入2")


