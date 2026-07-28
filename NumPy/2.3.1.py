"""Python 的相对缓慢通常出现在很多小操作需要不断重复的时候，比如对数组的每个元素做
循环操作时。假设有一个数组，我们想计算每个元素的倒数，一种直接的解决方法是："""
import numpy as np
np.random.seed(0)
def compute_reciprocals(values):
    output=np.empty(len(values))
    for i in range(len(values)):
        output[i]=1.0/values[i]
    return output
values=np.random.randint(1,10,size=5)
print(compute_reciprocals(values))
"""如果测试一个很大量的输入数据运行上述代码的时间，这一操作将非常耗时，
并且是超出意料的慢！我们将用IPython 的%timeit 魔法函数（详情请参见1.9 节）来测量："""

"""NumPy 中的向量操作是通过通用函数实现的。通用函数的主要目的是对NumPy 数组中的
值执行更快的重复操作。它非常灵活，前面我们看过了标量和数组的运算，但是也可以对
两个数组进行运算："""
print(np.arange(5)/np.arange(1,6))
#通用函数也可以进行多维数组的运算
x=np.arange(9).reshape(3,3)
print(2**x)