def fuc_a():
    print("---语句2---")


def fuc_b():
    print("---语句1---")
    fuc_a()
    print("---语句3---")


fuc_b()
fuc_a()
