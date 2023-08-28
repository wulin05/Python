"""
演示lambda匿名函数：
匿名函数使用lambda关键字进行定义
定义语法：lambda 传入参数: 函数体(一行代码)

注意事项：匿名函数用于临时构建一个函数，只用一次的场景
匿名函数的定义中，函数体只能写一行代码，如果函数体要写多行代码，不可用lambda匿名函数，应使用def定义带名函数

"""


def test_func(add):
    result = add(1, 2)
    print(result)


# 通过lambda匿名函数的形式，将匿名函数作为参数传入，但是由于lambda没有名字，只能给test_func临时使用一次
test_func(lambda x, y: x + y)

# 可以看出 test_func(lambda x, y: x + y) 功能等于下面的代码
# def add(x, y):
#     # z = x + y
#     return x + y
#
#
# test_func(add)
