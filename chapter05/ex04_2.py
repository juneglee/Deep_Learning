# 함수고급 : 람다

# 함수의 매개 변수로 함수 전달하기 
# 매개변수로 받은 함수를 10번 호출하는 함수
def call_10_times(func):
    for i in range(10):
        func()
def print_hello():
    print("안녕하세요")
call_10_times(print_hello)

# filter() 함수와 map() 함수
# 함수를 매개변수로 전달하는 대표적인 표준함수 
# map(함수, 리스트)
# filter(함수, 리스트)
def power(item):
    return item * item
def under_3(item):
    return item < 3

list_input_a = [1, 2, 3, 4, 5]

# map() 함수를 사용합니다.
output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print("-----------------------------------------")
# filter() 함수를 사용합니다.
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))
print("+========================================")
# 람다
# lambda 매개변수 : 리턴값

# 람다 
power = lambda x: x * x
under_3 = lambda x: x < 3
list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print("-----------------------------------------")
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))
print("+========================================")
# 인라인 람다
list_input_a = [1, 2, 3, 4, 5]
output_a = map(lambda x: x * x, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print("-----------------------------------------")
output_b = filter(lambda x: x < 3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))
