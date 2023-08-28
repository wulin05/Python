"""
案例：新建一个python文件，命名为my_module1,并定义test函数
注意：
     每个Python文件都可以作为一个模块，模块的名字就是文件的名字，
     也就是说，自定义模块名必须要符合标识符命名规则
"""
# 调用 my_module1 模块，其实就是直接使用模块的文件名，就能使用该模块下的test功能(函数)了!!!
import my_module1  #

# 这个注意看,导入my_module1模块竟然会输出10,这是因为my_module1中有test(2, 5)进行测试,这个结果会在这里输出
# 所以,才会提到在my_module1模块中使用  if __name__ == '__main__':
#                                      test(2, 5)
# 这种方式,避免在 my_modele1的模块中进行了test的测试,会把结果输出到这边!

my_module1.test(10, 15)
# 也可以使用10_03-python介绍的模块导入方式： from my_module1 import test
# 那么调用模块的方法：                     test(10, 15)

# 注意事项：在my_module2.py和my_module3.py两个文件中都定义了my_test()功能(函数):
# 分别为：
# 模块1：my_module2.py
# def my_test(a, b):
#     print(a + b)
# 模块2：my_module3.py
# def my_test(a, b):
#     print(a - b)
# 下面两条是导入不同名称的模块，但调用功能的名称一样，都名为：my_test
from my_module2 import my_test
from my_module3 import my_test

# 调用相同名称的功能代码(函数)，后面的会把前面的覆盖了:注意看，前一条是灰的，后面一条颜色正常
my_test(1, 1)
