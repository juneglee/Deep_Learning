# 모멘텀(Momentum) 
# 
class Momentum:

    """모멘텀 SGD"""

    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.v = None
        
    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, val in params.items():                                
                self.v[key] = np.zeros_like(val)
                
        for key in params.keys():
            self.v[key] = self.momentum*self.v[key] - self.lr*grads[key] 
            params[key] += self.v[key]
        
        # 인스턴스 변수 v가 물체의 속도 
        # v는 초기화 때는 아무 값도 담지 않고, 대신 update 가 처음 호출 될 때
        # 매개변수 와 같은 구조의 데이터를 딕셔너리 변수로 저장 