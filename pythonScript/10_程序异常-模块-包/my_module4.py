__all__ = ['test_a']
# __all__ = ['test_a', 'test_b'] 用这个的话，就代表test_a、test_b两个函数都可用
# 即，都能在python代码中可被 * 所调用
# 或者 __all__ = ['test_a'] 这个不用,就代表该模块下的所有功能(函数)都能被其他包调用去使用


def test_a(x, y):
    print(x + y)


def test_b(x, y):
    print(x - y)
