#  수치 미분 
# 아주 작은 차븐으로 미분하는 것을 수치미분이라 합니다.
# 수식을 전개해 비문하는 것을 해석적이라는 말을 해석적 해 혹은 해석적으로 미분하는 등으로 표현 
# 즉, 해석적 미분은 우리가 수학 시간에 배운 미분이며, 수치 미분은 이를 근사치로 계산하는 방법 
# 수치해석학은 해석학 문제에서 수치적인 근삿값을 구하는 알고리즘을 연구하는 학문 

# 시간을 뜻하는 h를 한없이 0에 가깝게 하여, x의 작은 변화가 함수f(x) 를 얼마나 변화시키느냐를 의미 

# 나쁜 구현 예 
def numerical_diff(f,x):
    h = 10e-50
    return (f(x+h)- f(x)) /h
    # 이 방식은 반올림 오차를 일으킨다. 반올림 오차는 작은 값(가령 소수점 8자리 이하)이 생략되어 
    # 최종 계산 결과에 오차가 생기게 된다.
    # 1e-50 을 float32형(32비트 부통소수점)으로 나타내면 0.0이 되어, 올바로 표현할 수 없다 
    # 너무 작은 값을 이용하면 컴퓨터로 계산하는데 문제가 된다.

# 이 오차를 줄이기 위해 (x-h)일 때 함수f의 차분을 계산하는 방법을 쓴다
# x를 중심으로 그 전후의 차분을 계한다는 의미에서 중심 차분 혹은 중앙 차분이라한다 

def numerical_diff(f,x):
    h = 1e-4 # 0.0001
    return (f(x+h)- f(x-h)) / (2*h)

# 수치 미분의 예
def function_1(x):
    return 0.01*x**2 + 0.1*x

import numpy as np
import matplotlib.pylab as plt

x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x")
plt.plot(x,y)
plt.show()

# x = 5일 때 미분
print(numerical_diff(function_1, 5)) # 0.1999999999990898
# x = 10 일 때 미분
print(numerical_diff(function_1, 10)) # 0.2999999999986347
