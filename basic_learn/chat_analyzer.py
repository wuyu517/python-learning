with open("chat.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
total=len(lines)
python_count=sum(1 for line in lines if "Python"in line) #单行注释，意思是当条件成立时返回1，最后由sum()将所有的1加起来，这是一种简化写法
ai_count=sum(1 for line in lines if "AI"in line)
print(f"总行数:{total}")
print(f"包含Python的行数:{python_count}")
print(f"包含AI的行数:{ai_count}")

'''
函数封装写法
def count_keyword(lines, keyword):
    return sum(1 for line in lines if keyword in line)
python_count = count_keyword(lines, "Python")
ai_count = count_keyword(lines, "AI")
'''