# AdaGrad
# 신경망 학습에서는 학습률이 중요하다, 
# 이 값이 너무 작으면 학습 시간이 너무 길어지고, 반대로 너무 크면 발산하여 학습이 제대로 이뤄지지 않는다 
# 이 학습률을 정하는 효과적인 기술로 학습률 감소 Learning rate decay 가 있다
# AdaGrad 는 각각의 매개변수에 맞춤형 값을 만들어 준다 
# 기존의 식에서 h 라는 변수가 등장 
# 
# AdaGrad는 과거의 기울기를 제곱하여 계속해 더해간다. 그래서 학습을 진행할수록 갱신 정도가 약해진다 
# 실제로 무한히 계속 학습한다면 어느 순간 갱신량이 0이 되어 전혀 갱신되지 안게 된다. 
# 이러한 문제를 개선한 방법으로 RMSProp 라는 방법이 있다
# RMSProp 은 과거의 모든 기울기를 균힐하게 더해가는 것이 아니라, 먼 과거의 기울기는 서서히 잊고 새로운 기울기 정보를 크게 반영 
# 이를 지수이동평균(Exponential Moving Average: EMA)라 하여, 과거 기울기의 반영 규모를 기하급수적으로 감소시킨다.

class AdaGrad:

    """AdaGrad"""

    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None
        
    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)
            
        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
            # 여기서 주의할 것은 마지막 줄에서 1e-7이라는 작은 값을 더하는 부분이다
            # 이 작은 값은 self.h[key]에 담겨 있다 해도 0으로 나누는 사태를 막아준다

class RMSprop:

    """RMSprop"""

    def __init__(self, lr=0.01, decay_rate = 0.99):
        self.lr = lr
        self.decay_rate = decay_rate
        self.h = None
        
    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)
            
        for key in params.keys():
            self.h[key] *= self.decay_rate
            self.h[key] += (1 - self.decay_rate) * grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
