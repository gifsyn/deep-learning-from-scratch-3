import numpy as np


# 1.2 Variable クラスの実装
class Variable:
    def __init__(self, data):
        self.data = data


data = np.array(1.0)
x = Variable(data)
print(x.data)

x.data = np.array(2.0)
print(x.data)


# 【補足】NumPyの配列の多次元配列
x = np.array(1)
print(x.ndim)

x = np.array([1, 2, 3])
print(x.ndim)

x = np.array([[1, 2, 3],
              [4, 5, 6]])
print(x.ndim)