#  클래스의 정의 
# 
# 객체 지향 프래그로밍 
# 크래스 기반의 객체 지향 프로그래밍 언어는 클래스라는 것을 기반으로 객체를 만들고, 
# 그러한 객체를 우선으로 생각해서 프래고르맹하는 것을 이념으로 삼고 있다 

# 객체 
# 추상화 
# - 프로그램에서 필요한 요소만을 사용해서 객체를 표현하는 것 
# - 복잡한 자료, 모듈, 시스템 등으로부터 핵심적인 개념 도는 기능을 간추려 나는 것
students = [
    { "name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 95 },
    { "name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98 },
    { "name": "구지연", "korean": 76, "math": 96, "english": 94, "science": 90 },
    { "name": "나선주", "korean": 98, "math": 92, "english": 96, "science": 92 },
    { "name": "윤아린", "korean": 95, "math": 98, "english": 98, "science": 98 },
    { "name": "윤명월", "korean": 64, "math": 88, "english": 92, "science": 92 }
]
print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] +\
        student["english"] + student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep="\t")
print("---------------------------------------------")

# 객체를 만드는 함수 (1)
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }
students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] +\
        student["english"] + student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep="\t")
print("---------------------------------------------")

# 객체를 처리하는 함수 (2)
# 딕셔너리를 리턴하는 함수를 선언합니다.
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

# 학생을 처리하는 함수를 선언합니다.
def student_get_sum(student):
    return student["korean"] + student["math"] +\
        student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student))

students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))

# 핵심 키워드 
# 객체 : 속성을 가질 수 있는 모든 것을 의미
# 객체 지향 프로그래밍 언어 : 객체를 기반으로 프로그램을 만드는 프로그래밍 언어 
# 추상화 : 복잡한 자료, 모듈, 시스템 등으로부터 핵심적인 개념 도는 기능을 간추려 나는 것 
# 클래스 : 객체를 쉽고 편리하게 생성하기 위해 만드렁진 구문
# 인스턴스 : 클래스를 기반으로 생성한 객체를 의미 
# 생성자 : 클래스 이름과 같은 인스턴스
# 메소드 : 클래스가 가진 함수 

