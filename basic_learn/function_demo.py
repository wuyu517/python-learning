# 1. 你的核心计算函数（保持不变）
def bmi(weight, height):
    return weight / height ** 2

print("--- BMI 计算器（函数异常处理版）---")

# 2. 获取体重（带异常处理）
while True:
    try:
        user_weight = float(input("请输入体重 (kg): "))
        if user_weight <= 0:
            print("❌ 体重必须大于 0！")
            continue
        break
    except ValueError:
        print("❌ 输入错误！体重必须是数字。")

# 3. 获取身高（带异常处理）
while True:
    try:
        user_height = float(input("请输入身高 (m): "))
        if user_height <= 0:
            print("❌ 身高必须大于 0！")
            continue
        break
    except ValueError:
        print("❌ 输入错误！身高必须是数字。")

# 4. 调用你的函数并传入安全的变量
result = bmi(user_weight, user_height)

# 5. 打印结果
print(f'\n您的 BMI 指数为: {result:.2f}')