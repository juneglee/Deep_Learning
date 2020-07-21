# 합성곱/풀링 계층 구현하기 

import numpy as np
# 4차원 배열 
x = np.random.rand(10, 1, 28, 28) # 높이 28, 너비 28, 채널 1, 데이터 10
print(x.shape)
print(x[0].shape) # 첫번째 데이터 # (1, 28, 28)
print(x[1].shape) # 두번째 데이터 # (1, 28, 28)
print(x[0,0]) # 첫번째 데이터의 첫 채널의 공간 데이터 
