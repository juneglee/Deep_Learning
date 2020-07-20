# 로지스틱 회귀 (logistic regression)
# : 참인지 거짓인지를 구분
# 참(1) 과 거짓(0) 사이를 구분하는 s자 형태의 선을 그어주느 작업

# 시그모이드 함수 (sigmoid function)
# : 선형 회귀와 마찬가지로 ax + b 의 형태로 나타내며
# a는 경사도를 결정 a 값이 커지면 경사가 커지고 a 값이 작아지면 경사가 작아진다
# a 값이 작이졈 오차는 무한대로 커지며, a값이 커진다고 해서 무한대로 커지지 않습니다 

# 오차 공식 
# 시그모이드 a와 b의 값을 구하는 송식은 경사 하강법 

# 로그 함수 
# 실제 값이 1일 때와 실제값이 0 일때 그래프를 구할 수 있으며,
# 실제 값이 1일 때는 예측 값이 1일 때 오차가 0이고, 반대로 예측 값이 0에 가까울 수록 오차는 커진다 
# 실제 값이 0일 때는 예측 값이 0일 수록 오차가 없고, 1에 가까워질수록 오차가 매우 커진다. 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#공부시간 X와 성적 Y의 리스트를 만듭니다.
data = [[2, 0], [4, 0], [6, 0], [8, 1], [10, 1], [12, 1], [14, 1]]

x_data = [i[0] for i in data] # 공부시간
y_data = [i[1] for i in data] # 성적

#그래프로 나타내 봅니다.
plt.scatter(x_data, y_data)
plt.xlim(0, 15)
plt.ylim(-.1, 1.1)

# 기울기 a와 절편 b의 값을 초기화 합니다.
a = 0
b = 0

#학습률을 정합니다.
lr = 0.05 

#시그모이드 함수를 정의합니다.
def sigmoid(x):
    return 1 / (1 + np.e ** (-x))

#경사 하강법을 실행합니다.
for i in range(2001):
    for x_data, y_data in data:
        a_diff = x_data*(sigmoid(a*x_data + b) - y_data)  # a에 관한 편미분, 앞써 정의한 sigmoid 함수 사용
        b_diff = sigmoid(a*x_data + b) - y_data           # b에 관한 편비분
        a = a - lr * a_diff                               # a를 업데이트 하기 위해, a_diff에 학습률을 lr을 고합 값을 a에서 뻄 
        b = b - lr * b_diff                               # b를 업데이트 하기 위해, b_diff에 학습률을 lr을 고합 값을 b에서 뻄 
        if i % 1000 == 0:    # 1000번 반복될 때마다 각 x_data값에 대한 현재의 a값, b값을 출력합니다.
            print("epoch=%.f, 기울기=%.04f, 절편=%.04f" % (i, a, b))


# 앞서 구한 기울기와 절편을 이용해 그래프를 그려 봅니다.
plt.scatter(x_data, y_data)
plt.xlim(0, 15)
plt.ylim(-.1, 1.1)
x_range = (np.arange(0, 15, 0.1)) #그래프로 나타낼 x값의 범위를 정합니다.
plt.plot(np.arange(0, 15, 0.1), np.array([sigmoid(a*x + b) for x in x_range]))
plt.show()

# 만약 여기에 입력 밧이 추가되어 세개 이상의 입력 값을 다룬다면, 
# 시그모이드 함수가 아니라 소프트맥스 (softmax)라는 함수를 ㅆ야 한다 

