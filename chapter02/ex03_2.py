# 변수와 입력

# 사용자 입력 : input()
String = input("인사말을 입력하세요> ")
print(String)

# input() 함수의 입력 자료형
number = input("숫자를 입력하세요> ")
print(number) # 12345
print(type(number)) # 결과값 :  Str 
# 무엇을 입력하여도 무조건 문자열 자료형이다.

# 문자열 숫자로 바꾸기 
String_a = input("입력A > ")
int_a = int(String_a)
int_fa = float(String_a)

String_b = input("입력B > ")
int_b = int(String_b)
int_fb = float(String_b)

# 예제 A : 123 B : 45
print("문자열 자료 : ", String_a + String_b) # 12345
print("숫자 자료 :" , int_a + int_b) # 168
print("float 자료 :" , int_fa + int_fb) # 168.0

# ValueError  예외 
# 1. 숫자가 아닌 것을 숫자로 변환하려고 할때 
# int("안녕하세요")
# 2. 소수점이 있는 숫자 형식을 문자열 int() 함수로 변환하려고 할때 
# int("52.273")

#숫자로 문자열 바꾸기 : str
output_a = str(52)
output_b = str(52.273)
print(type(output_a), output_a)
print(type(output_b), output_b)
