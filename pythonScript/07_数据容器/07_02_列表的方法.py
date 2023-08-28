"""
演示数据容器之:list列表的常用操作，也叫列表的方法
1.查找列表元素的下标索引： 列表.index(元素)
2.列表[下标x] = 元素
3.列表.insert(下标, 元素)
4.列表.append(元素)
5.列表1.extend(列表2)
6.del.列表[下标x]
7.列表.pop(下标)
8.列表.remove(元素)
9.列表.clear()
10.列表.count(元素)
11.len(列表）
"""
# 1.1 查找某元素在列表内的下标索引,语法： 列表.index(元素)
name_list = ['aaa', 'bbb', 'ccc']
index = name_list.index("aaa")
print(f"aaa在列表中的下标索引值是:{index}")

# 1.2 修改特定下标索引的值
name_list[0] = 'linwu'
print(f"列表被修改元素值后,结果是:{name_list}")

# 1.3 在指定下标位置插入元素
# 语法: 列表.insert(下标,元素): 在指定的下标位置，插入指定的元素
name_list.insert(1, "wulin")
print(f"列表插入元素后,结果是:{name_list}")
name_list.insert(-1, "王小偌")
print(f"列表的最后插入元素后,结果是:{name_list}")
# 实际从结果看,不是在最后插入"王小偌",而是在倒数第二个位置。其实想要在最后插入,就用下面的append方法！

# 1.4 在列表的尾部追加'''单个'''新元素
name_list.append("ddd")
print(f"列表尾部插入元素后,结果是:{name_list}")

# 1.5 在列表的尾部追加'''一批'''新元素
new_list = [1, 2, 3]
name_list.extend(new_list)
print(f"列表在追加了一个新的列表后,结果是:{name_list}")

# 1.6 删除指定下标索引的元素(两种方式)
# 1.6.1 方式一： del 列表[下标]
del name_list[0]
print(f"列表删除元素后结果是:{name_list}")

# 1.6.2 方式二： 列表.pop(下标), 比del的方法,不仅仅原列表的元素被删除,而且将取出的元素作为返回值！
# 补充一个内容：当列表或者元组中嵌套列表的情况，使用pop删除元素的方式是
# 列表名(或元组名)[下标].pop(下标)

element = name_list.pop(6)
print(f"通过pop方法取出元素后结果是:{name_list}")
print(f"取出的元素是:{element}")

# 1.7 删除某元素在列表中的第一个匹配项
my_list = ["a", "a", "b", "b", "c"]
my_list.remove("b")
print(f"通过remove方法移除元素后,列表的结果是:{my_list}")

# 1.8 清空列表
my_list.clear()
print(f"列表被清空了,结果是:{my_list}")

# 1.9 统计列表内某元素的数量
my_list = ["a", "a", "b", "b", "c", "d", "e", "e"]
count = my_list.count("b")
print(f"输出列表中b的数量是:{count}")
print(my_list.count("b"))
print(f"输出列表中b的数量是:{my_list.count('b')}")

# 2.0 统计列表中全部的元素数量
count = len(my_list)
print(f"列表中的元素总共有:{count}个")
print(len(my_list))


