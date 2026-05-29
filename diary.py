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
print("--- 电子日记本 ---")
print("1. 写日记")
print("2. 看日记")

choice = input("请选择操作 (1 或 2): ")

if choice == "1":
    # 你的核心代码：写日记
    line = input("请输入今天的日记: ")
    # "a" 模式很安全：文件不存在会自动创建，存在则追加
    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write(line + "\n")
    print("日记已成功追加保存！")

elif choice == "2":
    # 核心改动：读日记（加入异常处理，防止文件不存在时崩溃）
    try:
        with open("diary.txt", "r", encoding="utf-8") as file:
            print("\n--- 历史日记内容 ---")
            print(file.read())
    except FileNotFoundError:
        # 老师要求的“自动处理”：文件不存在时，不崩溃，而是给出友好提示
        print("\n🔍 提示：目前还没有日记文件（diary.txt 不存在）。")
        print("不用担心，系统已为您自动初始化。去试着写第一篇日记吧！")

else:
    print("❌ 输入错误，请输入 1 或 2！")