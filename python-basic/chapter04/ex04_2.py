# 구문 내부에 여러 줄 문자열을 사용했을 때의 문제점

# if 조건문 과 여러줄 문자열 (1)
# 예상치 못 한 들여쓰기 (indent)가 들어간다 
number = int(input("정수 입력> "))
if number % 2 == 0:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 짝수입니다.""".format(number, number))
else:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 홀수입니다.""".format(number, number))
print("----------------------------------------")

# if 조건문 과 여러줄 문자열 (2)
if number % 2 == 0:
    print("""입력한 문자열은 {}입니다.
{}는(은) 짝수입니다.""".format(number, number))
else:
    print("""입력한 문자열은 {}입니다.
{}는(은) 홀수입니다.""".format(number, number))
print("----------------------------------------")

# if 조건문 과 긴 문자열
if number % 2 == 0:
    print("입력한 문자열은 {}입니다.\n{}는(은) 짝수입니다.".format(number, number))
else:
    print("입력한 문자열은 {}입니다.\n{}는(은) 홀수입니다.".format(number, number))


