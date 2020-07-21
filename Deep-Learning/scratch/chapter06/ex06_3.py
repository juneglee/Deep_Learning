# CNN 구현하기 
# 손글시 숫자를 인식하는 CNN을 조립

# CNN을 구성하는 계층들을 생성 
self.layers = OrderedDict()
self.layers['Conv1'] = Convolution(self.params['W1'], self.params['b1'],
                                conv_param['stride'], conv_param['pad'])
self.layers['Relu1'] = Relu()
self.layers['Pool1'] = Pooling(pool_h=2, pool_w=2, stride=2)
self.layers['Affine1'] = Affine(self.params['W2'], self.params['b2'])
self.layers['Relu2'] = Relu()
self.layers['Affine2'] = Affine(self.params['W3'], self.params['b3'])

self.last_layer = SoftmaxWithLoss()

# 순서가 있는 딕셔너리 OrderedDirt인 layers에 계층들을 차례로 추가 한다 
# 마지막 SoftmaxWithLoss계층 만큰 last_layer라는 별도 변수에 저장