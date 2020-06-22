# if~else 와 elif

# if ~ else
# if 조건문에 else 구문을 추가해서 짝수와 홀수 구분
number = input("정수 입력> ")
number = int(number)

if number % 2 == 0:
    # 조건이 참일 때, 즉 짝수 조건
    print("짝수입니다")
else:
    # 조건이 거짓일 때, 즉 홀수 조건
    print("홀수입니다")
 