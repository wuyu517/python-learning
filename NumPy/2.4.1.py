import numpy as np
#数组值的求和
#设想计算一个数组中所有元素的和。Python 本身可用内置的sum 函数来实现：
L=np.random.random(100)
print(sum(L))
#它的语法和NumPy 的sum 函数非常相似，并且在这个简单的例子中的结果也是一样的：
#NumPy 的sum 函数在编译码中执行操作，所以NumPy 的操作计算得更快一些
print(np.sum(L))

big_array=np.random.rand(1000000)
#Python中的min和max函数
print(min(big_array),max(big_array))
#NumPy中也有类似的语法，且也执行得更快
print(np.min(big_array),np.max(big_array))
#对于min、max、sum 和其他NumPy 聚合，一种更简洁的语法形式是数组对象直接调用这些方法：
print(big_array.min(),big_array.max(),big_array.sum())


M=np.random.random((3,4))
print(M)
#默认情况下，每一个NumPy 聚合函数将会返回对整个数组的聚合结果：
print(M.sum())
'''聚合函数还有一个参数，用于指定沿着哪个轴的方向进行聚合。例如，可以通过指定
axis=0 找到每一列的最小值：'''
print(M.min(axis=0))
#每一行的最大值
print(M.max(axis=0))
"""
axis 关键字指定的是数组将会被折叠的维度，而不是将要返回的维度。因此指定axis=0
意味着第一个轴将要被折叠——对于二维数组，这意味着每一列的值都将被聚合。
"""

"""
其他聚合函数
"""
y=np.array([1,2,3,4,5])
#计算元素和
print(np.sum(y))
#计算元素积
print(np.prod(y))
#计算元素平均值
print(np.mean(y))
#计算元素标准差
print(np.std(y))
#计算元素方差
print(np.var(y))
#最小值索引
print(np.argmin(y))
#最大值索引
print(np.argmax(y))
#计算元素中位数
print(np.median(y))
#计算基于元素排序的统计值
#np.percentile() 是 NumPy 中用来计算百分位数（Percentile）的函数
#np.percentile(a, q, axis=None)
#a：输入的数据（数组/矩阵）
#q：要计算的百分位（数值范围在 0 到 100 之间，比如 50 代表 50%）
#axis：（可选）计算的维度/轴
print(np.percentile(y,50))
#验证任一元素是否为真
print(np.any(y))
#验证所有元素是否为真
print(np.all(y))