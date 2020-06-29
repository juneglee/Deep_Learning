# 상속
# : 어떤 클래스를 기반으로 그 속성과 기능을 물려받아 새로운 클래스를 만드는 것
#
# 다중상속 : 다른 누군가를 만들어 놓은 형태들을 조립해서 내가 원하는 것을 만드는것ㅇ
# 부모 : 프로그래밍 언어의 기반이 되는 것
# 자식 : 부모를 기반으로 생성한 것

# 상속의 활용
class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 메서드가 호출되었습니다.")
    def test(self):
        print("Parent 클래스의 test() 메서드입니다.")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self) 
        print("Child 클래스의 __init()__ 메서드가 호출되었습니다.")

child = Child()
child.test()
print(child.value)
print("-------------------------------------")

# 사용자 정의 예외 클래스 만들기 
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self) 

raise CustomException
print("-------------------------------------")

# 자식 클래스로써 부모의 함수 재정의(오버라이드)하기 
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("##### 내가 만든 오류가 생성되었어요! #####")
    def __str__(self):
        return "오류가 발생했어요"

raise CustomException
print("-------------------------------------")

# 자식 클래스로써 부모에 없는 새로운 함수 정의하기 
class CustomException(Exception):
    def __init__(self, message, value):
        Exception.__init__(self)
        self.message = message
        self.value = value

    def __str__(self):
        return self.message

    def print(self):
        print("###### 오류 정보 ######")
        print("메시지:", self.message)
        print("값:", self.value)

try:
    raise CustomException("딱히 이유 없음", 273) # 예외 발생
except CustomException as e:
    e.print()