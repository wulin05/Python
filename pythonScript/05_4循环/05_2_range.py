# for x in range(5,13,2):
#     print(x)

# x = 1
# for x in range(1,101):
#     print(f"今天是向小妹表白的第{x}天，坚持。")
#     for y in range(1,11):
#         print(f"送给小美的第{y}朵玫瑰花")
#     print(f"小美，我喜欢你(第{x}天的表白结束)")
#
# print(f"第{x}天，表白成功")

i = 1
while i <= 100:
    print(f"今天是向小美表白的第{i}天，坚持")
    for j in range(1, 11):
        print(f"送给小美的第{j}朵玫瑰花")
    print(f"小美，我喜欢你(第{i}天的表白结束)")
    i += 1
print(f"第{i-1}天，表白成功")
