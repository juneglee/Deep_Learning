# 드롭아웃
# 신경망이 모델이 복잡해지면 감소만으로는 대응하기 어려워 진다 
# 이럴 때는 흔히 드롭아웃 Dropout이라는 기봅을 이용
# 트롭아웃은 뉴런을 임의로 삭제하면서 학습하는 방법이다. 훈련 때 은닉층의 뉴런을 무작위로 골라 삭제 
# 훈련 때는 데이터를 흘릴 때마다 삭제할 뉴런을 무작위로 선택하고, 시험 떄는 모든 뉴런에 신호를 전달 
# 단, 시험 때는 각 뉴런의 출력에 훈련 때 삭제한 비율을 곱하여 출력 

class Dropout:
    def __init__(self, dropout_ratio=0.5):
        self.dropout_ratio =dropout_ratio
        self.mask = None
    
    def forward(self, x, train_flg = True):
        if train_flg:
            self.mask = np.random.rand(*x.shape) > self.dropout_ratio
            return x * self.mask
        else:
            return x * (1.0 - self.dropout_ratio)

    def backward(self, dout):
        return dout * self.mask

# MINIST 데이터셋으로 확인
import os
import sys
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from common.multi_layer_net_extend import MultiLayerNetExtend
from common.trainer import Trainer

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

# 오버피팅을 재현하기 위해 학습 데이터 수를 줄임
x_train = x_train[:300]
t_train = t_train[:300]

# 드롭아웃 사용 유무와 비울 설정 ========================
use_dropout = True  # 드롭아웃을 쓰지 않을 때는 False
dropout_ratio = 0.2
# ====================================================

network = MultiLayerNetExtend(input_size=784, hidden_size_list=[100, 100, 100, 100, 100, 100],
                              output_size=10, use_dropout=use_dropout, dropout_ration=dropout_ratio)
trainer = Trainer(network, x_train, t_train, x_test, t_test,
                  epochs=301, mini_batch_size=100,
                  optimizer='sgd', optimizer_param={'lr': 0.01}, verbose=True)
trainer.train()

train_acc_list, test_acc_list = trainer.train_acc_list, trainer.test_acc_list

# 그래프 그리기==========
markers = {'train': 'o', 'test': 's'}
x = np.arange(len(train_acc_list))
plt.plot(x, train_acc_list, marker='o', label='train', markevery=10)
plt.plot(x, test_acc_list, marker='s', label='test', markevery=10)
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()

# 드룹아웃을 적용하니 운련데이터와 시험데이터에 대한 정확도 차이가 줄어든다 
# 또한, 후련 데이터에 대한 정확도가 100% 에 도달하지 않게 되었다, 
# 이처럼 드룹아웃을 이용하면 표현력을 높이면서도 오버피팅을 억제할 수 있다 

# 기계학습에서는 앙상블 학습(ensemble learning)을 이용한다 
# 개별적으로 학습시킨 여러 모델의출력을 평군 내어 추론하는 방식 
# ex) 네트워크를 5개 줍니하여 따로 학습시키고, 시험 때는 그 5개의 출력을 평균을 낸다 
# 앙상블 학습은 드롭아웃과 밀접
# 드룹아웃이 학습 때 뉴런을 무작위로 삭제하는 행위는 매번 다른 모델을 학습시키는 것으로 해석시키는 것으로 해석할 수 있기 때문 
# 추론 때는 뉴런의 출력에 삭제한 비율을 곱함으로서 앙상블 학습에서 여러 모델의 평균을 내는 것과 같은 효과는 얻는다 
# 즉, 드롭아웃은 앙상블 학습과 같은 효과를 하나의 네트워크로 구현했다고 생각할 수있다 

