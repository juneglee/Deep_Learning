# 플레이스 홀더 (Placeholder)
# : 임의의 값을 입력받아서 읨의 값을 출력, 이때 사용하는 텐서플로 API가 플레이스 홀더와 변수 이다 

# 플레이스홀더 노드(tf.placeholder)는 그패르에서 임의의 입력값을 받을 수 있도록 만들어준다 

# tf.placeholder(dtype, shape=None, name=None)
# tf.placeholder는 feed_dict를 통해 임의의 값을 입력 받을 수 있도록 만든다 
# dtype : feed할 데이터 타입 (e.g. tf.float32, tf.int32, tf.bool)
# shape : feed할 데이터의 형태, None은 임의의 차원이 될 수 이쓴ㄴ 특수 키워드 (e.g. [None, 784] None 부분은 임의의 차원이 지정될 수 있다)
# name : 연산의 이름(optional)

import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b # 암시적으로 tf.add(a, b) 형태로 정의될 것이다 

print(adder_node, feed_dict={a : 3, b : 4.5})
