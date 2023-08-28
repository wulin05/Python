# 给定一个字符串："itheima itcast boxuegu"

my_list = "itheima itcast boxuegu"
print(my_list)

# 统计字符串内有多少个"it"字符
print(f"字符串{my_list}中有{my_list.count('it')}个it字符")

# 将字符串内的空格，全部替换为字符："|"
# print(f"{my_list.replace(' ', '|')}")
new_my_list = my_list.replace(' ', '|')
print(f"字符串{my_list}被|替换空格后,得到new_my_list的类型是: {type(new_my_list)},内容是: {new_my_list}")

# 并按照"|"进行字符串分割，得到列表
my_str_list = new_my_list.split("|")
print(f"字符串{new_my_list}按照|分割后得到列表my_str_list的类型是: {type(my_str_list)},内容是: {my_str_list}")

# 从上述的replace方法是得到新的字符串容器，split方法是得到新的列表容器！！
# 总之不会改变原字符串的值,都是生成新的字符串或新的列表
