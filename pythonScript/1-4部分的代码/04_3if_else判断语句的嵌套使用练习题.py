# age = int(input("请输入你的年龄："))
# if 18 <= age < 30:
#     print("年龄符合，继续判断")
#     if float(input("请输入入职时间：")) <= 2:
#         print("虽然年龄符合，但是入职时间没超过2年，需要判断级别！")
#         if int(input("请输入级别：")) > 3:
#             print("级别大于3，可以领取礼物。")
#         else:
#             print("条件都不满足，不可以领取礼物。")
#     else:
#         print("入职超过2年，可以领取礼物。")
# else:
#     print("未成年，不能领取礼物")

age = int(input("请输入你的年龄："))
if 18 <= age < 30:
    print("年龄达标了，继续判断")
    if float(input("请输入入职时间：")) > 2:
        print("年龄和入职时间满足条件，可以领取礼物。")
    elif int(input("请输入级别：")) > 2:
        print("级别达标，可以领取礼物")
    else:
        print("虽然年龄达标，但是入职时间和级别都不达标，不可以领取礼物")
else:
    print("年龄不达标，不可以领取礼物")
