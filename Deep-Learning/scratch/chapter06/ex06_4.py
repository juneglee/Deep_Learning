# CNN 구현하기 
# 손글시 숫자를 인식하는 CNN을 조립

# SimpleConvNet의 초기화를 하고, 초기화를 마친 다음에는 추론을 수행하는 
# predict 메서드와 손실함수의 값을 구하는 loss ㅁ서드를 다음과 같이 구현할 수 있다 

def predict(self, x):
    for layer in self.layers.values():
        x = layer.forward(x)
        return x

def loss(self, x, t):
    y = self.predict(x)
    return self.last_layer.forward(y, t)

# x는 입력 데이터, t는 정답 레이블 
# 추론을 수행하는 predict 메서드는 초기화 때 layers에 추가한 맨 앞에서부터 차례로 forward메서드를 호출하며 그 결과를 다음 계층에 전달
# 손실 함수를 구하는 loss 메서드는 predict 메서드의 결과를 인수로 마지막 층의 forward메서드를 호출
# 첫 계층부터 마지막 계층까지 forward를 처리