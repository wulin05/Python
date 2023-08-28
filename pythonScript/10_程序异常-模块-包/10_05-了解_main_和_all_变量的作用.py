"""
在10_04-python自定义模块和使用中，创建的三个模块文件：my_module1.py、my_module2.py
my_module3.py，如果在各自文件中直接使用 main()，执行后就会输出结果
但是，我们不希望在10_04-python.py文件中调用这三个模块的功能时，把结果也输出给我们，我们更希望
是在自己的文件中，使用自己定义的参数，来得出结果，所以，引申出__main__变量的作用
即：
" if __name__ == '__main__': "  表示，只有当程序是直接执行的才会进入if内部，
如果是被导入的，则if无法进入

具体请到my_module1.py、my_module2.py、my_module3.py这三个文件中查看

注意事项：不同模块，同名的功能，如果都被导入，那么后导入的会覆盖先导入的
"""

# from my_module1 import test
# from my_module2 import my_test
# from my_module3 import my_test
#
# test(10, 9)
# my_test(10, 9)


# 关于模块文件中的_all_变量，当使用`from xxx import *`导入时，只能导入列表中的元素
# 如 my_module4.py这个模块文件：
from my_module4 import *  # * 代表__all__ = ['函数1', '函数2',....,'函数n']
test_a(1, 2)
test_b(100, 1)   # test_b函数就用不了了，因为在 my_module4.py 文件中的[]中，只定义了test_a