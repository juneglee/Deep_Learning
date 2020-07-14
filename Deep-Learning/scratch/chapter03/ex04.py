#  편미분 
import numpy as np

def numerical_diff(f,x):
    h = 1e-4 # 0.0001
    return (f(x+h)- f(x-h)) / (2*h)

def function_2(x):
    return x[0]**2 + x[1]**2
    # 또는 np.sum(x**2)

# x0 = 3, x1= 4 일때 x0에 대한 편미분
def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

print(numerical_diff(function_tmp1, 3.0)) # 6.00000000000378

# x0 = 3, x1= 4 일때 x1에 대한 편미분
def function_tmp2(x1):
    return 3.0**2.0 + x1*x1

print(numerical_diff(function_tmp2, 4.0)) # 7.999999999999119

# 편미분은 변수가 하나인 미분과 마찬가지로 특정 장소의 기울기를 구한다.
# 단, 여러 변수 중 목표 변수 하나에 초점을 맞추ㅗㄱ 다른 변수의 값을 고정한다.

