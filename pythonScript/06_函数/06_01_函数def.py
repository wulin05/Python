"""
①参数如果不需要，可以省略
②返回值如不需要，可以省略
③函数必须先定义后使用
"""


# def 函数名(传入参数):
#     函数体
#     return 返回值

# 定义函数
def say_hi():
    # 编写函数体输出信息
    print("Hi,我是黑马程序员，学Python来黑马")


# 调用函数
say_hi()

# 无返回值函数的返回内容
result01 = say_hi()
print(f"无返回值函数的返回内容：{result01}")
print(f"无返回值函数的返回类型：{type(result01)}")


# x,y,z是形式参数
def add(x, y, z):
    result02 = x + y + z
    print(f"{x} + {y} + {z}的计算结果是: {result02}")


# 1,2,3是实际参数
add(1, 2, 3)
