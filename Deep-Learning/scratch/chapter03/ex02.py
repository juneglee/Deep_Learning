# 미니 배치 학습 
# 훈련데이터에 대한 손실함수의 값을 구하고, 그값을 최대한 줄여주는 매개변수를 찾는다 
# 이렇게 하려면 모든 훈련 데이터를 대상으로 손실 함수 값을 구해야 한다 

# 일부를 미니배치(mini-batch)하여 전체 훈련데이터 중 일부의 데이터를 무작위로 뽑아서 학습하는 방법

import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) =\
    load_mnist(normalize=True, one_hot_label =True)
    # one_hot_label : 원-핫 인코딩 : 정답 위치의 원소만 1이고 나머지가 0인 배열 

print(x_train.shape) # (60000, 784) - 훈련데이터가 60000개고, 입력 데이터는 784열인 이미지 데이터 
print(t_train.shape) # (60000, 10) - 훈련데이터가 60000개고, 정답 레이블는 10줄인 이미지 데이터 

# 훈련데이터에서 무작위로 10장만 뺄때 - np.random.choice()
train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print(np.random.choice(60000, 10))

# 미니배치 학습 이용 예 
# 텔레비전 시청률도 모든 세ㅐ의 텔레비전이 아니라 선택된 일부 가구의 텔레비전만을 대상으로 구한다 
# 이처럼, 시청률과 마찬가지로 미니배치의 손실함수도 일부 표본 데이터로 젠체를 비슷하게 계측한다 

def cross_entropy_error(y, t):
    if y.ndim ==1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y))/batch_size

# y : 신겸망의 출력
# t : 정답 레이블 
# y가 1차원이라면, 즉 데이터 하나당 교차 엔트로피 오차를 구하는 경우 reshape 함수로 데이터 형상을 바꿔준다

# 정답 레이블이 원-핫 인코딩이 아니라 2나 7 등의 숫자 레이블로 주어졌을 때의 교차 엔트로피 오차
def cross_entropy_error(y, t):
    if y.ndim ==1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t]))/batch_size

# 이 구현은 원-핫 인코딩일 때 t가 0인 원소는 교차 엔트로피 오차도 0이므로, 그 계산은 무시해도 좋다는 것이 핵심
# np.log(y[np.arange(batch_size), t])
# np.arange(batch_size)는 0부터 batch_size - 1까지 배열을 생성 
# 즉, batch_size가 5이면 np.arange(batch_size)는 [0, 1, 2, 3, 4]라는 넘파이 배열을 생성 
#     t에는 레이블이 [2, 7, 0, 9, 4] 와 같이 저장 