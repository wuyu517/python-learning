#数组的变形
import numpy as np
#将数字1~9放入一个3×3的矩阵中
grid=np.arange(1,10).reshape(3,3)
print(grid)
#如果希望该方法可行，那么原始数组的大小必须和变形后数组的大小一致

#将一个一维数组转变为二维的行或列的矩阵
x=np.array([1,2,3])
#通过变形获得的行向量
print(x.reshape((1,3)))
#通过newaxis获得的行向量
print(x[np.newaxis,:])#写在前面（np.newaxis, :）代表新增的是行维度；如果写在后面（:, np.newaxis），就会变成 3 行 1 列 的列向量 (3, 1)
#通过变形获得的列向量
print(x.reshape((3,1)))
#通过newaxis获得的列向量
print(x[:,np.newaxis])

#数组的拼接
x=np.array([1,2,3])
y=np.array([3,2,1])
print(np.concatenate((x,y)))
#np.concatenate也可以一次性拼接两个以上数组
z=np.array([99,99,99])
print(np.concatenate((x,y,z)))
#也可用于二维数组的拼接
grid=np.array([[1,2,3],[4,5,6]])
#沿着第一个轴拼接
print(np.concatenate([grid,grid]))
'''np.concatenate([grid, grid])默认轴：
没有传 axis 参数时，默认是 axis=0。
拼接逻辑：沿着行方向（纵向/上下）把两个 grid 上下拼在一起。
Shape 变化：从 (2, 3) + (2, 3) → (4, 3)（行数相加 2+2=4，列数不变）。'''
#沿着第二个轴拼接（从0开始索引）
print(np.concatenate([grid,grid],axis=1))
'''与上同理'''
#沿着固定维度处理数组时，使用np.vstack（垂直栈）和np.hstack（水平栈）函数会更简洁：
x=np.array([1,2,3])
grid0=np.array([[9,8,7],[6,5,4]])
#垂直栈数组
print(np.vstack([x,grid0]))
#水平栈数组
y0=np.array([[99],[99]])
print(np.hstack([grid0,y0]))
#与之相似，np.dstack将沿着第三个维度拼接数组

'''数组的分裂
与拼接相反的过程是分裂。分裂可以通过np.split、np.hsplit 和np.vsplit 函数来实现。
可以向以上函数传递一个索引列表作为参数，索引列表记录的是分裂点位置：'''
x0=[1,2,3,99,99,3,2,1]
x1,x2,x3=np.split(x0,[3,5])
print(x1,x2,x3)
grid1=np.arange(16).reshape((4,4))
print(grid1)
upper,lower=np.vsplit(grid1,[2])
print(upper,lower)
left,right=np.hsplit(grid1,[2])
print(left,right)
#与之相似，np.dsplit将数组沿着第三个维度分裂