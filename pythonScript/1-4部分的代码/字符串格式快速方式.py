# 关于字符串格式化快速方式
name = "传智播客"
setup_year = 2006
stock_price = 19.99
message03 = "%s,成立于:%s,股票价格是:%s" % (name, setup_year, stock_price)
print(message03)
print("%s,成立于:%d,股票价格是:%f" % (name, setup_year, stock_price))

num = 11.345
print("num的数字宽度为4,精度为2:%4.2f" % num)

# f表示format
print(f"我是{name},成立于{setup_year},今天的股票价格是：{stock_price}")

# 以上的所有内容都是基于变量的格式化
# 以下介绍表达式的格式化
# 表达式：一条具有明确执行结果的代码语句：1+1, 5*2, name = "张三", age = 11+11
print("1 * 1的结果是：%d" % (1 * 1))
print(f"1 * 2的结果是：{1 * 2}")
print("字符串在Python中的类型是：%s" % type('字符串'))

# 练习题
name01 = "传智播客"
stock_price01 = 19.99
stock_code01 = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7

finally_stock_price = stock_price01 * stock_price_daily_growth_factor ** growth_days

print(f"公司：{name01},股票代码：{stock_code01},当前股价{stock_price01}")
print("每日增长系数是： %.1f,经过%d天的增长后,股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_days, finally_stock_price))
