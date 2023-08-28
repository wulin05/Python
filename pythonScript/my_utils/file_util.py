"""
文件处理相关的工具模块
"""


def print_file_info(file_name):
    """
    功能是：将给定路径的文件内容输出到控制台中
    :param file_name: 即将读取的文件路径
    :return: None
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print("文件的全部内容如下：")
        print(content)
    except Exception as e:
        print(f"程序出现异常，原因是{e}")
    finally:
        if f:  # 如果文件不存在的话,那么f就是None值: if None 就不会执行下面的f.close()语句; 如果文件存在,则f值不为None,执行f.close()
            f.close()


def append_to_file(file_name, data):
    """
    功能是：接收传入数据data，追加到指定的文件中file_name
    :param file_name: 指定的文件路径
    :param data: 指定的追加数据
    :return: None
    """
    f = None
    try:
        f = open(file_name, "a", encoding="UTF-8")
        f.write("\n")
        f.write(data)
    except FileNotFoundError:   # 注意,之前是写成FileExistsError,所以死活不能捕获到异常!应该是 FileNotFoundError!!!
        print("文件路径不存在,请检查路径是否正确。")
    finally:
        if f:
            f.close()
    # f = open(file_name, "a", encoding="UTF-8")
    # f.write(data)
    # f.write("\n")
    # f.close()


if __name__ == '__main__':
    print_file_info("D:/以前の資料/Python/pythonScript/09_文件的操作/09_04_bill.txt")
    append_to_file("D/以前の資料/Python/pythonScript/10_程序异常-模块-包/append.txt", "第一次追加内容：传智教育")
    # 故意将append_to_file函数内的文件路径写错.....
