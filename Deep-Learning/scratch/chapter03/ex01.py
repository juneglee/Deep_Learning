# 평균 제곱 오차 (mean squared error : MSE)

import numpy as np

def mean_squared_error(y , t):
    return 0.5*np.sum(y-t)**2
# y : 신경망의 출력(신경망이 추정한 값)
# t : 정답레이블 
# t 는 한 원소만 1로 하고 그외는 0으로 나타느내느 표기버빈 원-핫 인코딩을 사용

# 교차 엔트로피 오차 (cross entropy error: CEE)

def cross_entropy_error(y,t):
    delta=1e-7
    return -np.sum(t*np.log(y+delta))
# delta : log()함수에 0을 입력하면 마니어스 무한대를 뜻하는 -infㄱ 되어 더이상 계산을 진행할 수 업게 되기 떄문에 
# 아주 작은 값인 보정값을 넣어준다 