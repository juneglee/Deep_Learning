#  raise 구문
# 프로그램 강제 종료되는 것을 막기 위해 예외 처리를 해야하며, 
# 아직 구현되지 않는 부분이므로 일부러 예외를 발생시켜 
# 프로그램을 죽게 만들어 잊어버리지 않도록 하는 것이 raise 키워드 이다 
#
# 사용법 
# raise 예외객체 
number = input("정수 입력> ")
number = int(number)

if number > 0:
    print("양수입니다 !")
    raise NotImplementedError
else:
    print("음수입니다 !")
    raise NotImplementedError