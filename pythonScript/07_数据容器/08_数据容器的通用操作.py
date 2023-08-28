"""
数据类型分类：
1.从是否支持下标索引:
  (1) 支持: 列表、元组、字符串 --序列类型
  (2) 不支持: 集合、字典  --非序列类型
2.从是否支持重复元素:
  (1)支持: 列表、元组、字符串 --序列类型
  (2)不支持: 集合、字典  --非序列类型
3.从是否可以修改:
  (1)支持: 列表、集合、字典
  (2)不支持: 元组、字符串

演示数据容器的通用功能
1.注意: 只有字典转字符串的时候,value值能被保存下来，转成其他类型的时候,value值都丢失了。
2.其他的数据类型(列表、元组、字符串、集合)都不能转成字典类型,因为字典是键值对。
3.使用sorted方法对数据容器进行排序后,所有的数据容器(列表、元组、字符串、集合、字典)都变成列表了。
  sorted(序列,[reverse=True]）
"""

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

# len元素个数
print(f"列表 元素个数有：{len(my_list)}")
print(f"元组 元素个数有：{len(my_tuple)}")
print(f"字符串 元素个数有：{len(my_str)}")
print(f"集合 元素个数有：{len(my_set)}")
print(f"字典 元素个数有：{len(my_dict)}")

print("======================================")
# max最大元素
print(f"列表 最大元素是：{max(my_list)}")
print(f"元组 最大元素是：{max(my_tuple)}")
print(f"字符串 最大元素是：{max(my_str)}")
print(f"集合 最大元素是：{max(my_set)}")
print(f"字典 最大元素是：{max(my_dict)}")

print("======================================")
# min最小元素
print(f"列表 最小元素是：{min(my_list)}")
print(f"元组 最小元素是：{min(my_tuple)}")
print(f"字符串 最小元素是：{min(my_str)}")
print(f"集合 最小元素是：{min(my_set)}")
print(f"字典 最小元素是：{min(my_dict)}")

print("======================================")
# 类型转换：容器转列表
print(f"列表转列表的结果是：{list(my_list)}")
print(f"元组转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表的结果是：{list(my_str)}")
print(f"集合转列表的结果是：{list(my_set)}")
print(f"字典转列表的结果是：{list(my_dict)}")

print("======================================")

# 类型转换：容器转元组
print(f"列表转元组的结果是：{tuple(my_list)}")
print(f"元组转元组的结果是：{tuple(my_tuple)}")
print(f"字符串转元组的结果是：{tuple(my_str)}")
print(f"集合转元组的结果是：{tuple(my_set)}")
print(f"字典转元组的结果是：{tuple(my_dict)}")

print("======================================")

# 类型转换：容器转字符串
print(f"列表转字符串的结果是：{str(my_list)}")  # 虽然输出好像没有变化，其实列表和元组："[1,2,3,4,5]","(1,2,3,4,5)"
print(f"元组转字符串的结果是：{str(my_tuple)}") # 实际是因为双引号""在输出时自动被省略了。
print(f"字符串转字符串的结果是：{str(my_str)}")
print(f"集合转字符串的结果是：{str(my_set)}")
print(f"字典转字符串的结果是：{str(my_dict)}")

print("======================================")
# 类型转换：容器转集合
print(f"列表转集合的结果是：{set(my_list)}")
print(f"元组转集合的结果是：{set(my_tuple)}")
print(f"字符串转集合的结果是：{set(my_str)}")
print(f"集合转集合的结果是：{set(my_set)}")
print(f"字典转集合的结果是：{set(my_dict)}")

print("======================================")

# sorted排序：注意输出结果。。。。全部都变成了列表了！！！
my_list1 = [10, 9, 8, 7, 6]
my_tuple1 = (7, 1, 5, 2, 8)
my_str1 = "ldoncafq"
my_set1 = {6, 4, 3, 9, 2}
my_dict1 = {"key3": 3, "key1": 1, "key5": 5, "key2": 2, "key4": 4}
print(f"列表对象的排序结果：{sorted(my_list1)}")
print(f"元组对象的排序结果：{sorted(my_tuple1)}")
print(f"字符串对象的排序结果：{sorted(my_str1)}")
print(f"集合对象的排序结果：{sorted(my_set1)}")
print(f"字典对象的排序结果：{sorted(my_dict1)}")

# 反向排序
print(f"列表对象的反向排序结果：{sorted(my_list1, reverse=True)}")
print(f"元组对象的反向排序结果：{sorted(my_tuple1, reverse=True)}")
print(f"字符串对象的反向排序结果：{sorted(my_str1, reverse=True)}")
print(f"集合对象的反向排序结果：{sorted(my_set1, reverse=True)}")
print(f"字典对象的反向排序结果：{sorted(my_dict1, reverse=True)}")
