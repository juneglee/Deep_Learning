# 매개 변수 갱신 
# 신경망의 학습의 목적은 손실 함수의 값을 가능한 한 낮추는 매개변수를 찾는 것이다 
# 매개변수의 최적값을 찾는 문제이며, 이러한 문제를 최적화 aptimization 라 한다 

# 매개 변수의 기울기를 구해, 기울어진 방향으로 매개변수 값을 갱신하는 일을 면번이고 반복해서 점점 최적의 값에 다가간다 
# 이것이 확률적 경사 하강법 (SGD)라는 단순한 방법

# 확률적 경사 하강법(SGD)
class SGD:
    def __init__(self, lr = 0.01):
        self.lr = lr
        # lr 은 초기화 때 받는 인수 lr은 learning rate(학습률)이라는 뜻
     
    def update(self, params, grads): # SGD를 반복해서 돌린다 
        # params, grads 은 딕셔너리 변수 
        # 딕셔너리 변수 Dictionary변수에 key와 value
        for key in params.keys():
            parmas[key] -= self.lr * grads[key]

network = TwoLayerNet(...)
optimizer = SGD()

for i in range(100):
    ...
    x_batch, t_batch = get_mini_batch(...) # 미니배치 
    grads = network.gradient(x_batch, t_batch)
    params = network.params
    optimizer.update(params, grads)
    ...
    # 매개변수 갱신은 optimizer가 책임지고 수행하니 우리는 optimizer에 매개변수와 기울기 정보만 넘겨주면 된다.

# SGD의 단점
# 비등방성 (anisotropy) : 방향에 따라 성질, 즉 여기에서는 기울기가 달라지는 함수
# 탐색 경로가 비효율적이라는 것 

# SGF의 이러한 단점을 개선해주는 모멘텀, AdaGrad, Adam이라는 방법이 있다 





