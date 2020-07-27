# 텐서플로 기초와 텐서보드
# 텐서플로(tensorflow) 는 이름에서 알 수 있듯이 텐서(tensor)를 흘려보내면서(flow) 데이터를 처리하는 라이브러리이다
# 역서 텐서는 다차원 배열을 의미한다 

# 랭크(Rank)는 텐서의 차원(Dimension)을 의미한다 
# 만약 랭크가 0이라면 스칼라, 1이라면 벡터, 2라면 행렬, 3이상이면 텐서라고 부른다 

# 이런 텐서들을 계산 그래프 구조 (Computational Graph)를 통해 노드에서 노드로 이동한다 
# 그래프 생성단계에서는 연산 과정을 그래프 형태로 표현하게 된다 
# 공학에서 정의하는 그래프는 노드(node)와 엣지(edge)로 이루어진 자료 구조이다 

# 텐서프롤는 노드에 연산(operator), 변수 (valiable), 상수 (constant) 등을 정의하고, 
# 노드 간의 연결인 엣지를 통해 텐서를 주고 받으면서 계산을 한다
# 

# 상수(constant) 값을 표현하는 tf.constant 노드를 2개 정의하고 출력
import tensorflow as tf 

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # 암시적으로 tf.float32 타입으로 선언될 것이다.
print(node1, node2)
# tf.Tensor(3.0, shape=(), dtype=float32) tf.Tensor(4.0, shape=(), dtype=float32)

# 텐서플로에서는 상수 선언은 그래프의 노드 형태를 정의한 것일 뿐이므로 실제 결과값을 출력하려면 정의한 그래프를 실행시켜줘야 한다
# 다시 말하면, 우리는 아직 그래프 생성 단계까지만 수행했기 때문에 다음 단계로 그래프 상에 실제 텐서값들을 흘려보내주기 위해서 
# 그래프 실행 단계를 수행해야 한다 
# 텐서플로에서 그래프 실행은 세션(session)을 열어서 수행해야 한다 

# tensorflow의 버전 1.xxx에서는 session에 저정하여 run으로 실행해야 한다 
# 하지만 버전 2.xxx에서는 session을 사용하지 않고 바로 print을 통해서 결과를 출력 할 수 있다 
'''
sess = tf.Session()
print(sess.run([node1, node2]))
'''
tf.print(node1, node2) # 3 4

# 더 복잡한 그래프 구조를 생성하면 더 복잡한 연산을 수행 
node3 = tf.add(node1, node2)
print("node3(정보 값) : ", node3) # node3(정보 값) :  tf.Tensor(7.0, shape=(), dtype=float32)
tf.print("node3 : ", node3) # node3 :  7