# for 반복문

# for 반복문 : 리스트와 범위 조합하기 
array = [273, 32, 103, 57, 52]
for element in array:
    print(element)

# for 반복문 : 반대로 반복하기 
for i in range(4, 0 - 1, -1):
    print("현재 반복 변수: {}".format(i))
print("----------------------------------")
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))

