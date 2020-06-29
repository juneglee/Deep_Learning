# 딕셔너리에 값 추가하기/ 제거하기 
#
#  딕셔너리[새로운 키] = 새로운 값

# 딕셔너리 요소에 추가 
dictionary = {}
print("요소 추가 이전:", dictionary)
print("---------------------------------------")
# 딕셔너리에 요소를 추가
dictionary["name"] = "새로운 이름"
dictionary["head"] = "새로운 정신"
dictionary["body"] = "새로운 몸"

print("요소 추가 이후:", dictionary)

# 딕셔너리 요소에 제거
dictionary2 = {
    "name": "7D 건조 망고",
    "type": "당절임"
    }

print("요소 제거 이전:", dictionary2)
print("---------------------------------------")
# 딕셔너리의 요소를 제거합니다.
del dictionary2["name"]
del dictionary2["type"]

# 요소 제거 후에 내용을 출력해봅니다.
print("요소 제거 이후:", dictionary2)
