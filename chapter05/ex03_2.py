# 피보나치 수열

# n번째 수열 = (n-1) 번째 수열 + (n-2) 번째 수열 

# 재귀 함수로 구현한 피보나치 수열(1)
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print("fibonacci(1):", fibonacci(1))
print("fibonacci(2):", fibonacci(2))
print("fibonacci(3):", fibonacci(3))
print("fibonacci(4):", fibonacci(4))
print("fibonacci(5):", fibonacci(5))
print("-------------------------------------")

# 재귀 함수로 구현한 피보나치 수열(2)
counter = 0
def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter # global 변수이름 : 함수의 외부의 변수를 참조하기 위해서 사용
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci(10)
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))
# 트리 형태에서 각각의 지점을 노드, 노드 중에 가장 마지막 단계의 노드를 리프라고 부른다 
print("-------------------------------------")

# 메모화 
# 딕셔너리를 사용해서 한번 계산한 값을 지정하는 것을 메모라고 하며, 
# 메모화를 사용하면 실행 후 곧바로 결과를 출력할 정도로 속도가 빨라진다 .
dictionary = {
    1: 1,
    2: 2
}
def fibonacci(n):
    if n in dictionary:
        # 메모 되어 있으면 메모된 값 리턴
        return dictionary[n]
    else:
        # 메모 되어 있지 않으면 값을 구함
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output
print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))

