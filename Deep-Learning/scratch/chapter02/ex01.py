# 시그모이드 함수 구현하기 

import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1/(1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show() 

# 시그모이드 = s자 모양 함수 
# 계단형 함수와 시그모이드 함수는 둘다 비선형 함수이다.
