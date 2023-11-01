import numpy as np
from step01 import Variable
from step02 import Square

# 테스트
data = np.array(10)
x = Variable(data)
f = Square()
y = f(x)

print(type(y))
print(y.data)