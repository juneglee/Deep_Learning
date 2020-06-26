#  함수 고급

# 튜플 : 함수와 함께 많이 사용되는 리스트와 비슷한 자료형으로, 
#        리스트와 다른점은 한번 결정되면 요소를 바꿀 수 없다는 것
# 람다 : 매개 변수로 함수를 전달하기 위해 함수 구문을 작성하는 것이 번거롭고, 
#        코드 공간 낭비라는 생각이 들때 함수를 간단하고 쉽게 선언하는 방법

# 튜플 
# (데이터, 데이터, 데이터)

# 리스트와 튜플의 특이한 사용
[a, b] = [10, 20]
(c, d) = (10, 20)
print("a:", a) # a: 10
print("b:", b) # b: 20
print("c:", c) # c: 10
print("d:", d) # d: 20

# 괄호가 없는 튜플 
tuple_test = 10, 20, 30, 40
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test:", tuple_test) # tuple_test: (10, 20, 30, 40)
print("type(tuple_test):", type(tuple_test)) # type(tuple_test): <class 'tuple'>
print("-----------------------------")
a, b, c = 10, 20, 30
print("# 괄호가 없는 튜플을 활용한 할당")
print("a:", a) # a: 10
print("b:", b) # b: 20
print("c:", c) # c: 30

# 변수의 값을 교환하는 튜플
a, b = 10, 20
print("# 교환 전 값")
print("a:", a)
print("b:", b)
print("-----------------------------")
a, b = b, a
print("# 교환 후 값")
print("a:", a)
print("b:", b)
print("-----------------------------")

# 여러 개 값 리턴하기 
def test():
    return (10, 20)
a, b = test()
print("a:", a)
print("b:", b)