# ReLU를 사용할 때의 가중치 초깃값 
# ReLU를 이용할 때는 ReLU에 특화된 초깃값을 이용하라고 권장합니다.
# 이 특화된 초깃값을 찾아낸 카이밍 히의 이름 따 He 초깃값이라고 한다. 

# 활성화 함수로 ReLU를 사용할 때는 He 초깃값을 
# sigmoid 등의 S자 모양 곡선일 떄는 Xavier 초깃값을 사용 


#--------------------------------------------
# MINIST 데이터셋으로 본 가중치 초깃값비교 
import os
import sys

sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from common.util import smooth_curve
from common.multi_layer_net import MultiLayerNet
from common.optimizer import SGD


# 0. MNIST 데이터 읽기==========
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

train_size = x_train.shape[0]
batch_size = 128
max_iterations = 2000


# 1. 실험용 설정==========
weight_init_types = {'std=0.01': 0.01, 'Xavier': 'sigmoid', 'He': 'relu'}
optimizer = SGD(lr=0.01)

networks = {}
train_loss = {}
for key, weight_type in weight_init_types.items():
    networks[key] = MultiLayerNet(input_size=784, hidden_size_list=[100, 100, 100, 100],
                                  output_size=10, weight_init_std=weight_type)
    train_loss[key] = []


# 2. 훈련 시작==========
for i in range(max_iterations):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    for key in weight_init_types.keys():
        grads = networks[key].gradient(x_batch, t_batch)
        optimizer.update(networks[key].params, grads)
    
        loss = networks[key].loss(x_batch, t_batch)
        train_loss[key].append(loss)
    
    if i % 100 == 0:
        print("===========" + "iteration:" + str(i) + "===========")
        for key in weight_init_types.keys():
            loss = networks[key].loss(x_batch, t_batch)
            print(key + ":" + str(loss))


# 3. 그래프 그리기==========
markers = {'std=0.01': 'o', 'Xavier': 's', 'He': 'D'}
x = np.arange(max_iterations)
for key in weight_init_types.keys():
    plt.plot(x, smooth_curve(train_loss[key]), marker=markers[key], markevery=100, label=key)
plt.xlabel("iterations")
plt.ylabel("loss")
plt.ylim(0, 2.5)
plt.legend()
plt.show()

# 층별 뉴런 수가 100개인 5층 신경망에서 활서오하 함수 ReLU를 사용 
# std = 0.01일 때는 학습이 전혀 이뤄지지 않습니다. 앞서 활성화 값의 분포에서 본 것처럼 순전파 때 너무 작은 값이 흐르기 떄문
# 그로 인해 역전파 떄의 기울기도 작아져 가중치가 거의 갱신되지 않는 것이다.
# 반대로 Xavier 와 He 초깃값의 경우는 학습이 순조롭게 이뤄지고 있다. 다만 학습 진도는 He 초깃값 쪽이 더 빠르다 