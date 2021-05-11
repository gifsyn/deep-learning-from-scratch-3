import numpy as np


class Variable:
    def __init__(self, data):
        self.data = data


# 2.2 Function クラスの実装
class Function:
    def __call__(self, input):
        x = input.data # データを取り出す
        y = self.forward(x) # 具体的な計算はforwardメソッドで行う
        output = Variable(y) # Variableとして返す
        return output

    def forward(self, in_data):
        raise NotImplementedError()

# 2.3 Function クラスを使う
# Function クラスを継承して、入力された値を2乗するクラス Square
class Square(Function):
    def forward(self, x):
        return x ** 2


x = Variable(np.array(10))
f = Square()
y = f(x)
print(type(y))
print(y.data)