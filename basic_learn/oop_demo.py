# 1. 定义 Dog 类
class Dog:
    # 2. 构造方法：用来初始化小狗的属性（名字和年龄）
    def __init__(self, name, age):
        self.name = name  # 属性：名字
        self.age = age    # 属性：年龄

    # 3. 动态方法：小狗的行为
    def bark(self):
        print("旺旺！")


# --- 测试运行 ---
# 创建一只具体的小狗实例（实例化对象）
my_dog = Dog(name="旺财", age=3)

# 打印属性看看
print(f"小狗的名字是: {my_dog.name}, 年龄是: {my_dog.age}")

# 调用方法，输出图片要求的“旺旺！”
my_dog.bark()