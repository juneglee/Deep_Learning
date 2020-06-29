#  예외 고급 

# 예외 객체 
# try: 
#    예외가 발생할 가능성이 있는 구문
# except 예외의 종류 as 예외 객체를 활용할 변수 이름: 
#    예외가 발생했을 때 실행할 구문 

# 예외 객체 
try:
    number_input_a = int(input("정수 입력> "))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception) # Exception은 부모클래스 

# 예외 구분하기 
# 여러가지 예외가 발생할 수 있는 코드 
# 에러 1 : 정수로 변환될수 없는 값을 입력 ex) "yes!!"
# 에러 2 : 리스트의 길이를 넘는 인덱스를 입력한 경우 ex) 100 
list_number = [52, 273, 32, 72, 100]
try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)

# 예외 구분하기 
# try: 
#    예외가 발생할 가능성이 있는 구문
# except 예외의 종류 A: 
#    예외A가 발생했을 때 실행할 구문 
# except 예외의 종류 B: 
#    예외B가 발생했을 때 실행할 구문 
# except 예외의 종류 C: 
#    예외C가 발생했을 때 실행할 구문 
list_number = [52, 273, 32, 72, 100]
try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    # ValueError가 발생하는 경우
    print("정수를 입력해 주세요!")
except IndexError:
    # IndexError가 발생하는 경우
    print("리스트의 인덱스를 벗어났어요!")

# 예외 구분 구문과 예외 객체 
# as 키워드를 사용하여 추가 
list_number = [52, 273, 32, 72, 100]
try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError as exception:
    print("정수를 입력해 주세요!")
    print("exception:", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print("exception:", exception)