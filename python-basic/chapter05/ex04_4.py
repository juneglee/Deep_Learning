# 제너레이터 
# 이터레이터를 직접 만들 때 사용하는 코드로써, 함수 내부에 yield 키워드를 사용하면 
# 해당 함수는 제너레이터 함수가 되며,
# 일반 함수와 달리 함수를 호출해도 함수 내부의 코드가 실행되지 않는다 
# 제너레이터 객체는 next() 함수를 사용해 함수 내부의 코드를 실행하여야 한다 

# 제너레이터 함수 
def test():
    print("함수가 호출되었습니다.")
    yield test

print("A 지점 통과")
test()

print("B 지점 통과")
test()
print(test())

# 제너레이터 객체와 next() 함수 
# next() 함수를 호출한 이후 yield 키워드를 만나지 못하고 함수가 끝나면 
# StopIteration이라는 예외가 발생한다 
def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")
output = test()

print("D 지점 통과")
a = next(output)
print(a)
	
print("E 지점 통과")
b = next(output)
print(b)

print("F 지점 통과")
c = next(output)
print(c)

next(output)
