# 숫자와 문자열의 다양한 기능 
 
# 대소문자 바꾸기 : upper()와 lower()
a = "Hello Python Programing"
print(a.upper()) # HELLO PYTHON PROGRAMING
print(a.lower()) # hello python programing

# 문자열 양평의 공백 제거 : Strip()
b = """
    안녕하세요 
공백 제거 합니다
"""
print(b.strip())

# 문자열의 구성 파악하기: isOO()
# isalnum() : 문자열이 알파벳 또는 숫자로만 구성되어 있는지 확인
# isalpha() : 문자열이 알파벳으로로 구성되어 있는지 확인
# isidentifier() : 문자열이 식별자로 구성되어 있는지 확인
# isdecimal() : 문자열이 정수로 구성되어 있는지 확인
# isdigit() : 문자열이 숫자로 구성되어 있는지 확인
# isspace() : 문자열이 공백으로 구성되어 있는지 확인
# islower () : 문자열이 소문자로 구성되어 있는지 확인 
# isuppser() : 문자열이 대문자로 구성되어 있는지 확인
print("trainA10".isalnum()) # True
print("10".isdigit()) # True

# 문자열 찾기 : find()와 rfind()
# find() : 왼쪽에서 찾아서 처음 등장하는 위치를 찾습니다.
# rfind() : 오른쪽부터 찾아서 처음 등장하는 위치를 찾습니다.
c = "안녕하세요".find("안녕") 
print(c) # 0 #문자열은 0번째부터 시작하기 때문에 안녕은 0번쨰 위치로 찾은 것이다

d = "안녕안녕하세요".rfind("안녕")
print(d) # 2 #오른쪽에서부터 찾았기 때문에 0 1 2인 2번째 인것이다

# 문자열과 in 연산자 
# : 문자열 내부에 어떤 문자열이 있는지 확인하려면 in 연산자를 사용한다
print("안녕" in "안녕하세요") # True
print("메롱" in "안녕하세요") # False

# 문자열 자르기 : split() 
e = "10 20 30 40 50".split()
print(e) # ['10', '20', '30', '40', '50'] # 실행결과로 리스트(list)가 나옴






 