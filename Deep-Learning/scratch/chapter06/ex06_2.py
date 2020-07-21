# CNN 구현하기 
# 손글시 숫자를 인식하는 CNN을 조립

# 가중치 매개변수를 초기화 하는 부분

self.params = {}
self.params['w1'] = weight_init+std * \
                        np.random.randn(filter_num, input_dim[0], filter_size, filter_size)
self.params['b1'] = np.zeros(filter_num)
self.params['W2'] = weight_init_std * \
                    np.random.randn(pool_output_size, hidden_size)
self.params['b2'] = np.zeros(hidden_size)
self.params['W3'] = weight_init_std * \
                    np.random.randn(hidden_size, output_size)
self.params['b3'] = np.zeros(output_size)

# 학습에 필요한 매개변수는 1번째 층의 합성곱 계층과 나머지 두 완전 연결 계층의 가중치와 편향이다 
# 이들 매개변수는 인스턴스 변수 params 딕셔너리에 저장한다 
# 1번째 층의 합성곱 계층의 가중치를 W1, 편향을 b1 이라는 키로 저장
# 마찬가지로 2번째, 3번째 층의 완전 연결 계층 2,3으로 저장한다 

