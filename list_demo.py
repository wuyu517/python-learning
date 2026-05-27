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
scores = [78, 95, 84, 62]
print(max(scores))
print(min(scores))
average = sum(scores) / len(scores)
print(average)
"""
升级挑战（推荐）

用：

for

循环输出：

第1位同学成绩：78
第2位同学成绩：95
"""
for index,score in enumerate(scores,start=1):
    print(f'第{index}位同学的成绩：{score}')