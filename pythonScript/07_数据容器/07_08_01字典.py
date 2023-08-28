"""
字典的定义，和集合相似,同样使用{}，但是集合存储的元素是一个个的,而字典是存储键值对，如下语法：
{key:value,key:value,.....,key:value}
my_dict = {key:value,key:value,......,key:value}

定义空字典
my_dict = {}
my_dict = dict()

注意：定义空集合,只能通过:
my_set = set(),不能
my_set = {}
即,空集合只有一种写法：my_set = set(), 因为my_set = {}这种方式被空字典占用了!

字典和集合一样,不可以使用下标索引。但是字典可以通过key来取得对应的Value。
总结字典的特点：
1.可以容纳多个数据
2.可以容纳不同类型的数据
3.每一份数据是KeyValue键值对
4.可以通过Key获取到Value,Key不可重复(重复会覆盖)
5.不支持下标索引,没有下标索引的概念
6.可以修改(增加、删除、更新元素等)
7.支持for循环,不支持while循环
"""

# 定义字典
my_dict = {"王力鸿": 99, "周杰轮": 88, "林俊节": 77}

# 定义空字典的两种方式：
my_dict1 = {}       # 回顾：定义空集合只能用：my_set = set()，而不能使用 my_set = {}，因为这个定义方式被字典占用了。
print(f"输出my_dict1的类型：{type(my_dict1)}")
my_dict2 = dict()   # 注意，和定义空集合很类似：my_set = set()
print(f"输出my_dict2的类型：{type(my_dict2)}")

print("===============================================================")
# 定义重复key的字典：结果会后续的key内容覆盖之前的，即，"王力鸿"只出现一次，值为88
# my_dict = {"王力鸿":99, "王力鸿":88, "林俊节":77}
# print(f"重复key的字典my_dict1的内容是：{my_dict}")

# 从字典中基于key获取value,也可以说明字典和集合一样,不可以使用下标索引。但是字典可以通过key来取得对应的Value。
score = my_dict["王力鸿"]   # 注意，只有字典可以这样取出value值，列表、元组、字符串只能通过下标进行获取元素
print(f"获取王力鸿的value值：{score}")
