name1 = "Lin wu"
name2 = '林武'
name3 = """I like python!"""


def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串: {data},长度是{count}")


my_len(name1)
my_len(name2)
my_len(name3)
