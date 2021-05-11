import numpy as np


# 6.1 Variable クラスの追加実装
class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None # 微分した値を持つように拡張


# 6.2 Function クラスの追加実装
class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        self.input = input # 入力された変数を覚える
        return output

    def forward(self, x):
        raise NotImplementedError()

    def backward(self, gy): # 微分の計算を行う逆伝播の機能
        raise NotImplementedError()


# 6.3 Square と Exp クラスの追加実装
class Square(Function):
    def forward(self, x):
        y = x ** 2
        return y

    def backward(self, gy):
        x = self.input.data
        gx = 2 * x * gy
        return gx


class Exp(Function):
    def forward(self, x):
        y = np.exp(x)
        return y

    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy
        return gx


# 6.4 バックプロパゲーションの実装
# (手作業・コーディングによる実装)
# 順伝播
A = Square()
B = Exp()
C = Square()

x = Variable(np.array(0.5))
a = A(x)
b = B(a)
y = C(b)

# 逆伝播
y.grad = np.array(1.0)
b.grad = C.backward(y.grad)
a.grad = B.backward(b.grad)
x.grad = A.backward(a.grad)
print(x.grad) # 3.297442541400256 数値微分の結果とほとんど同じ
