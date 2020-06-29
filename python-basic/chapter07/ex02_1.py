# 클래스의 추가적인 구문
#
# 어떤 클래스의 인스턴스인지 확인하기 
#
# isinstance(인스턴스, 클래스) 확인 
# isinstance(student, Student) : true
# 단순 인스턴스 확인
# type(student) == Student

# 이때 isinstance() 함수는 상속관계까지 확인하고, 
# 반면 type() 함수는 상속관계를 확인하지 않는다 

class Student:
    def study(self):
        print("공부를 합니다.")
class Teacher:
    def teach(self):
        print("학생을 가르칩니다.")

classroom = [Student(), Student(), Teacher(), Student(), Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()
 