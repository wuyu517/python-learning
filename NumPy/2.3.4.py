import numpy as np
"""指定一个用于存放运算结果的数组不同于创建
临时数组，你可以用这个特性将计算结果直接写入到你期望的存储位置。所有的通用函数
都可以通过out 参数来指定计算结果的存放位置："""
x=np.arange(5)
y=np.empty(5)
np.multiply(x,10,out=y)
print(y)
#这个特性也可以被用作数组视图，例如可以将计算结果写入指定数组的每隔一个元素的位置：
z=np.zeros(10)
np.power(2,x,out=z[::2])
print(z)

"""reduce 的作用就是：
把一个二元运算符（需要两个输入参数的函数，比如加法、乘法），
重复施加到数组的元素上，最终将数组“折叠”成单个值。"""
#对add 通用函数调用reduce 方法会返回数组中所有元素的和：
x0=np.arange(1,6)
print(np.add.reduce(x0))
"""在 NumPy 中，这个功能的优势：
任何“二元通用函数”都能直接用 .reduce()
只要一个函数能接收两个参数并返回一个结果，它就能用来规约数组。"""
#对multiply通用函数调用reduce方法返回数组中所有元素的乘机
print(np.multiply.reduce(x0))
#如果需要存储每次计算的中间结果，可以使用accumulate：
print(np.add.accumulate(x0))
print(np.multiply.accumulate(x0))

#最后，任何通用函数都可以用outer 方法获得两个不同输入数组所有元素对的函数运算结果。这意味着你可以用一行代码实现一个乘法表：
x1=np.arange(1,6)
print(np.multiply.outer(x1,x1))
"""
.outer(A, B) 的作用是：
把数组A中的每一个元素，
分别与数组B中的每一个元素做对应的运算（这里是乘法），
最后拼成一个二维矩阵（表格）。
不同长度的两个数组也能直接吐出组合后的矩阵。
"""
#加法加法表
print(np.add.outer(x,x1))
#幂次方表
print(np.power.outer(x,x1))