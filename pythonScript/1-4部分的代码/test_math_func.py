from math_func import add


def test_add():
    assert add(2, 3) == 5
    assert add('hello', 'world') == 'hello world'
