# 딕셔너리 내부에 키가 있는지 확인
# 
# in 키워드를 사용하여 내부에 키가 있는지 없는지 확인
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}
key = input("> 접근하고자 하는 키: ")
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

# get() 함수 
# 존재하지 않는 키에 접근하는 상황에서 두번쨰 대처 방법으로는 딕셔너리의 get()
value = dictionary.get("none")
print("값:", value)
if value == None:
    print("존재하지 않는 키에 접근했었습니다.")


# for 반복문 : 딕셔너리와 함께 사용하기 
#
# for 키 변수 in 딕셔너리:
#     코드 
for key in dictionary:
    print(key, ":", dictionary[key])
