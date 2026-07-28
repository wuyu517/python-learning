name=input("请输入名字：")
height=float(input("请输入身高："))
weight=int(input("请输入体重："))
bmi=weight/(height**2)
print(f"你的BMI是{bmi:.2f}")
if bmi<18.5:
    print("身体状态：偏瘦")
elif bmi<24:
    print("身体状态：正常")
else:
    print("身体状态：偏胖")