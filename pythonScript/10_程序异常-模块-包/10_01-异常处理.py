"""
为什么要捕获异常：
在可能发送异常的地方，进行捕获，当异常出现的时候，提供解决方式，而不是任由起导致程序无法运行下去
演示捕获异常
语法：
try:
    可能要发生异常的语句
except[异常名 as 别名]:     # [..]代表可选项
[else:]
    未出现异常时应做的事情
[finally:]
    不管出不出现异常都要做的事情
"""

# 基本捕获语法：其实就是捕获所有异常，因为在except后没有写明具体错误类型，对于出现异常后，
# 执行except下的语句：如下例：当abc.txt不存在，根据except语句，使用w模式创建abc.txt文件
try:
    f = open("abc.txt", "r", encoding="UTF-8")
except:
    print("出现异常，因为文件不存在，那么将使用w模式去创建文件")
    f = open("abc.txt", "w", encoding="UTF-8")

print("--------------------------------------------------------------------")
# 捕获指定的异常
try:
    print(name)
    # 1 / 0
except NameError as e:  # 如果使用 1/0 的话,那么是division by zero,不是NameError的错误,没有捕获到,报错！
    print("出现了变量未定义的异常")
    print(e)  # name 'name' is not defined

print("--------------------------------------------------------------------")
try:
    1 / 0
except ZeroDivisionError as f:
    print("0不能作为除数")
    print(f)  # division by zero

print("--------------------------------------------------------------------")
# 捕获多个异常
try:
    print(1 / 0)  # 任意一个错误都能输出：出现了变量未定义 或者 除以0的异常错误
    print(name)
except (NameError, ZeroDivisionError) as g:
    print("出现了变量未定义 或者 除以0的异常错误")
    print(g)  # print(1 / 0)和print(name)都是错误，print(g)结果是：第一个错误
# 未正确设置捕获异常类型，将无法捕获异常

print("--------------------------------------------------------------------")
# 捕获所有异常
try:
    print(value)  # 以下三种，任意一个都会输出："出现异常了,这里是捕获所有异常"
    1 / 0
    f = open("aaa.txt", "r", encoding="UTF-8")
except Exception as i:  # Exception属于顶级异常，其他类、对象等等异常，都是它的小弟
    print("出现异常了,这里是捕获所有异常")

print("--------------------------------------------------------------------")
# 没有异常行为，执行语句 else：
try:
    print("hello,linwu")
except Exception as j:
    print("出现异常了")
else:
    print("好高兴，没有异常。")

print("--------------------------------------------------------------------")
# finally表示的是无论是否异常都要执行的代码，例如：关闭文件
try:
    f = open("ccc.txt", "r")
except Exception as k:
    f = open("ccc.txt", "w", encoding="UTF-8")
else:
    print("说明没有异常，ccc.txt文件已经存在")
finally:
    print("我是finally,有没有异常我都要执行!")
    f.close()
