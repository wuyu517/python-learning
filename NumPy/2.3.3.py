import numpy as np
"""通用函数有两种存在形式：一元通用函数（unary ufunc）对单个输入操作，二元通用函数
（binary ufunc）对两个输入操作。"""
x=np.arange(4)
print("x=",x)
print("x+5=",x+5)
print("x-5=",x-5)
print("x*2=",x*2)
print("x/2=",x/2)
print("x//2=",x//2)#地板除法运算
#还有逻辑非、** 表示的指数运算符和% 表示的模运算符的一元通用函数：
print("-x=",-x)
print("x**2=",x**2)
print("x%2=",x%2)
#可任意组合使用，注意优先级
print(-(0.5*x+1)**2)
"""所有这些算术运算符都是NumPy 内置函数的简单封装器，例如+ 运算符就是一个add 函
数的封装器"""

#绝对值
x0=np.array([-2,-1,0,1,2])
print(abs(x0))
#对应的NumPy 通用函数是np.absolute，该函数也可以用别名np.abs 来访问：
print(np.absolute(x0))
print(np.abs(x0))
#这个通用函数也可以处理复数。当处理复数时，绝对值返回的是该复数的幅度：
x1=np.array([3-4j,4-3j,2+0j,0+1j])#Python 中虚数单位用 j 或 J 表示（比如 4j），而不是数学里常见的 i
print(np.abs(x1))#因为输入的数组包含虚数，x1 的数据类型是复数类型（complex128）。计算绝对值后，结果会全变为正实数（float64）。

"""三角函数"""
#定义一个角度数组
theta=np.linspace(0,np.pi,3)
print("theta=",theta)
print("sin(theta)=",np.sin(theta))
print("cos(theta)=",np.cos(theta))
print("tan(theta)=",np.tan(theta))
#逆三角函数同样可以使用
x2=[1,0,-1]
print("x2=",x2)
print("arcsin(x2)=",np.arcsin(x2))
print("arccos(x2)=",np.arccos(x2))
print("arctan(x2)=",np.arctan(x2))

"""指数运算"""
x3=np.array([1,2,3])
#这里有一个容易踩坑的地方：
#在 NumPy 的 np.power(x1, x2) 中，
#第一个参数 x1 是底数，第二个参数 x2 是指数。
#如果写作 np.power(3, x)，计算的是 $3^1, 3^2, 3^3$。
#但是，如果传入纯 Python 列表 [1, 2, 3] 作为第二个参数，
#在某些 NumPy 版本中可能无法正常广播，或者结果不符合预期。
#最标准的写法是先把 $x$ 定义为 NumPy 数组：
print("x3=",x3)
print("e^x3=",np.exp(x3))
print("2^x3=",np.exp2(x3))
print("3^x3=",np.power(3,x3))
#对数函数
x4=[1,2,4,10]
print("x4=",x)
print("ln(x4)=",np.log(x4))
print("log2(x4)=",np.log2(x4))
print("log10(x4)=",np.log10(x4))
#一些特殊的版本，对于非常小的输入值可以保持较好的精度：
x5=[0,0.001,0.01,0.1]
print("exp(x5)-1=",np.expm1(x5))
print("log(1+x5)=",np.log1p(x5))
#当x 的值很小时，以上函数给出的值比np.log 和np.exp 的计算更精确

"""有一个更加专用，也更加晦涩的通用函数优异来源是子模块scipy.special。如果你希
望对你的数据进行一些更晦涩的数学计算，scipy.special 可能包含了你需要的计算函数。
这些函数能列一个长长的列表，下面的代码片段展示了一些可能在统计学中用到的函数："""
from scipy import special
#Gamma函数（广义阶乘，generalized factorials)和相关函数
y=[1,5,10]
print("gamma(y)=",special.gamma(y))
print("ln|gamma(y)=",special.gammaln(y))
print("beta(y,2)=",special.beta(y,2))
#误差函数（高斯积分）
#它的实现和它的逆实现
z=np.array([0,0.3,0.7,1.0])
print("erf(z)=",special.erf(z))
print("erfc(z)=",special.erfc(z))
print("erfinv(z)=",special.erfinv(z))