# 리스트 내부에 있는지 확인하기 : in/not in 연산자 
# 사용법 
# 값 in 리스트 / 값 not in 리스트 

list_a = [273, 32, 108, 57, 52]
print("내부에 있을 때 : in")
print(273 in list_a) # True
print(99 in list_a) # False
print(100 in list_a) # False
print(52 in list_a) # True
print("------------------------------------")
print("내부에 없을 때 : not in")
print(273 not in list_a) # False
print(99 not in list_a) # True
print(100 not in list_a) # True
print(52 not in list_a) # False
