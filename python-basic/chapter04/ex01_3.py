# 리스트 요소 추가하기 : append, insert, extend
# 사용법 
# 리스트명.append(요소)
# 리스트명.insert(위치,요소) = (삽입할 위치, 삽입할 값)

list_a = [1, 2, 3]
list_b = [1, 2, 3]

# 리스트 뒤에 요소 추가하기
print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a) # [1, 2, 3, 4, 5]
print("------------------")

# 한번에 여러 요소를 추가하고 싶을 때는 extend()
list_b.extend([4, 5, 6]) 
print(list_b) # [1, 2, 3, 4, 5]
print("------------------")

# 리스트 중간에 요소 추가하기
print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a) # [10, 1, 2, 3, 4, 5]

#  + 를 사용한 연결 연산자와 append, insert, extend의 차이 
# 연결 연산자는 원본에 아무런 영향을 주지 않는 '비파괴적'이지만, 
# append, insert, extendsms 는 리스트에 직접적인 영향을 주는 '파괴적'이다