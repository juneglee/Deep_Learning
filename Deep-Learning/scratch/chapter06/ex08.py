# CNN 시각화 하기 
# 1번째 층의 가중치 시각화 하기 
# ex07에서 1번째 층의 합성곱 계층의 가중치는 형상이 (30 1 5 5) - (필터 30, 채널 1, 5x5 크기)이다 
# 필터의 크기가 5 x 5이고 채널이 1개라는 것은 이 필터를 1채널의 회색조 이미지로 시각화 할 수 있다는 뜻이다 

# 가중치 비교 
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from ex06 import SimpleConvNet

def filter_show(filters, nx=8, margin=3, scale=10):
    FN, C, FH, FW = filters.shape
    ny = int(np.ceil(FN / nx))

    fig = plt.figure()
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
    for i in range(FN):
        ax = fig.add_subplot(ny, nx, i+1, xticks=[], yticks=[])
        ax.imshow(filters[i, 0], cmap=plt.cm.gray_r, interpolation='nearest')
    plt.show()


network = SimpleConvNet()
# 무작위(랜덤) 초기화 후의 가중치
filter_show(network.params['W1'])

# 학습된 가중치
network.load_params("params.pkl")
filter_show(network.params['W1'])

# 학습된 마친 필터는 규칙성이 있는 이미지가 되었다. 
# - 흰색에서 검은색으로 점차 변화는 필터와 덩어리(블롭 blob)가 진 필터 등 규칙을 띄는 필터로 바뀌었다

# 규칙성 있는 필터는 무엇을 보고 있는 걸까?
# - 에지(색상이 바뀐 경계선) 와 블롭 (국소적으로 덩어리진 영역)을 보고 있다 
# 이처럼 합성곱 계층의 필터는 에지나 블롭 등의 원시적인 정보를 추출할 수 있다 

# 층 깊이에 따른 추출 정보 변화 
# 1번째 층의 합성곱 계층에서는 에지나 블롭 등의 저수준 정보가 추출되고, 
# 계층이 깊어질수록 추출되는 정보(정확히는 강하게 반응하는 뉴런)는 더 추상화 된다는 것을 알수 있다 

# 합성곱 계층을 여러겹 쌓으면, 층이 깊어지면서 더 복잡하고 추상화된 정보가 추출된다는 것 
# 처음 층은 단순한 에지에 반응하고, 이어서는 덱스트를 반응, 더 복잡한 사물의 일부를 반응하도록 변화한다 
# 즉, 층이 깊어지면서 뉴런이 반응하는 대상이 단순한 모양에서 고급 정보로 벼노하해 간다. 다시말하면 사물의 의미를 이해하도록 변화한다 
