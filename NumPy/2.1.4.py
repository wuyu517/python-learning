import numpy as np

print(np.array([3.14,4,2,3]))
print()

print(np.array([ 1., 2., 3., 4.], dtype='float32'))
print()

# 嵌套列表构成的多维数组
print(np.array([range(i,i+3)for i in [2,4,6]]))
print()

# 创建一个长度为10的数组，数组的值都是0
print(np.zeros(10,dtype=int))
print()

# 创建一个3×5的浮点型数组，数组的值都是1
print(np.ones((3,5),dtype=float))
print()

# 创建一个3×5的浮点型数组，数组的值都是3.14
print(np.full((3,5),3.14))
print()

# 创建一个数组，其中包含一个线性序列# 从 0 开始，到 20 结束，步长为 2
# （这类似于内置的 range() 函数
print(np.arange(0,20,2))
print()

#创建一个包含五个均匀分布在 0 到 1 之间的值的数组
print(np.linspace(0,1,5))
print()

# 创建一个 3x3的数组，其中包含 0 到 1 之间均匀分布的随机值
print(np.random.random((3,3)))
print()

# 创建一个3×3的、均值为0、方差为1的
# 正态分布的随机数数组
print(np.random.normal(0,1,(3,3)))
print()

# 创建一个3×3的、[0, 10)区间的随机整型数组
print(np.random.randint(0,10,(3,3)))
print()

# 创建一个3×3的单位矩阵
print(np.eye(3))
print()

# 创建一个由3个整型数组成的未初始化的数组
# 数组的值是内存空间中的任意值
print(np.empty(3))