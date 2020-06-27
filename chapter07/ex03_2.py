# 게터/세터
# 게커와 세터는 프라이빗 변수의 값을 추출하거나 변경할 목적으로,
# 간접적으로 속성에 접근하도록 해주는 함수 
# 

# 게터와 세터 
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi *  self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.__radius = value

circle = Circle(10)
print("# 원의 둘레와 넓이를 구합니다.")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())
print()

print("# __radius에 접근합니다.")
print(circle.get_radius())
print()

circle.set_radius(2)
print("# 반지름을 변경하고 원의 둘레와 넓이를 구합니다.")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

# 데코레이터를 사용한 게커와 세터 
# @property 와 @변수이름.setter
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi *  self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    @property 
    def radius(self):
        return self.__radius
    @radius.setter 
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value

print("# 데코레이터를 사용한 Getter와 Setter")
circle = Circle(10)
print("원래 원의 반지름: ", circle.radius)
circle.radius = 2
print("변경된 원의 반지름: ", circle.radius)
print()

print("# 강제로 예외를 발생시킵니다.")
circle.radius = -10
