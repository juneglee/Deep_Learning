# CNN 구현하기 
# 손글시 숫자를 인식하는 CNN을 조립

# CNN 네트워크는 Convolution - ReUL- Pooling - Affine - ReLU - Affine - softmax 순으로 흐른다 

# 초기화 때 받는 인수 
# input_dim - 입력 데이터 (채널 수, 높이, 너비)의 차원
# conv_param - 합성곱 계층의 하이퍼파라미터(딕셔너리), 딕셔너리의 키는 다음과 같다 
#  - filter_num - 필터 수
#  - filter_size - 필터 크기 
#  - stride - 스트라이트
#  - pad - 패팅
# hidden_size - 은닉층(완전연결)의 뉴런수 
# output_size - 출력층(완전연결)의 뉴런수
# weight_init_std - 초기화 떄의 가중치 표준편차
# 여기서 합성곱 계층의 하이퍼파라미터는 딕셔너리 형태로 주어진다 (conv_param)
# 이것은 필요한 하이퍼파라미터의 값이 예컨대 {'filter_num':30, 'filter_size':5, 'pad':0, 'stride':1}처럼 저장

class SimpleConvNet:
    def __init__(self, input_dim= (1, 28, 28), conv_param = {'filter_num':30, 'filter_size':5, 'pad':0, 'stride':1},
                hidden_size=100, output_size=10, weight_init_std=0.01):
        filter_num =conv_param['filter_num']
        filter_size =conv_param['filter_size']
        filter_pad =conv_param['pad']
        filter_stride =conv_param['stride']

        input_size = input_dim[1]
        conv_output_size = (input_size - filter_size + 2*filter_pad) /\
            filter_stride + 1
        pool_output_size = int(filter_num * (conv_output_size/2) * (conv_output_size/20))

        # 초기화 인수로 주어진 합성곱 계층의 하이퍼 파라미터를 딕셔너리에서 꺼냅니다 (나중에 쓰기 쉽도록)
        # 그리고 합성곱 계층의 출력 크기를 계산 
