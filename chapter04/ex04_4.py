# 이터레이터 
# for 반복자 in 반복할 수 있는 것
# 이터러블(iterable) : '반복할 수 있는 것'을 프로그래밍 용어 
#                    : 내부에 있는 요소들을 차례차례 꺼낼 수 있는 객체를 의미 
# 이터레이터(iterator) : 이터러블 중에서 next() 함수를 적용해 하나하나 꺼낼 수 있는 요소

# reversed() 함수와 이터레이터 
numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)
print("reversed_numbers :", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

# reversed_numbers : <list_reverseiterator object at 0x032D71A8>
# 6
# 5
# 4
# 3
# 2