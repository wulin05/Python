# % 表示：我要占位
# s 表示：将变量变成字符串放入占位的地方
name = "黑马程序员"
message01 = "学IT来 %s" % name
print(message01)

# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message02 = "Python大数据学科，北京%s期，毕业平均工资：%s" % (class_num, avg_salary)
print(message02)

# 关于%s，%d，%f三种不同的格式符号
name = "传智播客"
setup_year = 2006
stock_price = 19.99
message03 = "%s,成立于:%d,股票价格是:%f" % (name, setup_year, stock_price)
print(message03)

# 字符串格式-数字精度控制
# 示例：%5d：表示将整数的宽度控制在5位，如数字11，被设置成5d，就会变成：【空格】【空格】【空格】11，用三个空格补足宽度
# %7.2f：表示将宽度控制为5，将小数点精度设置为2，如11.345，结果是：【空格】【空格】11.35
# %.2f：表示不限制宽度，只设置小数点精度为2，如11.345，结果是：11.35
num1 = 11
num2 = 11.345
print("数字11宽度现在5，结果是：%5d" % num1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11.345宽度不限制，小数精度2，结果是：%.2f" % num2)
