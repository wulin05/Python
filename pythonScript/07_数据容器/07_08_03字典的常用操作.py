"""
新增元素和更新元素：字典[key] = value。 key在字典中不存在，则是新增元素；如果key已存在，则就是更新value值。
操作总结：
1.字典[key]: 获取指定key对应的value值
2.字典[key] = value: 添加或更新键值对
3.字典.pop(key): 取出key对应的value并在字典内删除此key的键值对
4.字典.clear(): 清空字典
5.字典.keys(): 获取字典的全部key,可用于for循环遍历字典
6.len(字典): 计算字典内的元素数量


"""
stu_score_dict = {
    "王力宏": {
        "语文": 99,
        "数学": 88,
        "英语": 77
    }, "周杰伦": {
        "语文": 11,
        "数学": 22,
        "英语": 33
    }, "林俊杰": {
        "语文": 80,
        "数学": 70,
        "英语": 60
    }
}
stu_score_dict["林俊杰"]["英语"] = 98
print(f"输出更新元素后字典：{stu_score_dict}")

stu_score_dict["张学友"] = {"语文": 1, "数学": 2, "英语": 3}
print(f"输出新增元素后字典：{stu_score_dict}")

stu_score_dict["刘德华"] = {"语文": 10}
print(f"输出新增元素后字典：{stu_score_dict}")

# 删除元素： 注意集合是使用.remove方法删除元素,.pop是随机抽取元素(删除元素)。而字典可以通过.pop(key)来移除元素(键值对)。
score = stu_score_dict.pop("张学友")  # 延伸：集合里有 .remove()方式可以移除元素
print(f"删除的value值为：{score}")
print(f"删除张学友后，字典的内容为：{stu_score_dict}")

# 清空元素  因为清空了字典，后续还有其他操作，所以这边注释掉了
# stu_score_dict.clear()
# print(f"清空字典后，字典的值是：{stu_score_dict}")

# 获取全部的key
# 字典提供了方法：
# 语法： 字典.keys()
keys = stu_score_dict.keys()
print(keys)
print(f"获取字典stu_score_dict的全部key：{stu_score_dict.keys()}")


print("----------------------------------------------------------------")
# 遍历字典：方式有两种（但其实核心都是先获取到key值，通过key值输出value值)
# 方式一：通过获取到全部的key来完成遍历
for key1 in keys:
    print(f"字典的key1是：{key1}")
    print(f"字典的{key1}对应的value值是：{stu_score_dict[key1]}")

print("----------------------------------------------------------------")
# 方式二：直接对字典进行for循环，每一次循环都是直接得到key
for key2 in stu_score_dict:
    print(f"字典的key2是：{key2}")
    print(f"字典的value是：{stu_score_dict[key2]}")

print("----------------------------------------------------------------")
# 统计字典内的元素数量
num = len(stu_score_dict)
print(num)

