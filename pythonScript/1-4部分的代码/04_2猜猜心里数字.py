# 获取范围在1-100的随机数字
import random

num = random.randint(1, 100)

flag = True
count = 0
while flag:
    guest_num = int(input("请输入您猜测的数字："))
    count += 1
    if guest_num == num:
        print(f"猜中了，您一共猜了{count}次")
        flag = False
    elif guest_num > num:
        print("您猜的大了")
    else:
        print("您猜的小了")

#     else:
#         if guest_num > num:
#             print("您猜的大了")
#         else:
#             print("您猜的小了")
#
print(f"您一共猜了{count}次")
