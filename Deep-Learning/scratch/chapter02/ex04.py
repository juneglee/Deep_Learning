# 행렬의 내적(행렬 곱)
 
import numpy as np

# 2 X 2 / 2 X 2
A = np.array([[1, 2] , [3 ,4]])
print(A.shape)

B = np.array([[5, 6] , [7 ,8]])
print(B.shape)

print(np.dot(A, B))

print("-----------------------")
# 2 X 3 / 3 X 2
C = np.array([[1, 2, 3] , [3 ,4 ,5]])
print(C.shape)

D = np.array([[5, 6] , [7 ,8] , [9 ,1]])
print(D.shape)

print(np.dot(C, D))
print("-----------------------")

# 3 X 2 / 2
E = np.array([[5, 6] , [7 ,8] , [9 ,1]])
print(E.shape)

F = np.array([7, 8])
print(F.shape)

print(np.dot(E, F))