# 位置参数：调用函数时根据函数定义的参数位置来传递参数
# 关键字参数：函数调用时通过 "键=值" 方式传递参数,作用：可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求

def user_info(name, age, gender):
    print(f"您的名字是{name}, 年龄是{age}, 性别是{gender}")


user_info('TOM', 20, '男')  # 全部位置参数
user_info(name='小美', age=18, gender='女')  # 全部关键字参数
user_info(age=80, gender='男', name='老林')  # 关键字参数可以不按照参数定义的顺序传参
user_info('小芳', gender='女', age=12)  # 位置参数和关键字参数混用


# user_info(gender='男', '小周', age=25)  这种方式报错，位置参数必须在关键字参数的前面
# user_info('女', 20, name='小周')  # 这时候也报错，因为name有两个值了：女、小周

# 缺省参数（默认值）：缺省参数也叫默认参数，用于定义函数，为参数提供默认值
# 调用函数时可不传该默认参数的值（注意：所有位置参数必须出现在默认参数前，包括函数定义和调用
# 作用：当调用函数时没有传递参数，就会使用缺省参数对应的值

def user_detail(name, age, sex='男'):  # 缺省参数一定在后面，例如 age定义了缺省值，sex没有定义缺省值，程序报错
    print(f"您的名字是{name},年龄是{age},性别是{sex}")


user_detail("林武", 36)
user_detail("Rose", 18, "女")


# 不定长参数：不定长参数也叫可变参数，用于不确定调用的时候会传递多少个参数（不传参也可以）的场景
# 作用：当调用函数时不确定参数个数时，可以使用不定长参数
# 不定长 - 位置不定长，*号
# 传递的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组（tuple），args是元组类型，这就是位置传递

def user_avi(*args):
    print(f"args参数的类型是：{type(args)}，内容是：{args}")


user_avi('TOM')
user_avi('Tina', 18, '女')


# 不定长 - 关键字不定长，**号
# 注意：参数必须是以"键=值"形式，所有的"键=值"都会被kwargs接受，同时会根据"键=值"组成字典
def user_all(**kwargs):
    print(f"kwargs参数的类型是：{type(kwargs)}，内容是：{kwargs}")


# {'name': 'Jaden', 'age': 19, 'id': 110}
user_all(name='Jaden', age=19, id=110)