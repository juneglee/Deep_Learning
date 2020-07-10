# ReLU 함수 (Rectified Linear Unit, 렐루 함수 )
# 시그모이드 함수는 신경망 분야에서 오래전부터 이용해 왔으나, 최근에는 ReLU 함수를 주로 이용
# 입력이 0을 넘으면 그 입력을 그대로 출력하고, 0이하이면 0을 출력하는 함수 

import numpy as np

def relu(x):
    return np.maximum(0 , x) # 두 입력 중에 큰 값을 선택해 반환
