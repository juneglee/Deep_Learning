# 괄호로 문자열 연결하기 

# 괄호로 문자열 연결하기 
test = (
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어 "
    "생성됩니다."
)
# 쉼표가 없어서 하나의 문자열로 연결되어 생성된다.
print("test:", test)
print("type(test):", type(test))
# test: 이렇게 입력해도 하나의 문자열로 연결되어 생성됩니다.
# type(test): <class 'str'>
print("----------------------------------")

# 여러 줄 문자열과if 구문을 조합했을 때 문제 해결 (1)
# 줄바꿈을 하기 위해서는 마지막을 제외한 문자열 뒤에 \n을 입력한다 
number = int(input("정수 입력> "))
if number % 2 == 0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 짝수입니다."
    ).format(number, number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 홀수입니다."
    ).format(number, number))

# 문자열의 join() 함수 
# 사용법 : 문자열.join(문자열로 구성된 리스트)
print("::".join(["1","2","3","4","5"])) # 1::2::3::4::5

# 여러 줄 문자열과if 구문을 조합했을 때 문제 해결 (2)
if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 짝수입니다."
    ]).format(number, number))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 홀수입니다."
    ]).format(number, number))
