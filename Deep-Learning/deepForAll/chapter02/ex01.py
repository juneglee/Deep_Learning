# 선형회귀 (linear regression) : 최소 제곱법

# x값이 변함에 따라 y값도 변한다 
# x 를 독립 변수, 이 독립 변수에 따라 종속적으로 변하는 y를 종속변수 

# x 값만으로도 y 값을 설명할 수 있을 때 단순 선형 회귀 (simple linear regresssion)
# x 값이 여러개가 필요할 때는 다중 선형 회귀 (multiple linear regression)

# 일차 함수 그래프의 식
# Hypothesis : H(x) = Wx + b
# y = ax + b

# 최소 제곱법 
# a = (x - x평균)*(y - y평균)의 합 / (x-x 평균)^2 의 합

# coding: utf-8

import numpy as np

# x 값과 y값
x=[2, 4, 6, 8]
y=[81, 93, 91, 97]

# x와 y의 평균값 
# mean () : 모든 원소의 평균을 구하는 넘파이 함수 
mx = np.mean(x)
my = np.mean(y)
print("x의 평균값:", mx)
print("y의 평균값:", my)

# 기울기 공식의 분모
divisor = sum([(mx - i)**2 for i in x])
# sum()은 시그마에 해당하는 함수 이다 
# **2 는 제곱을 구하라는 의미 
# for i in x는 x의 각 원소를 한번씩 i 자리에 대입하라는 의미 

# 기울기 공식의 분자 : (x - x평균)*(y - y평균)의 합
def top(x, mx, y, my):
    d = 0
    for i in range(len(x)):
        d += (x[i] - mx) * (y[i] - my)
    return d
dividend = top(x, mx, y, my)

print("분모:", divisor)
print("분자:", dividend)

# 기울기와 y 절편 구하기
a = dividend / divisor
b = my - (mx*a)

# 출력으로 확인
print("기울기 a =", a)
print("y 절편 b =", b)
 
