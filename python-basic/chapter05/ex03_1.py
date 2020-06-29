# 재귀함수 

# 반복문으로 팩토리얼 구하기 
def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output
print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))

# 재귀 함수로 팩토리얼 구하기 
def factorial(n):
    # n이 0이라면 1을 리턴
    if n == 0:
        return 1
    # n이 0이 아니라면 n * (n-1)!을 리턴
    else:
        return n * factorial(n - 1)
print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))

