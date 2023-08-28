# 函数作为参数传递
# 函数传入是以计算逻辑的传递，不是之前使用的数据作为参数传入
# 之前的函数学习中，我们一直使用的函数，都是接受数据作为参数传入：
# 数字、字符串、字典、列表、元组
# 其实，函数本身也可以作为参数传入到另外一个函数内
# 示例：

def test_func(add):
    result = add(1, 2)
    print(f"add参数的类型是：{type(add)}")
    print(result)


def add(x, y):
    return x + y


test_func(add)
