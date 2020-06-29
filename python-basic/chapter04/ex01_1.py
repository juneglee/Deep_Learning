# 리스트 
# - 파이썬에서 리스트의 의미는 여러가지 자료를 저장할 수 있는 자료

# 사용법 [요소, 요소, 요소 ...] 
# 이때 요소는 element라고 부른다 

[1, 2, 3, 4]
["안","녕","하","세","요"]
[273,32,108,'문자열',True,False]

list_a = [273,32,108,'문자열',True,False]
print(list_a[0]) # 273
print(list_a[1]) # 32
print(list_a[2]) # 108
print(list_a[3]) # 문자열
print(list_a[4]) # True
print(list_a[5]) # False

# 리스트 사용 방법 
# 첫째, 대괄호 안에 음수를 넣어 뒤에서부터 요소를 선택할 수 있습니다.
print(list_a[-1]) # False
print(list_a[-2]) # True

# 둘쨰, 리스트 접근 연산자를 다음과 같이 이중으로 사용할 수 있습니다.
print(list_a[3]) # 문자열
print(list_a[3][0]) # 문

# 셋째, 리스트 안에 리스트를 사용할 수 있습니다
list_b = [[1, 2, 3],[4, 5 ,6],[7 ,8 ,9]]
print(list_b[1]) # [4, 5 ,6]
print(list_b[1][1]) # 5

# 리스트 index 안에 존재하지 않는 요소를 접근할때 indexError 발생