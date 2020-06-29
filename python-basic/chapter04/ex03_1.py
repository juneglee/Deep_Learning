#  반복문과 while 반복문

# 범위 range 자료형
# 첫째, 매개변수에 숫자를 한개 넣는 방법
# range(A)
# 둘째, 매개변수에 숫자를 두개 넣는 방법
# range(A , B)
# 둘째, 매개변수에 숫자를 세개 넣는 방법
# range(A , B , C)

a = range(5)
b = range(0, 5) 
c = range(0 , 10 , 2) # 0부터 2씩 증가사면서 (10-1)까지 정수로 범위를 만듬

print(a) # range(0, 5)
print(list(a)) # [0, 1, 2, 3, 4]

print(b) # range(0, 5)
print(list(b)) # [0, 1, 2, 3, 4]

print(c) # range(0, 10, 2)
print(list(c)) # [0, 2, 4, 6, 8]

# 매개변수로 사용
n =10
d = range(0 , int(n/2)) # 실수를 정수로 바꾸는 방법
e = range(0 , n // 2) # 정수 나누기 연산자를 많이 사용

print(list(d)) # [0, 1, 2, 3, 4]
print(list(e)) # [0, 1, 2, 3, 4]

# for 키 변수 in 범위:
#     코드 
for i in range(5):
    print(str(i) + "= 반복 변수")
print()

for i in range(5, 10):
    print(str(i) + "= 반복 변수")
print()

for i in range(0, 10, 3):
    print(str(i) + "= 반복 변수")
print()
