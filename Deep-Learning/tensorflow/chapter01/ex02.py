# 텐서보드 (TensorBoard)
# : 시각화 툴을 이용해서 그래프 구조를 시각화해 볼수 있다 


# tensorFlow API 알아보기 
# tf.constant(value, dtype = None, shape = None, name = 'Const')
# tf.constant는 상수 텐서를 선언한다 
# value : 상수값이며, 직접 지정하거나 shape 형태로 채울 값을 지정할 수 있다 
# dtype : 데이터 타입 (e.g. tf.float32, tf.int32, tf.bool)
# shape : 상수 데이터의 형태 
# name : 텐서의 이름(optional)

# shape 형태 
import tensorflow as tf
# 상수값을 직접 지정
tensor1 = tf.constant([1, 2, 3, 4, 5, 6, 7])
tf.print(tensor1) # [1 2 3 ... 5 6 7]
# shape에 정의된 형태로 값을 채움
tensor2 = tf.constant(-0.1, shape=[2, 3])
tf.print(tensor2) # [[-0.1 -0.1 -0.1]
                  #  [-0.1 -0.1 -0.1]]