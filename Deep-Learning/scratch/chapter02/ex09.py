# 신경망 추론 처리 
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test
    # normalize을 true로 설정하면 0 ~ 255 범위인 픽셀의 값을 0.0 ~1.0 범위로 변한(단순히 픽셀의 값을 255로 나눈다)

def init_network():
    with open("sample_weight.pkl", 'rb') as f: 
        # pickle 파일인 sample_weight.pkl에 저장된 학습된 가중치 매개변수
        # 이 파일에는 가중치와 편향 매개변수가 딕셔너리 변수로 저장되어 있다 
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

x, t = get_data()
network = init_network()
accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p= np.argmax(y) # 확률이 가장 높은 원소의 인덱스를 얻는다.
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy:" + str(float(accuracy_cnt) / len(x))) # 정확도(Accuracy) : 분류가 얼마나 올바른가  

# 이처럼 데이터를 특정 범위로 변환하는 처리를 정규화(normalization) 하고, 
# 신경망의 입력 데이터에 특정 변환을 가하는 것을 전치리(pre-processing)