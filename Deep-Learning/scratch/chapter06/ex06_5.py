# CNN 구현하기 
# 손글시 숫자를 인식하는 CNN을 조립

# 오차 역전파법으로 기울기를 구하는 구현
def gradient(self, x, t):
    # forward : 순전파
    self.loss(x, t)

    # backward : 역전파
    dout = 1
    dout = self.last_layer.backward(dout)

    layers = list(self.layers.values())
    layers.reverse()
    for layer in layers:
        dout = layer.backward(dout)

    # 결과 저장
    grads = {}
    grads['W1'], grads['b1'] = self.layers['Conv1'].dW, self.layers['Conv1'].db
    grads['W2'], grads['b2'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
    grads['W3'], grads['b3'] = self.layers['Affine2'].dW, self.layers['Affine2'].db

    return grads

# 매개변수의 기울기는 오차 역전파법으로 구한다 (순전파와 역전파를 반복)
# 마지막으로 grads 라는 딕셔너리 변수에 각 가중치 매개 변수의 기울기를 저장 