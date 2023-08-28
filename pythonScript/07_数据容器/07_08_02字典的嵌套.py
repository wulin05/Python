# 字典的key和value可以是任意数据类型(但，key不可以为字典类型)
# 这么理解：如果字典里的key也可以是字典类型，那么就意味着一个key，可以有不同的value，那就不符合字典的特征了
# 示例如下：
stu_score_dict = {
    "王力宏": {
        "语文": 99,
        "数学": 88,
        "英语": 77
    },
    "周杰伦": {
        "语文": 11,
        "数学": 22,
        "英语": 33
    },
    "林俊杰": {
        "语文": 80,
        "数学": 70,
        "英语": 60
    }
}
print(f"学生的考试信息是：{stu_score_dict}")

# 从嵌套字典中获取数据
socre_zhou = stu_score_dict["周杰伦"]["语文"]
print(f"获取周杰伦的语文考试成绩：{socre_zhou}")

socre_lin = stu_score_dict["林俊杰"]["英语"]
print(f"获取林俊杰的英语考试成绩：{socre_lin}")
