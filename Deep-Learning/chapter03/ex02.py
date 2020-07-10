# 오차 역전파(back propagation)
# : 다층 퍼셉트론에서의 최적화 과정 
# 가중치에서 기울기를 빼도 값의 변화가 없을 때까지 계속해서 가중치 수정 작업을 반복하는 것 

# 1. 환경 변수 지정 : 환경 변수에는 입력 값과 타깃 결과값이 포함돈 데이터 셋, 학습률 등이 포함된다. 
#                     활성화 함수와 가중치 등도 선언
# 2. 신경망 실행    : 초기값을 입력하여 활성화 함수와 가중치를 거쳐 결과값이 나온다 
# 3. 결과를 실제 값과 비교 : 오차를 측정 
# 5. 결과 출력

# 반복 횟수 지정
# 4. 출력층 가중치 수정 , 은닉층 가중치 수정
# 2. 신경망 실행
# 3. 결과를 실제 값과 비교 

# 다층 퍼셉트론이 오차 역전파를 만나 신경망이 되고, 신경망은 xor 문제를 가볍게 해결하지만, 
# 문제점이 생긴다 
# 기울기 소실 (vanishing gradient) : 층이 늘어나면서 역전파를 통해 전달되는 이 기울기의 값이 점점 작아져 맨 처음층까지 전달되지 않는 문제
#                                    이는 활성화 함수로 사용된 시그모이드 함수의 특성 때문이다 

# 이를 해결하기 위해서 다른 여러 함수로 대체한다.
# 시그모이드 함수 
# 하이퍼블릭 탄젠트 함수 
# 렐루 함수 
# 소프트플러스 함수 

# 속도와 정확도 문제를 해결하는 고급 경사 하강법
# 고급 경사 하강법 : 가중치를 업데히는 방법으로 경사 하강법이지만, 
# 한 번 업데이트를 할려면 전체 데이터를 미분해야 하므로 계산량이 매우 많다는 단점이 있다 
#  
# 확률적 경사 하강법 (Stochastic Gradient Descent: SGD)
# : 전체 데이터를 사용하여 계산하는 것이 아니라, 램던하게 추출한 일부 데이터를 사용한다 
# 모멘텀 (momentum)
# : 관성, 탄력, 가속도 
# 오차를 수정하기 전에 바로 앞 수정 값과 방향(+, -)을 참고하여 같은 방향으로 일정한 비율만 수정되게 하는 방법 

# 이외의 방법 
# 네스테로프 모멘텀 (NAG)
# 아다그라드 (Adagrad)
# 알엠에스프롭 (RMSprop)
# 아담(Adam)