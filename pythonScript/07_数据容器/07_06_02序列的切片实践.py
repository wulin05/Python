# 字符串："万过薪月,员序程马黑来,nohtyP学"
my_str = "万过薪月,员序程马黑来,nohtyP学"
# 1.要求：使用学过的任何方式，得到"黑马程序员"
# 可供参考方式：1，倒序字符串，切片取出，然后倒序
#             2. split分割","，replace替换"来"为空，倒序字符串

# 使用双切片，第一次切片[::-1]得到正序的字符串，再切片[9:14]，取出想要的结果：黑马程序员
result = my_str[::-1][9:14]
print(f"方法一: {result}")

print("===================================")

# 使用上述的思路，其实可以得出另外一个方法：正序切片得到：员序程马黑，再直接倒序输出。
result_new = my_str[5:10][::-1]
print(f"方法二: {result_new}")

print("===================================")

print(f"方法三: {my_str[-10:-15:-1]}")

print("===================================")

# 直接使用倒序切片的方式获取结果：黑马程序员
result1 = my_str[9:4:-1]
print(f"方法四: {result1}")

print("===================================")

print("方法五：")
result2 = my_str.split(",")
print(result2)  # 字符串split分割后，得到的是一个列表，列表的元素是字符串，而本身字符串也是一种数据容器
new_result2 = result2[1].replace("来", "")
print(new_result2)  # 对列表的第二个元素：即，对字符串"员序程马黑来"的"来"这个字符使用空字符进行替换,得到一个新的字符串"员序程马黑"
print(f"{new_result2[::-1]}")  # 最后在进行序列的切片操作，即：序列[起始下标:结束下标:步长]

print("===================================")

print("方法六：")
# 上面可以直接用一条命令表示： my_str.split(",")[1].replace("来","")[::-1]
print(f"{my_str.split(',')[1].replace('来', '')[::-1]}")

print("===================================")
print("对于方法五、六的具体剖析: ")
# 其实我这里的疑问是:经过split(',')后,字符串就得到了一个列表,列表中好像没有提到有replace方法呀?
# 很好,有这个疑惑,那么我们就一步步来看看每次步骤下得到的类型:
print(f"{my_str.split(',')}的类型是: {type(my_str.split(','))}")
print(f"{my_str.split(',')[1]}的类型是: {type(my_str.split(',')[1])}")
"""
注意看输出结果,可以得知: my_str.split(',')这步得到的是列表, 
my_str.split(',')[1], 这步得到的是字符串
所以还是得用字符串的replace方法,而不能用列表list的remove方法了。
my_str.split(',')[1].remove("来")会报错!
"""
print(f"{my_str.split(',')[1].replace('来', '')}")
print(f"{my_str.split(',')[1].replace('来', '')[::-1]}")

