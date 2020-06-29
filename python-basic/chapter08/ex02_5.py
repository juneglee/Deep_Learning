# 함수 데코레이터 
# 데코레이터를 사용하면 functools라는 모듈을 사용할 수 있고,
# 함수 데코레이터를 사용할 때 매개 변수 등을 전달 수 있어 반복되는 구문이 많아질때 
# 소스의 가독성도 높이고 매우 유용하게 사용할 수 있다 .

# 함수 데코레이터 
def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper

# 데코레이터를 붙여 함수를 만듭니다.
@test
def hello():
    print("hello")

# 함수를 호출합니다.
hello()

