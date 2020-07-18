# 활성화 함수 계층 구현하기 (ReLU, Sigmoid)
# 
# ReLU 계층 
# forward() 와 backward() 함수는 넘파이 배열을 인수로 반듣다고 가장 
# common/layers.py


# ReLU클래스는 mask라는 인스턴스 변수를 가집니다. mask는 True/False 로 구성된 넘파이 배열로,
# 순전파인 입력인 x의 원소 값이 0dlgkdls 인덱는 True, 그외(0보다 큰 원소)는 False로 유지합니다. 

import numpy as np

x = np.array( [[1.0, -0.5], [-2.0, 3.0]])
print(x)
#[[ 1.  -0.5]
#  [-2.   3. ]]
mask = (x <= 0)
print(mask)
# [[False  True]
#  [ True False]]

# 다음과 같이 순전파일 떄의 입력값이 0이하면 역전파 때의 값은 0이 돼야 합니다.
# 그래서, 역전파 떄는 순전파 떄 만들어둔 mask 를 써서 mask 의 원소가 True인 곳에는 
# 상류에서 전파된 dout을 0으로 설정합니다.
#  