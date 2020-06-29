# 표준 모듈
# 
# 표준 모듈 : 파이썬에 기본적으로 내장되어 있는 모듈
# 외부 모듈 : 다른 사람들이 만들어 공개한 모듈
# import

# import math 
# 수학과 관련된 기능 
# math.sin()
# math.cos()
# math.tan()
# math.log(x.[base]
# math.ceil() - 올림
# math.floor() - 내림
# math.round() - 반올림, 단 홀수인 것들은 올림이 되고, 짝수는 내림이 된다.
import math 
print(math.sin(1))
print("------------------------------------------")

# from 구문 
# from 모듈 이름 import 가져오고 싶은 변수 또는 함수 
# from math import sin, cos, tan, floor, ceil
# from math import * (모두 가져오기)
from math import sin, cos, tan, floor, ceil
print(math.sin(1))
print("------------------------------------------")

# as 구문 
# 모듈을 가져올때 이름 출동을 방지하기 위해서 사용
import math as m
print(m.sin(1))
print("------------------------------------------")

