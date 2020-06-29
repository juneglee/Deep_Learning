#  구문 오류와 예외 

#  오류의 종류
# 구문오류 : 실행 전 발생하는 오류 
# 예외 or 런타임 오류 : 프로그램 실행 중에 발생하는 오류 

# 기본 예외 처리 
# 조건문을 사용하는 방법
# try 구문을 사용하는 방법 

# 조건문으로 예외 처리하기 
user_input_a = input("정수 입력> ")

if user_input_a.isdigit():
    number_input_a = int(user_input_a)
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
else:
    print("정수를 입력하지 않았습니다.")

# try except 구문으로 예외를 처리
try:
    number_input_a = int(input("정수 입력> "))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except:
    print("무언가 잘못되었습니다.")

# try except 구문과 pass 키워드 조합하기 
list_input_a = ["52", "273", "32", "스파이", "103"]
list_number = []
for item in list_input_a:
    try:
        float(item) # 예외가 발생하면 알아서 다음으로 진행은 안 되겠지?
        list_number.append(item) # 예외 없이 통과했으면 리스트에 넣어줘!
    except:
        pass
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))


# try except else 구문으로 예외를 처리
try:
    number_input_a = int(input("정수 입력> "))
except:
    print("정수를 입력하지 않았습니다.")
else:
    # 출력합니다.
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)

# try except else finally 구문으로 예외를 처리
try:
    number_input_a = int(input("정수 입력> "))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")

# 정리 
# try + except 
# try + except + else 
# try + except + finally 
# try + except + else + finally 
# try + finally

# try : 예외가 발생할 가능성이 있는 코드
# except : 예외가 발생했을 때 실행할 코드 
# else : 예외가 발생하지 않았을때 실행할 코드
# finally : 무조건 실행할 코드 