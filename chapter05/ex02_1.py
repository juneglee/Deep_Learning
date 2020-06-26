# 함수에 매개변수 만들기 
#
# 사용법
# def 함수이름(매개변수, 매개변수, ...):
#     문장 
#
# 매개변수의 기본 
def print_n_times(value, n):
    for i in range(n):
        print(value)
print_n_times("안녕하세요", 5)
print("-------------------------------------")

# 가변 매개변수 
# print() 함수와 같이 매개변수를 원하는 만큼 받을 수 있는 함수
# 
# 사용법 
# def 함수이름(매개변수, 매개변수, ..., *가변 매개변수 ):
#     문장 
# 
def print_n_times(n, *values):     # n번 반복합니다.
    for i in range(n):             # values는 리스트처럼 활용합니다.
        for value in values:
            print(value)           # 단순한 줄바꿈
        print()
print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")
print("-------------------------------------")

# 기본 매개변수 
# 매개변수를 입력하지 않았을 경우 매개변수에 들어가는 기본값
def print_n_times(value, n=2):
    for i in range(n):
        print(value)
print_n_times("안녕하세요")


