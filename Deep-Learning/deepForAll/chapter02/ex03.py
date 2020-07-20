# 선형회귀 (linear regression) : 
#  옵티마이저(Optimizer) : 경사하강법(Gradient Descent)
# - 오차의 변화에 따라 이차 함수 그래프를 만들고 적절한 학습률을 설정해 미분 값이 0인 지점을 구하는 것
# 선형 회귀를 포함한 수많은 머신 러닝, 딥 러닝의 학습은 
# 결국 비용 함수를 최소화하는 매개 변수인 W와 b을 찾기 위한 작업을 수행합니다. 
# 이때 사용되는 알고리즘을 옵티마이저(Optimizer) 또는 최적화 알고리즘이라고 부릅니다.

# 옵티마이저를 통해 적절한 W와 b를 찾아내는 과정을 머신 러닝에서 학습(training)이라고 부른다

#  cost가 최소화가 되는 지점은 접선의 기울기가 0이 되는 지점이며, 또한 미분값이 0이 되는 지점입니다. 
#  경사 하강법의 아이디어는 비용 함수(Cost function)를 미분하여 현재 W에서의 접선의 기울기를 구하고,
#  접선의 기울기가 낮은 방향으로 W의 값을 변경하고 다시 미분하고 이 과정을 접선의 기울기가 0인 곳을 향해 W의 값을 변경하는 작업을 반복하는 것

# 학습률(learning rate) : 이동 거리를 정해주는  것  

# cost 의 예측 값을 편미분을 통해서 a에대한 편미분, b에 대한 편미분을 한다 

# pandas (판다스) : 파이썬 데이터 처리를 위한 라이브러리 
# Numpy (넘파이) : 수치 데이터를 다루느는 파이썬 패키지 
# Matplotlib (맷플롭립) : 데이터를 차트(chart)나 플롯(plot)으로 시각화 (visulaization)하는 패키지 
# 추후에 자세히 공부

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#공부시간 X와 성적 Y의 리스트를 만듭니다.
data = [[2, 81], [4, 93], [6, 91], [8, 97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

#그래프로 나타내 봅니다.
plt.figure(figsize=(8,5))
plt.scatter(x, y)
plt.show()

# 리스트로 되어 있는 x와 y값을 넘파이 배열로 바꾸어 줍니다.
# (인덱스를 주어 하나씩 불러와 계산이 가능해 지도록 하기 위함입니다.)
x_data = np.array(x)
y_data = np.array(y)

# 기울기 a와 절편 b의 값을 초기화 합니다.
a = 0
b = 0

#학습률을 정합니다.
lr = 0.03 

#몇 번 반복될지를 설정합니다.
epochs = 2001 

#경사 하강법을 시작합니다.
for i in range(epochs):                               # epoch 수 만큼 반복
    y_hat = a * x_data + b                            # y를 구하는 식을 세웁니다 (Hy)
    error = y_data - y_hat                            # 오차를 구하는 식입니다.
    a_diff = -(2/len(x_data)) * sum(x_data * (error)) # 오차함수를 a로 미분한 값입니다. 
    b_diff = -(2/len(x_data)) * sum(error)            # 오차함수를 b로 미분한 값입니다. 
    a = a - lr * a_diff                               # 학습률을 곱해 기존의 a값을 업데이트합니다.
    b = b - lr * b_diff                               # 학습률을 곱해 기존의 b값을 업데이트합니다.
    if i % 100 == 0:                                  # 100번 반복될 때마다 현재의 a값, b값을 출력합니다.
        print("epoch=%.f, 기울기=%.04f, 절편=%.04f" % (i, a, b))


# 앞서 구한 기울기와 절편을 이용해 그래프를 그려 봅니다.
y_pred = a * x_data + b
plt.scatter(x, y)
plt.plot([min(x_data), max(x_data)], [min(y_pred), max(y_pred)])
plt.show()

