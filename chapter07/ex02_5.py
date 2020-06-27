# 클래스 변수와 메소드

# 클래스 함수 
# 사용
# class 클래스 이름:
#     @classmethod
#     클래스 변수 = 값
# 접근
# 클래스 이름.변수 이름(매개변수 )
#
# @classmethod : 데코레이터 
# @로 시작하는 것을 파이썬에서는 데코레이터라고 하며 "꾸며주는 것"이라는 의미를 가진다 
# 함수 데코레이터와 클래스 데코레이터로 나뉜다.

class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("------ 학생 목록 ------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------- ------- -------")

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 76, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤아린", 95, 98, 98, 98)
Student("윤명월", 64, 88, 92, 92)
Student("김미화", 82, 86, 98, 88)
Student("김연화", 88, 74, 78, 92)
Student("박아현", 97, 92, 88, 95)
Student("서준서", 45, 52, 72, 78)

Student.print()

