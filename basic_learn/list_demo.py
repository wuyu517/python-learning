"""
   学生成绩管理器（简化版）

要求：

1. 创建列表

存储多个成绩：

scores = [78, 95, 84, 62]
2. 输出：
最高分
最低分
平均分
提示

你会用到：

max()
min()
sum()
len()
平均分公式
average = sum(scores) / len(scores)
"""
scores = []  # 初始化一个空列表，用来存放动态输入的成绩

print("--- 学生成绩管理器 ---")
print("提示：请输入学生成绩，输入 'q' 或 'quit' 结束录入。")

# 1. 动态录入阶段（加入异常处理，防止输入不合法崩溃）
while True:
    user_input = input("请输入成绩 (0-100): ").strip()

    if user_input.lower() in ['q', 'quit']:
        break  # 用户输入 q，退出录入

    try:
        score = float(user_input)  # 如果输入的是字母，这里会抛出 ValueError

        # 限制分数在合理的范围内
        if 0 <= score <= 100:
            scores.append(score)  # 只有合法的分数才会加进列表
        else:
            print("❌ 成绩不合法！分数必须在 0 到 100 之间。")

    except ValueError:
        print("❌ 输入错误！成绩必须是数字，请重新输入。")

# 2. 数据分析阶段（加入安全判断，防止列表为空时计算崩溃）
if len(scores) == 0:
    print("\n⚠️ 提示：未录入任何成绩，无法进行统计。")
else:
    print("\n================ 统计结果 ================")
    # 你的核心计算逻辑：
    print(f"最高分: {max(scores)}")
    print(f"最低分: {min(scores)}")

    average = sum(scores) / len(scores)
    print(f"平均分: {average:.2f}")

    print("----------------------------------------")
    # 升级挑战：你写的超棒的 enumerate 循环输出
    for index, score in enumerate(scores, start=1):
        print(f'第 {index} 位同学的成绩: {score}')