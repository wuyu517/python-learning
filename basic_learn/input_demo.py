name = input("请输入姓名：")

# 1. 处理体重的异常输入
while True:
    try:
        weight = int(input("请输入体重 (kg)："))
        if weight <= 0:
            print("❌ 体重必须大于 0，请重新输入！")
            continue  # 结束本次循环，重新要求输入
        break  # 输入正确，跳出循环
    except ValueError:
        print("❌ 输入不合法！体重必须是整数（例如：65），请重新输入。")

# 2. 处理身高的异常输入
while True:
    try:
        height = float(input("请输入身高 (m)："))
        if height <= 0:
            print("❌ 身高必须大于 0，请重新输入！")
            continue
        break  # 输入正确，跳出循环
    except ValueError:
        print("❌ 输入不合法！身高必须是数字（例如：1.75），请重新输入。")

# 3. 核心计算与输出（此时数据绝对安全，不会崩溃）
bmi = weight / (height ** 2)

print(f"\n{name} 的 BMI 指数为：{bmi:.2f}")