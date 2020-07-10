# 퍼셉트론

# XOR 게이트 
# 베타적 논리합이라는 논리 회로 ('베타적'이란 자기 외에는 거부한다는 의미)
# x1과 x2 중에 한쪽이 1일 때만 1을 출력 
#
# 퍼센트론으로는 XOR 게이트를 표현할 수 없어, '다층 퍼셉트론'으로 만든다 
# 즉, AND, NAND, OR를 사용하여 쉽게 구현할 수 있다.
from ex01 import AND
from ex01 import OR
from ex01 import NAND

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))