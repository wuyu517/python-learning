"""
猜数字小游戏

规则：

程序设定数字 7
用户不断输入
猜对结束
猜大提示“大了”
猜小提示“小了”
"""
num=7
player=int(input("请输入结果："))
while player!=7:
    if player >7:
        print("大了")
    elif player<7:
        print("小了")
    player = int(input("没猜对，请重新输入结果："))
print("猜对了")