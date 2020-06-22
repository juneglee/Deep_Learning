# 리스트 요소 제거하기 
# 인덱스로 제거하기 및 값으로 제거하기가 있다 

# 인덱스로 제거하기 : del, pop
# 사용법
# del 리스트명[인덱스]
# 리스트명.pop(인덱스)
list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")
# 제거 방법[1] – del
del list_a[1]
print("del list_a[1]:", list_a) # [0, 2, 3, 4, 5]
# 제거 방법[2] – pop()
list_a.pop(2)
print("pop(2):", list_a) # [0, 2, 4, 5]

# 범위를 지정하여 제거할 수 있다 
list_b = [0, 1, 2, 3, 4, 5]
del list_b[3:5]
print("del list_b[3:5]:", list_b) # [0, 1, 2, 5]
list_c = [0, 1, 2, 3, 4, 5]
del list_c[:3]
print("del list_c[:3]:", list_c) # [3, 4, 5]
list_d = [0, 1, 2, 3, 4, 5]
del list_d[3:]
print("del list_d[3:]:", list_d) # [0, 1, 2]

# 값으로 제거하기 : remove
# 사용법 
# 리스트.remove(값)
list_e = [1, 2, 1, 2]
list_e.remove(2)
print(list_e) # [1, 1, 2]

# 모두 제거하기 : clear
# 사용법
# 리스트.clear()
list_f = [0, 1, 2, 3, 4, 5]
list_f.clear()
print(list_f) #[]
