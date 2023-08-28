# num是局部变量，出了函数test_a外就无效
def test_a():
    num = 100
    print(num)


test_a()
# print(num) 　　
# 程序会报错，因为num是局部变量

# num_01是全局变量,在函数体内和函数体外都能够被调用
num_01 = 200


def test_01():
    print(f"test_01:{num_01}")


def test_02():
    print(f"test_02:{num_01}")


test_01()
test_02()
print(num_01)
print("--------------------------------------------------------")

# num_02是全局变量,在函数体内修改num_02值不会改变num_02在函数外部的值
# 如果函数体内声明num_02为global变量,那么修改num_02的值,函数外也会变化

num_02 = 300


def test_03():
    print(f"test_03:{num_02}")


def test_04():
    num_02 = 999  # 其实函数内部的num_02和外部num_02没有关系，程序这边其实也提示了：重命名该元素
    print(f"test_04:{num_02}")


def test_05():
    global num_02
    num_02 = 9999
    print(f"test_05:{num_02}")


test_03()
test_04()
print(num_02)
test_05()
print(num_02)
