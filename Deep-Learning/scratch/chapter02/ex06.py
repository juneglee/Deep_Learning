# 3층 신경망 구현하기 

# 입력층(0층) 은 2개 , 첫번째 은닉층 (1층) 은 3개 , 두번째 은닉층 (2층) 2개, 출력층 (3층)은 2개의 뉴런으로 구성
import numpy as np

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def identity_function(x):
    return x

def init_network():
    network = {}
    network['w1'] = np.array([[0.1, 0.3, 0.5] , [0.2 ,0.4 ,0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['w2'] = np.array([[0.1, 0.4] , [0.2 ,0.5], [0.3 ,0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['w3'] = np.array([[0.1, 0.3] , [0.2 ,0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

def forword(network, x):
    W1, W2, W3 = network['w1'], network['w2'], network['w3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y

network = init_network()
x = np.array([1.0, 0.5])
y = forword(network, x)
print(y) 
# [0.31682708 0.69627909]