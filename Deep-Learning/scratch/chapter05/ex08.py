# 은닉층의 활성화 값 분포 
# 은닉층의 활성화 값(활성화 함수의 출력 데이터)의 분포를 관찰하면 중요한 정보를 얻을 수 있다 
# 

# 활성화 함수로 시그모이드 함수를 사용하는 5층 신경망에 무작위로 생성한 일력 데이터를 흘리며, 
# 각층의 활성화 값 분포를 히스토그램으로 그려본다

import numpy as np
import matplotlib.pyplot as plt 

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.random.randn(1000, 100) # 1000개의 데이터
node_num = 100                 # 각 은닉층의 노드(뉴런) 수
hidden_layer_size = 5          # 은닉층 5개
activations = {}               # 이곳에 활성화 결과(활성화 값)를 저장

for i in range(hidden_layer_size):
    if i != 0:
        x = activations[i - 1]

    # w = np.random.randn(node_num, node_num) * 1 # 표준편차를 1
    # w = np.random.randn(node_num, node_num) * 0.01 # 표준편차를 0.01
    w = np.random.randn(node_num, node_num) / np.sqrt(node_num) # Xavier 초깃값 
    a = np.dot(x, w)
    z = sigmoid(a)
    activations[i] = z

# 히스토그램 그리기

for i, a in activations.items():
    plt.subplot(1, len(activations), i+1)
    plt.title(str(i+1) + "-layer")
    plt.hist(a.flatten(), 30, range=(0,1))
plt.show()

# 표준편차를 1로 했을 때 
# 각 층의 활서오하 값들이 0과 1에 치우쳐 분포되어 있으며, 
# 여기에서 사용한 시그모이드 함수는 그 출력이 0에 가까워지자(또는 1에 가까워지자) 그 미분은 0에 다가간다.
# 그래서 데이터가 0과 1에 치우쳐 분포하게 되면 역전파의 기울기 값이 점점 작아지다가 사라진다
# 이것이 기울기 소실이라 알려진 문제이다 

# 표준편차를 0.11로 했을 때 
# w(표준편차)를 0.01로 한 정규분포의 경우 각 층의 활성화 값 분포는 
# 0.5부근에 집중되었다, 앞의 처럼 0과 1에 치우치진 않았으니 기울기 손실 문제는 일어나지 않지만, 
# 활성화 값들이 치우쳤다는 것은 표현력 관점에서는 큰 문제가 있는것이다. 
# 이 상황에서는 다수의 뉴런이 거의 같은 값으 출려하고 있으니 뉴런을 여러개 둔 의가 엇어진다는 뜻이다 
# 그래서 활정화 값들이 치우치면 표현력을 제한한다는 관점에서 문제가 된다.

# 표준편차를 Xavier 초깃값 했을 때
# 층이 깊어지면서 형태가 다소 일그러지지만, 앞에서 본 방식보다는 확실히 넓게 분포된다
# 각 층에 흐르는 데이터는 적당히 퍼져 있으므로, 시그모이드 함수의 표현력도 제한 받지 않고 
# 학습이 효율적으로 이뤄질 것으로 예상
# 이때 오른쪽이 약간 일그러짐이 있으면, 이는 tanh함수(쌍곡선 함수)를 이용하면 개선된다. 
# tanh 함수도 sigmoid함수와 같은 S자 모양 곡선 함수이다. 
# 다만, tanh은 원점 (0 , 0)에서 대칭인 S 곡선인 반면 sigmoid함수는 (x,y) = (0, 0.5)에서 대칭인 S곡선이다 