# 활성화 함수 
# 입력 신호의 총합을 출력 신호로 변환하는 함수를 일반적으로 활성화 함수 
# 활성화 함수를 임계값을 경계로 출력이 바뀌는데, 이런 함수를 계단 함수

# 계단함수 구현하기 
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype = np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show() 