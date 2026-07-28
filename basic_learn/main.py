import math_tools

result = math_tools.add(3, 5)

print(result)
'''
你还可以：

from math_tools import add

print(add(3, 5))

区别
import math_tools

调用时：

math_tools.add()


from ... import ...

调用时：

add()

更简洁。

模块搜索路径（重要理解）

Python import 时：

会去找：

当前项目目录

里的 .py 文件。

所以：

同目录下文件
可以直接 import
'''
import calculator
result = calculator.add(3, 5)
print(result)

from calculator import sub
print(sub(3,5))

import calculator
result= calculator.mul(3, 5)
print(result)

import greeting

greeting.hello("Ricardo")

from greeting import hello
print(hello("Ricardo"))