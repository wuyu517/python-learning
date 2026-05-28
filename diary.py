"""
参考Gmini
# 1. 让用户输入一句话，并存进变量 line 中
line = input("请输入今天的日记：")

# 2. 使用 "a" 模式（追加模式）打开或创建 diary.txt
# 注意：我们要手动在末尾加上换行符 "\n"，这样下次运行输入时才会另起一行
with open("diary.txt", "a", encoding="utf-8") as file:
    file.write(line + "\n")

print("日记已成功追加保存！")
"""
line = input("请输入今天的日记：")
with open("diary.txt", "a", encoding="utf-8") as file:
    file.write(line + "\n")