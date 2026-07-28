import numpy as np
np.random.seed(0)#确保每次执行生成同样的随机数组

x1=np.random.randint(10,size=6)#一维数组
x2=np.random.randint(10,size=(3,4))#二维
x3=np.random.randint(10,size=(3,4,5))#三维
print(x1)
print()
print(x2)
print()
print(x3)
print()
print("x3 ndim:",x3.ndim)#数组维度
print("x3 shape:",x3.shape)#数组大小
print("x3 size:",x3.size)#数组总大小
print("dtype:",x3.dtype)#数据类型
print("itemsize:",x3.itemsize,"bytes")#每个数组元素字节大小
print("nbytes:",x3.nbytes,"bytes")#数组总字节大小
'''一般来说，可以认为nbytes 跟itemsize 和size 的乘积大小相等'''

#在多维数组中，可以用逗号分隔的索引元组获取元素
print(x2)
print(x2[2,0])
#也可用以修改元素值
x2[0,0]=12
print(x2)

'''注意，和Python 列表不同，NumPy 数组是固定类型的。这意味着当你试图将一个浮点
值插入一个整型数组时，浮点值会被截短成整型。并且这种截短是自动完成的，不会给你
提示或警告，所以需要特别注意这一点！'''
x1[0]=3.14159#将被截短
print(x1)
print()

#切片符号获取子数组
#x[start:stop:step]默认值分别是0，0，1
x=np.arange(10)
print(x)
print(x[:5])#前五个元素
print(x[5:])#索引五之后的元素
print(x[4:7])#中间的子数组
print(x[::2])#每隔一个元素
print(x[1::2])#从索引一开始每隔一个元素
print()
print(x[::-1])#所有元素逆序
print(x[5::-2])#从索引五开始每隔一个元素逆序
print()
#多维子数组
print(x2)
print(x2[:2,:3])#两行三列
print(x2[:3,::2])#所有行，每隔一列
print(x2[::-1,::-1])#全部逆序
print()


#获取数组的行和列
print(x2[:,0])#x2的第一列
print(x2[0,:])#x2的第一行
#在获取行时，出于语法的简介考虑，可以省略空的切片：
print(x2[0])#等于x2[0, :]
print()

'''非副本视图的子数组
关于数组切片有一点很重要也非常有用，那就是数组切片返回的是数组数据的视图，而
不是数值数据的副本。这一点也是NumPy 数组切片和Python 列表切片的不同之处：在
Python 列表中，切片是值的副本。'''
print(x2)
#从中抽取一个2×2 的子数组：
x2_sub = x2[:2, :2]
print(x2_sub)
'''现在如果修改这个子数组，将会看到原始数组也被修改了！结果如下所示：'''
x2_sub[0, 0] = 99
print(x2_sub)
print(x2)
#这种默认的处理方式实际上非常有用：它意味着在处理非常大的数据集时，可以获取或处理这些数据集的片段，而不用复制底层的数据缓存。

#创建数组的副本
x2_sub_copy = x2[:2, :2].copy()
print(x2_sub_copy)#如果修改这个子数组，原始的数组不会被改变：
x2_sub_copy[0, 0] = 42
print(x2_sub_copy)
print(x2)