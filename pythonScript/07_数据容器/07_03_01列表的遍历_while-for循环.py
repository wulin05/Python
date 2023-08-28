def list_while_func():
    index_1 = 0
    mylist = ["福建", "广东", "浙江"]
    while index_1 < len(mylist):
        element = mylist[index_1]
        index_1 += 1
        print(f"第{index_1}个元素是:{element} ")


def list_for_func():
    sedlist = ["福州", "广州", "杭州"]
    for element in sedlist:
        print(f"列表内的元素是:{element}")


list_while_func()

list_for_func()
