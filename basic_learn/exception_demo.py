try:
    num = int(input("请输入一个整数："))
    result = 10 / num
except ValueError:
    print("请输入整数")
except ZeroDivisionError:
    print("不能除以0")

