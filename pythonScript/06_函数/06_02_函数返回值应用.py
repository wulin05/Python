def check_age(age):
    if age > 18:
        # return "Success"
        return "Ture"
    # 这里的 return None不需要else的原因是：当if语句生效后,写在return “Ture"后面的代码就不执行了。
    return None


result = check_age(20)
print(f"输出result的类型:{result}")

if not result:
    print("未成年，不可进入")
else:
    print("成年人，可以进入")

# None某种意义上就是False

# None可以用于声明无初始内容的变量
name = None
print("name的值是: %s, name的类型是: %s" % (name, type(name)))
print(f"name的值是: {name}, name的类型是: {type(name)}")
