# 需求：有如下一个列表对象：

my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']

# 最终需求：得到一个集合，由于集合有自动去重功能，所以得到的集合是：{'黑马程序员', '传智播客', 'itheima', 'itcast', 'best'}

# 流程：
# 1.定义一个空集合
my_set = set()
print(f"定义空集合my_set,内容为：{my_set}")

# 2.通过for循环遍历列表
for element in my_list:
    my_set.add(element)

# 打印输出集合，默认集合自动去重
print(f"列表my_list的内容是：{my_list}")
print(f"通过for循环后,得到的集合my_set的内容是：{my_set}")

print("----------------------------------------------------------")
# 直接通过强制类型转换,将一个list列表转换位set集合:
my_list01 = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
my_set01 = set(my_list01)
print(my_set01)


