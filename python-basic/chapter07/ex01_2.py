#  클래스 선언
# 
# 클래스 & 인스턴스 
# 사용법 : 클래스 
# class 클래스 이름:
#      클래스 내용 
# 사용법 : 인스턴스 
# 인스턴스 이름(변수 이름) = 클래스 이름() # 생성자 함수라고 부른다 
# class Student: # 클래스 선언
#    psss

# student = Student() # 학생을 선언

# students =[ # 학생 리스트 선언
#    Student(),
#    Student(),
#    Student(),
#    Student(),
#    Student(),
#    Student()
# ]

# 생성자 
# class 클래스 이름:
#    def __init__(self, 추가적인 매개변수):
#       pass
# 여기서 self 는 자기 자신을 나타내는 딕셔너리
# 접근할 때는 self.<식별자> 형태로 접근 
#  
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print(students[0].name)
print(students[1].name)
print(students[2].name)
print(students[3].name)
print(students[4].name)
print(students[5].name)

# 소멸자 
# 생성자와 반대로 인스턴스가 소멸될 때 호출되는 함수 
#  def __del__