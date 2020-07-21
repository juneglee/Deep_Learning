# im2col로 데이터 전개하기
# im2col은 image to column, 즉 이미지에서 행렬로 라는 뜻이다.  
# 합성곱 계층과 풀링 계층은 복잡해 보이지만, 사실 트릭(im2col)을 사용하면 쉽게 구한다

# 합성곱 연산을 곧이곧대로 구현하면 for문을 겹겹이 써야하지만, 
# for 문 대신 im2col이라는 ㅕㄴ의 함수를 사용해 간단하게 구현이 가능하다 

# im2col은 입력데이터를 필터링(가중치 계산)하기 좋게 전개하는(펼치는) 함수이다 
# 3차원 입력 데이터에 1m2col을 적용하면 2차원 행렬로 바뀐다 
# 정확히는 배치 안의 데이터 수까지 포함한 4차원 데이터를 2차원으로 변환
# 즉, 입력데이터에서 필터를 적용하는 영역(3차원 블록)을 한줄로 늘어 놓는다 

# 필터 적용 영역에 겹치게 되면 im2col로 전개한 후의 원소 수가 원래 블록의 원 수 보다 많아진다 
# 그래서 im2col을 사용해 구현하면 메모리를 더 많이 소비하는 단점이 있지만, 컴퓨터는 큰 행렬을 묶어서 계산하는데 탁월하다

# im2col 함수의 인터페이스 
# im2col(input_data, filter_h, filter_w, stride =1, pad = 0)
# input_data - (데이터수, 채널 수, 높이, 너비) 의 4차원 배열로 이뤄진 입력 데이터 
# filter_h - 필터의 높이 
# filter_w - 필터의 너비
# stride - 스트라이트
# pad - 패딩
 
import sys, os
sys.path.append(os.pardir)
from common.util import im2col
import numpy as np

x1 = np.random.rand(1, 3, 7, 7) # (데이터 수, 채널 수, 높이, 너비)
col1 = im2col(x1, 5, 5, stride=1, pad=0)
print(col1.shape) # (9, 75)

x2 = np.random.rand(10, 3, 7, 7)
col2 = im2col(x2, 5, 5, stride=1, pad=0)
print(col2.shape) # (90, 75)

