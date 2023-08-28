"""
通过windows文本编辑器软件，将下列内容复制保存到：09_01-02.txt，文件可以存储再任意位置
itheima itcast python
itheima python itcast
beijing shanghai itheima
shenzhen hangzhou itheima
zhengzhou bigdata itheima
通过文件读取操作，统计itheima单词出现的次数
"""

f = open("D:/以前の資料/Python/pythonScript/09_文件的操作/09_01-02.txt", "r", encoding="UTF-8")
# 方式一：
# content = f.read()
# count = content.count("itheima")
# print(f'"itheima"在文件中出现的次数是: {count}次')

# 方式二：
count = 0
for line in f:
    line = line.strip()        # 去除开头和结尾的空格以及换行符
    words_list = line.split(" ")    # 使用split(" ")得到一个字符串的列表对象
    # print(f"得到的words_list的类型是: {type(words_list)}, 内容是: {words_list}")
    for word in words_list:
        if word == "itheima":
            count += 1
print(f"itheima在文件中出现的次数是：{count}")

# 记得最后关闭文件
f.close()

