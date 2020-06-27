# 특수한 이름의 메소드

# 비교함수 
# 
# eq : equal (같다)
# ne : not equal (다르다)
# gt : greater than (크다)
# ge : greater than or equal (크거나 같다)
# it : less than (작다)
# le : less than or equal (작거나 같다)

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self, student):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(student),
            self.get_average(student))

    def __eq__(self, value): 
        return self.get_sum() == value.get_sum()
    def __ne__(self, value): 
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le____(self, value):
        return self.get_sum() <= value.get_sum()

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

student_a = Student("윤인성", 87, 98, 88, 95),
student_b = Student("연하진", 92, 98, 96, 98),

print("student_a == student_b = ", student_a == student_b)
print("student_a != student_b = ", student_a != student_b)
print("student_a >  student_b = ", student_a >  student_b)
print("student_a >= student_b = ", student_a >= student_b)
print("student_a <  student_b = ", student_a <  student_b)
print("student_a <= student_b = ", student_a <= student_b)
