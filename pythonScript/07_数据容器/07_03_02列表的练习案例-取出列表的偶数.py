# mylist = [1,2,3,4,5,6,7,8,9,10]
# newlist = []
# forlist = []


def list_while_func():
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    newlist = []
    index = 0
    while index < len(mylist):
        if mylist[index] % 2 == 0:
            element = mylist[index]
            newlist.append(element)
        index += 1
    print(newlist)


def list_for_func():
    mylist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    forlist = []
    for element in mylist:
        if element % 2 == 0:
            forlist.append(element)
    print(forlist)


list_while_func()
list_for_func()