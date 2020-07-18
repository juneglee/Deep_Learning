# Affine/Softmax 계층 구현하기 

# Softmax-With-Loss 계층 
# 소프트 맥스 함수는 입력값을 정규화하여 출력 

# 신경망에서 수행하는 작업은 학습과 추론 두가지 입니다. 
# 추론할 때는 softmax를 사용하지 않고, affine 을 출력 인식 결과로 이용 
# 신경망에서 정규화 하지 않는 출력 결과에서는 Softmax 앞에 Affine 계층의 출력을 정수 score라 한다 
# 즉, 신경망 출론에서 답을 하나만 내는 경우네는 가장 높은 점수만 알면 되니, Softmax계층은 필요 없다 

# 손실함수인 교차 엔트로피 오차도 포함하여 Softmax - with -Loss 계층을 구현한다 

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None # 손실함수
        self.y = None    # softmax의 출력
        self.t = None    # 정답 레이블(원-핫 인코딩 형태)
        
    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        
        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        if self.t.size == self.y.size: # 정답 레이블이 원-핫 인코딩 형태일 때
            dx = (self.y - self.t) / batch_size
        else:
            dx = self.y.copy()
            dx[np.arange(batch_size), self.t] -= 1
            dx = dx / batch_size
        
        return dx

# 소프트맥스 함수의 손실 함수로 교차 엔트로피 오차를 사용하니 역전파가 (y1-t1, y2-t2, y3-t3)로 말끔히 떨어진다 
# 사실 이런 말끔한은 우연이 아니라 교차 엔트로피 오차라는 함수가 그렇게 설계되었기 때문이다.
# 또 회귀의 출력층에서 사용하는 항등함수의 손실함수로 평균 제곱 오차를 이용하는 이유도 이와 같습니다. 
# 즉, 항등함수의 손실 함수로 평균 제곱 오차를 사용하면 역전파가 말끔히 떨어진다.

# 가령 정답 레이블이 (0, 1, 0) 일때 softmax 계층이 (0.3, 0.2, 0.5)를 출력했다고 가정
# 정답 레이블을 보면 정답의 인덱스는 1이다. 그런데 출력에서는 이때의 확률이 겨우 20%라서, 
# 이 시점의 신경망은 제대로 인식하지 못하고 있다
# 이 경우 softmax 계층이 역전파는 (0.3 -0.8 0.5)라는 커다란 오차를 전파 
# 결과적으로 softmax 계층의 앞 계층들은 그 큰 오차로부터 큰 꺠닫음을 덕게 된다 

# 정답 레이블이 (0, 1, 0) 일때 softmax 계층이 (0.01, 0.99, 0)를 출력했다고 가정 (신경망을 꽤 정확히 인식)
# softmax 계층의 역전파가 보내는 오차는 비교적 작은 (0.01 -0.01 0) 
# 앞 계층으로 전달된 오차가 작으므로 학습하는 정도는 작아진다 

# 역전파 때는 전파하는 값을 배치의 수(batch_size)로 나눠서 데이터 1개당 오차를 앞 계층으로 전파하는 점에 주의 