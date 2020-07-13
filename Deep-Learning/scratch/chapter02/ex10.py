# 배치 처리 
# 하나로 묶은 입력 데이터를 배치 batch라 하며, 이미지가 지폐처럼 바발로 묶여 있다고 생각 

# 배치 처리는 컴퓨터로 계산할 때 큰 이점을 준다. 이미지 1장단 처리 시간을 대폭 줄여주기 때문
# 1. 수치 게산 라이브러리 대부분이 큰 배열을 효율적으로 처리할 수 있도록 고도로 최적화 되어 있기 때문이고 
# 2. 커다란 신경망에서는 데이터 전송이 병목으로 작용하는 경우가 자주 있는데, 배치 처리를 함으로써 버스에 주는 부하는 줄인다 
# 즉. 배치 처리를 수행함으로써 큰 배열로 이뤄진 계산을 하게 되는데, 
#     컴퓨터에서는 큰 배열을 한꺼번에 계산하는 것이 분활된 작은 배열을 여러번 계산하는 것보다 빠르다  
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    w1, w2, w3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, w1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, w3) + b3
    y = softmax(a3)

    return y


x, t = get_data()
network = init_network()

batch_size = 100 # 배치 크기
accuracy_cnt = 0

for i in range(0, len(x), batch_size):
    # range(start, end) - start 에서 end-1까지 정수
    # range(start, end, step) - start 에서 end-1까지 step의 간격의 정수 
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    # x[i:i+batch_size] - i 번째 부터 i+batch_size 번째까지의 데이터를 묶는다 
    # batch_size가 100이므로 x[0:100], x[100:200], 와 같이 앞에서부터 100장씩 묶어 꺼낸다 
    p = np.argmax(y_batch, axis=1)
    # argmax() - 최댓값의 인덱스를 가져온다 
    # 다만 여기에서는 axis=1이라는 인수를 추가한 것에 주의 
    # 100x10 의 배열 중 1번째 차원을 구성하는 각 원소에서 (1번째 차원의 축으로 최댓값의 인덱스를 찾도록 한것)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])
    # 마지막으로 배치 단위로 분류한 결과를 실제 답과 비교   

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))







