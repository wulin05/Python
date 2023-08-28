# 先打开文件： f = open("文件名", "w", encoding="UTF-8")
# 进行文件的写入： f.write("内容")
# 内容刷新： f.flush()
# 注意：直接调用 write，内容并未真正写入文件，而是存在程序的内存中，称之为缓冲区
# 当真正调用flush的时候，内容才真正写入文件
# 这样做是避免频繁操作磁盘，导致效率下降（攒一堆，一次性写入磁盘）
# import time  # 如果使用time.sleep()函数,那就要import time函数

# 打开文件，不存在的文件，r,w,a
f = open("D:/以前の資料/Python/pythonScript/09_文件的操作/09_02-01文件的写入.txt", "w", encoding="UTF-8")
f.write("Hello world!!!!!")  # 使用write方法会在当前目录下创建一个09-02.txt的文件，此时文件内容是空的
# with open("D:/以前の資料/Python/pythonScript/09_文件的操作/09_02-01文件的写入.txt", "w", encoding="UTF-8") as f:
#     for line in f:
#         print(f"2-每一行数据是：{line}")

# flush刷新
# f.flush()        # 将内存中积攒的内容，写入到硬盘的文件中
# time.sleep(1000) # 使用sleep，让程序暂停运行，但不退出

# close关闭
f.close()  # close方法，内置了flush的功能的，所以可以把f.flush功能注释掉，直接用f.close()即可

# 打开一个存在的文件
f2 = open("D:/以前の資料/Python/pythonScript/09_文件的操作/09_02-01文件的写入.txt", "w", encoding="UTF-8")

# write写入、flush刷新
f2.write("黑马程序员")  # 当文件存在，write方法会将文件清空，然后写入内容

# close关闭
f2.close()
