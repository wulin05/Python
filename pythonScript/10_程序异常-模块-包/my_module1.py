def test(a, b):
    print(a * b)


test(2, 5)    # ----> 可以直接在模块文件直接调用功能test()

# 直接输入main回车后，就会出现下面的 if 一行，然后把 test(2, 5)写到再下面一行后，就可以
# 直接运行测试，也不会在其他地方调用该模块的test功能，出现test(2, 5)这个结果。
# if __name__ == '__main__':
#     test(2, 5)
