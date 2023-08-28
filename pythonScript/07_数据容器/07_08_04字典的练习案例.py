# 需求：如下员工信息，请使用字典完成数据的记录，并按格式输出

staff_dict = {
    "王力宏": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周杰伦": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "林俊杰": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "张学友": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德华": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}

for all_message in staff_dict:
    print(f'"{all_message}":', end='')
    print(f"{staff_dict[all_message]}")

# 通过for循环，对所有级别为1的员工，级别上升1级，薪水增加1000元
for all_member in staff_dict:
    if staff_dict[all_member]["级别"] == 1:
        staff_dict[all_member]["工资"] += 1000
        staff_dict[all_member]["级别"] += 1

print("=========================================================")

# 输出更新后的员工信息
for all_message in staff_dict:
    print(f'"{all_message}":', end='')
    print(f"{staff_dict[all_message]}")
