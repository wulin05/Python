# 将数字类型转换成字符串
num_str = str(11)
print(type(num_str), num_str)

float_str = str(11.345)
print(type(float_str), float_str)

# 将字符串转换成数字
num1 = int("11")
print(type(num1), num1)

num2 = float("11.345")
print(type(num2), num2)

# 万物皆可转字符串，因为只要将内容用双引号括起来
# 但字符串不一定能转化为数字，除非字符串的内容都是数字
"""
num3 = int("黑马程序员")
print(type(num3),num3)
"""

# 字符串字面量之间的拼接
print("学IT来黑马" + "月薪过万")

# 字符串字面量和字符串变量之间的拼接
name = "黑马程序员"
address = "建材城东路9号院"
tel = 18960287009
# 错误方式：+是无法拼接数字的
# print("我是：" + name + "，我的地址是：" + address + ",我的电话是：" + tel)


# % 表示：我要占位
# s 表示：将变量变成字符串放入占位的地方
message = "学IT来 %s" % name
print(message)

# 正确应该使用字符串格式化方式
