"""
为什么会提出Python包的概念：
虽然基于Python模块，我们可以在编写代码的时候，导入许多外部代码来丰富功能
但是，如果Python模块太多了，就可能造成一定的混乱
基于此，可以通过Python包的功能来管理

什么是Python包：
从物理上看，包就是一个文件夹，在该文件夹下包含了一个_init_.py文件(必须存在)，该文件夹里可用于包含多个
模块文件，比如 my_package包下的: fir_module.py、sec_module.py、thi_module.py三个模块
或者: my_package_new包下的: my_module01.py、my_module02.py两个模块
如果包文件夹下没有_init_.py文件，那么该文件夹就只是普通的代码文件，而不是Python包了

从逻辑上看，包的本质依然是模块

总结:
Python包 总结:
1.什么是python包
  包就是一个文件夹,里面可以存放很多Python的模块(代码文件),通过包,在逻辑上将一批模块归为一类,方便使用。
2.__init__.py文件的作用
  创建包会默认自动创建的文件,通过这个文件来表示一个文件夹是Python的包,而非普通的文件
3.__all__ = [] 方式的作用
  在模块文件中 或 包文件下的__init__.py文件中 定义了 __all__ = [] 的作用是：
  控制 import * 能够导入的内容(或叫导入的 函数)
"""

# import my_package.fir_module
# import my_package.sec_module
#
# my_package.fir_module.info_print1()
# my_package.sec_module.info_print2()

print("---------------------------------------------------")
# 或者：
# from my_package import fir_module
# from my_package import sec_module
#
# fir_module.info_print1()
# sec_module.info_print2()

print("---------------------------------------------------")
# 又或者：
# from my_package.fir_module import info_print1
# from my_package.sec_module import info_print2
#
# info_print1()
# info_print2()

print("---------------------------------------------------")
# 也能通过my_package包中__init__.py文件中定义的__all__ = ['fir_module', 'sec_module'],
# 控制import * 能够导入的内容；
# 注意：刚创建my_package的Python包的时候，自动生成了_init_.py的文件，该文件里没有内容
# 那么，__all__变量是定义在_init_.py文件里，来实现功 import * 的功能
from pythonScript.my_package import *

fir_module.info_print1()
sec_module.info_print2()
# thi_module.info_print3()
# 这是因为在my_package包里的_init_.py文件中，
# __all__ = ['fir_module', 'sec_module']
# 没有 thi_module,所以 thi_module 被认为是未定义的：NameError: name 'thi_module' is not defined.

from pythonScript.my_package_new import *
# from pythonScript.my_package_new import my_module01, my_module02

my_module01.new_print1()
my_module02.new_print2()  # 同理,由于my_module02模块不在该my_package_new包下的
# __init__.py文件中定义的 __all__ = ['my_module01']中,所以,这样写会报错
# 但是如果使用：from pythonScript.my_package_new import my_module01, my_module02
# 则使用 new_print2() 功能的时候, 是ok的!


print("---------------------------------------------------")
# from my_package import fir_module, sec_module, thi_module
# 上面这条写法，就直接把my_package包下的3个模块文件添加进来


