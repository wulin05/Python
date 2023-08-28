print("欢迎来到黑马动物园")

if int(input("请输入你的身高：(cm)")) > 120:
    print("你的身高大于120cm，不可以免费游玩。")
    print("不过如果你的vip等级大于2，可以免费游玩。")

    if int(input("请输入你的vip级别(1~5):")) < 3:
        print("你的vip等级小于3，不可以免费游玩。")
        print("不过如果今天是1号，可以免费游玩。")

        if int(input("请输入今天的日期：")) == 1:
            print("今天是1号，可以免费游玩")
        else:
            print("Sorry,所有条件都不满足，你需要补票10元。")

    else:
        print("你的vip等级大于3，可以免费游玩。")

else:
    print("欢迎你小朋友，可以免费游玩。")
