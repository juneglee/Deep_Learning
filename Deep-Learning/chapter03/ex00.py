# 인공 신경망 (Artificial Neural Network)
# : 뉴런과 뉴런이 서로 새로운 연결을 만들기도 하고 필요에 따라 위치를 바꾸는 것처럼, 
# 여러 층의 퍼셉트론을 서로 연결시키고 복잡하게 조합하여 주어진 입력 값에 대한 판단을 하게 하는 것

# 신경망을 이루는 가장 중요한 기본 단위는 퍼셉트론(perceptron)
# 퍼셉트론은 입력 값과 활성화 함수를 사용해 출력 값을 다음으로 넘기는 가장 작은 신경망 

# y = wx + b
# 여기서, w를 가중치, b는 바이어스 
# 이때 0과 1을 판단하는 함수를 활성화 함수(activation function)이라고 하며,
#  시그모이드 함수가 대표적인 활성화 함수 이다 

# 다층 퍼셉트론
# 다층 퍼셉트론이 입력층과 출력 사이에 숨어 있는 은닉층을 만드는 것으로 나타낼 수 있다 
# 은닉층에 모이는 중간 정거장을 노드(node)라고 한다 

# 순방향 신경망(Feed-Forward Neural Network, FFNN)
# 다층 퍼셉트론(MLP)과 같이 입력층에서 출력층 방향으로 연산이 전개되는 신경망을 
# 피드 포워드 신경망(Feed-Forward Neural Network, FFNN)이라고 합니다.

# 순환 신경망 (Recurrent Neural Network, RNN)
# 신경망은 은닉층의 출력값을 출력층으로도 값을 보내지만, 
# 동시에 은닉층의 출력값이 다시 은닉층의 입력으로 사용되는데 이는 FFNN의 정의에 벗어납니다.


