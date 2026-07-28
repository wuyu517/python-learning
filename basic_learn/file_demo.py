file = open("test.txt", "r", encoding="utf-8")

content = file.read()

print(content)

file.close()
"""
更推荐的写法（重点）

Python 更常用：

with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
    
    
    为什么 with 更好？

因为：

自动关闭文件

即使报错也安全。

以后几乎都用：

with open()
"""
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python")

with open("output.txt", "a", encoding="utf-8") as file:
    file.write("\n新的内容")