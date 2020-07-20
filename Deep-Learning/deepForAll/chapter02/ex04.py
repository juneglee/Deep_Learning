# 다중 선형 회귀 분석(Multiple Linear Regression Analysis)
# : 정확한 정보를 예측하기 위해서 정보를 추가해 새로운 예측 값을 구하려면 변수의 개수를 늘린다 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d # 3D 그래프 그리는 라이브러리 

#공부시간 X와 성적 Y의 리스트를 만듭니다.
data = [[2, 0, 81], [4, 4, 93], [6, 2, 91], [8, 3, 97]]
x1 = [i[0] for i in data] 
x2 = [i[1] for i in data]
# x1과 x2라는 두개의 독립 변수 리스트를 만들어 준다 
y = [i[2] for i in data]

#그래프로 확인해 봅니다.
ax = plt.axes(projection='3d') # 그래프 유형
ax.set_xlabel('study_hours')
ax.set_ylabel('private_class')
ax.set_zlabel('Score')
ax.dist = 11 
ax.scatter(x1, x2, y)
plt.show()

#리스트로 되어 있는 x와 y값을 넘파이 배열로 바꾸어 줍니다.
# (인덱스를 주어 하나씩 불러와 계산이 가능해 지도록 하기 위함입니다.)
x1_data = np.array(x1)
x2_data = np.array(x2)
y_data = np.array(y)

# 기울기 a와 절편 b의 값을 초기화 합니다.
a1 = 0
a2 = 0
b = 0

#학습률을 정합니다.
lr = 0.05 

#몇 번 반복될지를 설정합니다.
# (0부터 세므로 원하는 반복 횟수에 +1을 해 주어야 합니다.)
epochs = 2001 

#경사 하강법을 시작합니다.
for i in range(epochs):                                  # epoch 수 만큼 반복
    y_pred = a1 * x1_data + a2 * x2_data + b             # y를 구하는 식을 세웁니다
    error = y_data - y_pred                              # 오차를 구하는 식입니다.
    a1_diff = -(1/len(x1_data)) * sum(x1_data * (error)) # 오차함수를 a1로 미분한 값입니다. 
    a2_diff = -(1/len(x2_data)) * sum(x2_data * (error)) # 오차함수를 a2로 미분한 값입니다. 
    b_diff = -(1/len(x1_data)) * sum(y_data - y_pred)    # 오차함수를 b로 미분한 값입니다.
    a1 = a1 - lr * a1_diff                               # 학습률을 곱해 기존의 a1값을 업데이트합니다.
    a2 = a2 - lr * a2_diff                               # 학습률을 곱해 기존의 a2값을 업데이트합니다.
    b = b - lr * b_diff                                  # 학습률을 곱해 기존의 b값을 업데이트합니다.
    if i % 100 == 0:                                     # 100번 반복될 때마다 현재의 a1, a2, b값을 출력합니다.
        print("epoch=%.f, 기울기1=%.04f, 기울기2=%.04f, 절편=%.04f" % (i, a1, a2, b))

