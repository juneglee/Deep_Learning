#  오차 역전파법으로 구한 기울기 검증하기 
# 기울기를 구하나느 방법 (두가지 : 수치 미분, 해석적으로 수식을 풀어 구하는 방법)
# 해석적 바법은 오차역전파 법을 이용하여 매개변수가 많아도 효율적으로 계산 (수치 미분은 느리다)

# 기울기 확인(gradient check)
# : 수치 미분의 구현에는 버그가 숨어 있기 때문에 어려운 반면, 오차 역전파법은 구현하기 복자배서 종종 실수를 한다 
# 그래서 수치 미분의 결과와 오차 역전파법의 결과를 비교하여 오차역전파법을 제대로 구현했는지 검증하고 한다 
# 이처럼 두 방식으로 구한 기울기가 일치함을 확인하는 작접 

import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

# 데이터 읽기
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

x_batch = x_train[:3]
t_batch = t_train[:3]

grad_numerical = network.numerical_gradient(x_batch, t_batch)
grad_backprop = network.gradient(x_batch, t_batch)

# 각 가중치의 절대 오차의 평균을 구한다.
for key in grad_numerical.keys():
    diff = np.average( np.abs(grad_backprop[key] - grad_numerical[key]) )
    print(key + ":" + str(diff))
# 언제나 처럼 가장 먼저 MNIST 데이터셋을 읽습니다. 
# 그리고 훈련데이터 일부를 수치 미분으로 구한 기울기와 오차 역전파법으로 구한 기울기의 오차를 확인
# 여기에서는 각 가중치 매개변수의 차이를 절댓값으로 구하고, 이를 평균한 값이 오차가 된다.

# W1:4.0220968473795646e-10
# b1:2.493100577104267e-09
# W2:4.70769918323676e-09
# b2:1.3933478569955192e-07

# 수치미분과 오차 역전파법의 결과 오차가 0이 되는 일은 드뭅니다. 
# 이는 컴퓨터가 할 수 있는 계산의 정밀도가 유한하기 떄문 (가령 32비트 부동소수점)
# 이 정밀도의 한계 때문에 오차는 대부분 0이 되지는 않지만, 올바르게 구현했다면 0에 아주 가까운 작은 값이 됩니다.
# 만약 그 값이 크면 오차역전파법을 잘못 구현했다고 의심해야 한다 