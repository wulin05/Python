"""
python演示对文件的读取
"""
import time

# 打开文件 - open(位置, 类型, 编码类型)
f = open("D:/以前の資料/Python/pythonScript/09_文件的操作/09_01-01.txt", "r", encoding="UTF-8")
print(type(f))
print("---------------------------------------------")

# 读取文件 - read(): 文件对象.read(num)
# num 表示要从文件中读取的数据长度(单位是字节)，如果没有传入num，那么就表示读取文件中所有的数据
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"读取全部内容的结果：{f.read()}")
# print(f"使用read读取文件内容的类型是：{type(f.read())}")  # 输出的类型是 str字符串
# print("---------------------------------------------")

# 读取文件 - readLines()：
# 使用f.readlines读取文件，得到的lines是列表类型，列表内的元素是字符串。
# lines = f.readlines()
# print(f"lines对象的类型是：{type(lines)}")
# print(f"lines对象的内容是：{lines}")
# f.close()
# print("---------------------------------------------")

# 读取文件 - readline()
# line1 = f.readline()
# print(f"第一行：{line1}")
# line2 = f.readline()
# print(f"第二行：{line2}")
# print(f"每一行输出的类型是：{type(line1),type(line2)}")  # 输出类型是str字符串
# print("---------------------------------------------")

# for循环读取文件内容
# for line in f:
#     print(f"循环读取每一行：{line}")
#     print(f"读取每一行line的类型是: {type(line)}")  # 输出类型是str字符串
#
# print("---------------------------------------------")

# time.sleep(500000)   # 使用time.sleep()模拟文件一直被python占用

# print("---------------------------------------------")

# 文件的关闭
f.close()  # 使用 对象.close()进行手动关闭文件，就可以对f对应的文件进行操作了

# with open 语法操作文件：使用with open打开文件后，程序运行后，自动将文件关闭，即 f.close()
# with open("D:/pythonScript/1-4部分的代码/test01.txt", "r", encoding="UTF-8") as f:
#     for line in f:
#         print(f"2-每一行数据是：{line}")
# time.sleep(1000)
