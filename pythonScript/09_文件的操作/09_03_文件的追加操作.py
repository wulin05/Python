"""
案例演示：
打开文件，通过追加"a"模式：f = open("python.txt", "a", encoding="UTF-8")
文件写入：f.write("hello,world")
内容刷新：f.flush()

注意：a模式，文件不存在会创建文件
     a模式，文件存在会在最后，追加写入文件
    （这里可以明显看出与 w模式的不同了,w模式可以认为是覆盖文件内容）
"""

f = open("09_03.txt", "a", encoding="UTF-8")
f.write("这是写入使用a模式后，在当前目录下新建09_03.txt文件后写入的内容")
f.close()

f = open("09_03.txt", "a", encoding="UTF-8")
f.write("\n这是存在09_03.txt文件后，追加的内容：Hello,world@")
f.close()
