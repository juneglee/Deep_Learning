# 끝자리로 짝수와 홀수 구분하기 
number = input("정수 입력> ")

last_character = number[-1] #마지막 자리 숫자를 추출
last_number = int(last_character) # 숫자로 변환하기 

print("---------------------------------------")
# 짝수 확인
if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8:
    print("짝수 입니다")
# 홀수 확인
if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9:
    print("홀수 입니다")
print("---------------------------------------")

# in 문자열 연산자를 활용해서 짝수와 홀수 구분
if last_character in "02468":
    print("짝수 입니다")
if last_character in "13579":
    print("홀수 입니다")

print("---------------------------------------")
# 나머지 연산자를 활용해서 짝수와 홀수 구분
number = int(number)
if number % 2 == 0:
    print("짝수 입니다")
if number % 2 == 1:
    print("홀수 입니다")