"""
函数的定义
方法的定义
函数和方法功能一样，有传入参数，有返回值，只是方法的使用格式不同
函数的使用： num = add(1, 2)
方法的使用： student = Student()
           num = student.add(1, 2)
"""


# 函数add的定义
def add(x, y):
    return x + y


# 方法的定义
class Student:
    def add(self, y):
        return self + y
