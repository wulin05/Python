# 案例1
# age = int(input("请输入您的年龄："))
#
# if age >= 18:
#     print("您已成年，需要买票10元。")
# else:
#     print("您未成年，可以免费游玩。")

# 案例2
# print("欢迎来到黑马动物园")
#
# height = int(input("请输入你的身高：(cm)"))
# vip_level = int(input("请输入你的vip级别(1~5):"))
#
# if height <= 120:
#     print("你的身高小于120cm，可以免费游玩。")
# elif vip_level >= 3:
#     print("你的vip登记大于3，可以免费游玩。")
# else:
#     print("不好意思，所有条件都不满足，需要购票10元。")
#
# print("祝你游玩愉快！")

# 案例3
print("欢迎来到黑马动物园")

if int(input("请输入你的身高：(cm)")) <= 120:
    print("你的身高小于120cm，可以免费游玩。")
elif int(input("请输入你的vip级别(1~5):")) >= 3:
    print("你的vip等级大于2，可以免费游玩。")
elif int(input("请输入今天的日期：")) == 1:
    print("今天是1号免费日，可以免费游玩。")
else:
    print("不好意思，所有条件都不满足，需要购票10元。")

print("祝你游玩愉快！")
