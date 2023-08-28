# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1},类型是：{type(bool_1)}; bool_2变量的内容是：{bool_2},类型是：{type(bool_2)}")

# if
age = 30
print(f"今年我已经{age}岁了")
if age >= 18:
    print("我已经成年了")

print("时间过得真快啊！")

# 案例
age01 = int(input("请输入你的年龄："))
if age01 >= 18:
    print("你已经成年，游玩需要补票10元")
print("祝您游玩愉快")
