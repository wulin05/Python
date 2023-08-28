# 需求：定义一个元组,内容是:('周杰伦',11,['football','music']),
# 记录的是一个学生的信息(姓名、年龄、爱好)
# 通过元组的功能(方法),对其进行:
# 1.查询其年龄所在的下标位置 2.查询学生的姓名
# 3.删除学生爱好中的football 4.增加爱好:coding到爱好list内

tuple_list = ('周杰伦', 11, ['football', 'music'])
print(f"查询其年龄所在的下标位置是:{tuple_list.index(11)}")
print(f"查询学生的姓名:{tuple_list[0]}")

# 删除学生爱好中的football,方法一：
# del tuple_list[2][0]
# print(f"使用del方法删除学生爱好中的football后的结果是:{tuple_list}")

# 删除学生爱好中的football,方法二：
del_name = tuple_list[2].pop(0)
print(del_name)
print(f"使用pop方法删除学生爱好中的football后的结果是:{tuple_list}")
# 另外可以查询资料，切片的方式可以变相地删除元组的元素

# 增加爱好:conding到爱好list内
word = tuple_list[2].insert(0, 'coding')
print(word)  # 输出值是 None,因为list的insert方法无返回值
print(f"增加爱好:coding到爱好list内:{tuple_list}")

