# 퍼셉트론 (perceptron) : 다수의 신호를 입력으로 받아 하나의 신호로 출력
# 퍼셉트론은 프랑크 로젠블라트(_Frank Rosenblatt_)가 1957년에 고안한 알고리즘입니다. 
# 신경망(딥러닝)의 기원이 되는 알고리즘 
# 퍼셉트론의 구조를 배우는 것은 신경망과 딥러닝으로 나아가는 데 중요한 아이디어를 배운다.

# 신호란 ? 전류나 강물처럼 흐름이 있는 것
#          1을 신호가 흐른다, 0을 신호가 흐르지 않는다 

# 뉴런 혹은 노드의 값인 x1, x2 의 값이 가중치를 받아 x1 + x2 가 되고 
# 뉴런에서 보내혼 신호의 종합이 정해진 한계를 넘어설 때만 1을 출력하며,
# 그 한계를 임계값이라고 한다 
# 
# 단순한 논리 회로 
# AND 게이트 : 모두가 1일때만
# NAND 게이트 : Not AND 의미 
# OR 게이트 : 신호중에 하나 이상이 1이면
# 

# 퍼셉트론으로 구현하기 

# AND 함수 (가중치와 편향을 도입)
import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2]) 
    w = np.array([0.5, 0.5]) # 가중치
    b = -0.7 # 편향 : 뉴런이 얼마나 쉽게 활성화 되는지를 결정
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = AND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))

# NAND 게이트 
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))

# OR 게이트 
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = OR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))



