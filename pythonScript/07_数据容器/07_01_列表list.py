# 数据容器是一种可以存储多个元素的Python数据类型
# Python的数据容器有：list(列表)、tuple(元组)、str(字符串)、set(集合)、dict(字典)
"""
  定义空列表:
  变量名称 = []
  变量名称 = list()
  字面量：[元素1，元素2，元素3，.....]
  定义变量：
  变量名称 = [元素1，元素2，元素3，.....]
"""

# 定义了name_list,my_list,my_list_01三个列表
name_list = ['itheima', 'itcast', 'python']
print(name_list)
print(type(name_list))

my_list = ['linwu', 666, True]
print(my_list)
print(type(my_list))

my_list_01 = [[1, 2, 3], ['aaa', 'bbb', 'ccc'], [True, False]]
print(my_list_01)
print(type(my_list_01))

# 列表的下标索引,从左向右的方向，从0开始，依次递增
print(name_list[0], name_list[2])
print(my_list[1], my_list[2])
print(my_list_01[0], my_list_01[1])

# 列表的下标索引,从右向左的方向，从-1开始，依次递减
print(my_list[-1], my_list[-2], my_list[-3])

# 对于嵌套的列表，同样支持下标索引
print(my_list_01[0][0], my_list_01[0][1], my_list_01[2][0], my_list_01[2][1])
