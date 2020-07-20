# 적절한 하이퍼파라미터 값 찾기 
# 하이퍼 파라미터 = 각층의 뉴런 수, 배치 크기, 매개변수 갱신 시의 학습률과 가중치 감소 

# 같은 성능 평가인데 하이퍼 파라미터가 대상일 대는 시험 데이터를 사용해서는 아노디는 이유?
# 그것은 시험 데이터를 사용하여 하이퍼 파라미터를 조정하면 하이퍼 파라미터 값이 시험 데이터에 오버피팅 되기 때문
# 그래서 하이퍼 파라미터를 조정할 때는 하이퍼파라미터 전용 확인 데이터가 필요
# 하이퍼파라미터 조정용 데이터를 일반적으로 검증 데이터 validation data라 부른다 

# 훈련 데이터 : 매개변수 학습
# 검증 데이터 : 하이퍼파라미터 성능 평가
# 시험 데이터 : 신경망의 범용 선능 평가

# MINIST 데이터셋에서 검증 데이터를 얻는 가장 간단한 방법은 훈련 데이터 중 20% 정도를 검증 데이터로 분리하는 것

(x_train, t_train), (x_test, t_test) = load_mnist()

# 훈련데이터를 뒤섞는다 
x_train, t_train = shuffle_dataset(x_train, x_train)

# 20%를 검증 데이터로 분할
validation_rate=0.20
validation_num = ini(x.shape[0] * validation_rate)

x_val = x_train[:validation_num]
t_val = t_train[:validation_num]
x_train = x_train[validation_num:]
t_train = t_train[validation_num:]

