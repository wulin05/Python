"""
演示以数据容器的角色，学习字符串的相关操作
作为数据容器,字符串有如下特点：
1.只可以存储字符串
2.长度任意(取决于内存大小)
3.支持下标索引
4.允许重复字符串存在
5.不可以修改(与元组相似)
6.支持while、for循环

"""
my_str = "linwu is a super boy"
# 通过下标索引取值
value1 = my_str[4]
value2 = my_str[-1]
print(value1)
print(value2)

# 字符串同元组一样，是无法修改的数据容器，注意是本身是不会变化的
# 所以.append、.insert()、.extend、.clear、del 字符串[下标]、字符串.remove()、字符串.pop()的操作，
# 会改变字符串本身的内容的方法都不可以
# 而 字符串.replace()、字符串.split、字符串.strip这三种都是得到了一个新的字符串或列表，而原字符串本身没有变化
# my_str[2] = "I"

# index方法
value3 = my_str.index("super")
print(f"查找字符串{my_str}中and的起始下标值是:{value3}")
print(f"查找字符串{my_str}中and的起始下标值是:{my_str.index('super')}")

# replace方法，语法：字符串.replace(字符串1,字符串2）
# 功能：将字符串内的全部：字符串1，替换为字符串2
# 注意：不是修改字符串1本身，而是得到了一个新的字符串
print(f"将{my_str}进行字符串替换后得到:{my_str.replace('linwu','林武')}")
new_my_str = my_str.replace("linwu","林武")
print(f"将{my_str}进行字符串替换后得到:{new_my_str}")

# split方法：字符串的分割
# 语法：字符串.split(分隔符字符串)
# 功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入一个类型为列表的对象中
# 注意：字符串本身不变，而是得到了一个 列表 对象
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到:{my_str_list},类型是:{type(my_str_list)}")

# strip方法：字符串的规整操作(只去除前后指定字符串，其他位置出现的不删除)
# 语法：字符串.strip()
name_str = " This is my first coding ! "
print(f"输出原字符串name_str的内容,前后都带有空格:{name_str}")

print(f"字符串{name_str}使用strip()去除前后空格后的结果:{name_str.strip()}")
new_name_str = name_str.strip()
print(f"字符串{name_str}使用strip()去除前后空格后的结果:{new_name_str}")

name_str = "12 This is my first coding 21"
print(f"{name_str}去除前后1和2两个字符后的结果是:{name_str.strip('12')}")
# 注意：12或21字符不在字符串的最前或最后，那么不会被删除
name_str = "12 This is my first coding 21 !"
print(f"{name_str}去除前后1和2两个字符后的结果是:{name_str.strip('12')}")
name_str = "!12 This is my 12 first coding 21 "
print(f"{name_str}前后有其他字符的时候，无法删除指定的1和2两个字符:{name_str.strip('12')}")

# 统计字符串中某字符串的出现次数
my_str = "linwu is a super boy boy boy!"
print(f"统计字符串{my_str}中boy出现的次数:{my_str.count('boy')}")
print(f"统计字符串{my_str}中s出现的次数:{my_str.count('s')}")

# 统计字符串的长度
print(f"统计字符串{my_str}中长度:{len(my_str)}")