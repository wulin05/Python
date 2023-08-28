# 使用while循环遍历元组元素
tuplelist = ("福建", "广东", "浙江", "福州", "福州", "福州", "广州", "杭州")
index = 0
while index < len(tuplelist):
    print(f"while遍历元组tuplelist的元素:{tuplelist[index]}")
    index += 1

# 输出元组tuplelist的元素
print(tuplelist)

# 使用for循环遍历元组元素
for element in tuplelist:
    print(f"for遍历元组tuplelist的元素:{element}")


