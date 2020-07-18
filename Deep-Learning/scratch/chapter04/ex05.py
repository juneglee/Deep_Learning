# Affine/Softmax 계층 구현하기 

# Affine 계층 
# 신경망의 순전파 떄 수행하는 행렬의 내적은 기하학하에서는 어파인 변환이라고 한다 
import numpy as np

X = np.random.rand(2) # 입력
W = np.random.rand(2, 3) # 가중치
B = np.random.rand(3) # 편향

print(X.shape) 
print(W.shape)
print(B.shape)

Y=np.dot(X, W) + B  # dot : 내적을 계산하는 노드 
print(Y) # [0.59365089 1.07026112 0.95747572]

# 배치용 Affine (데이터 N개를 묶어 순전파하는 경우)

X_dot_W = np.array( [[0, 0, 0], [10, 10, 10]])
NB = np.array([1, 2, 3])

NY = X_dot_W + NB
print(NY)
# [[ 1  2  3]
#  [11 12 13]]

# 순전파의 편향 덧셈은 각각의 데이터(1번째 데이터, 2번째 데이터, ...) 에 더해집니다. 
# 그래서 역전파 떄는 각 데이터의 역전파 값이 편향의 원소에 모여야 합니다. 

dB = np.sum(NY, axis=0)
print(dB) # [12 14 16]
