# 신경망의 내적 
 
import numpy as np

X = np.array([1, 2])
print(X.shape)

W = np.array([[1, 2, 3] , [3 ,4 ,5]])
print(W.shape)

Y = np.dot(X, W)

# x와 W 의 대응하는 차원으 원소 수가 같아야 한다 