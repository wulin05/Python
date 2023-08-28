money = 10000
for i in range(1, 21):
    import random
    score = random.randint(1, 10)

    if score < 5:
        print(f"员工{i}绩效分{score},不发工资，下一位。")
        continue

    # if money >= 1000:
    #     money -= 1000
    #     print(f"员工{i},满足条件发放工资1000元,公司账户余额{money}。")
    # else:
    #     print("账户余额不足,结束发工资。")
    #     break

    if money >= 1000:
        print(f"公司账户余额:{money},员工{i},绩效分{score},发放工资1000")
        money -= 1000
    else:
        print(f"账户余额不足,当前余额:{money}元,结束发工资")
        break

    # if money >= 1000:
    #     if score < 5:
    #         print(f"员工{i}绩效分{score},不发工资,下一位。")
    #         continue
    #     else:
    #         print(f"员工{i}绩效分{score},满足发放工资1000")
    #         money -= 1000
    # else:
    #     print(f"账户余额不足,当前余额:{money}元,结束发工资")
    #     break
