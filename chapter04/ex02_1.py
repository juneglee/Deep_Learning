# 딕셔너리와 반복문
#
# 리스트 : 인덱스를 기반으로 값을 저장하는 것
#           선언 형식 : list_a = [] /  사용예 list_a[1]
# 딕셔너리 : 키를 기반으로 값을 저장하는 것
#           선언 형식 : dict_a = {} /  사용예 dict_a["name"]

# 딕셔너리 선언하기 
# 변수 = {
#  키 : 값,
#  키 : 값,
#  ...
#  키 : 값
# }
dict_a = {
    "name1" : "user1",
    "name2" : "user2"
}

# 딕셔너리의 요소에 접근하기 
print(dict_a["name1"])
print(dict_a["name2"])

# 리스트와 딕셔너리를 값으로 넣기 
dict_b = {
    "dirctor" : ["안소니","조"],
    "cast" : ["아이언맨","타노스","헐크","토르"]
}
print(dict_b) # {'dirctor': ['안소니', '조'], 'cast': ['아이언맨', '타노스', '헐크', '토르']}
print(dict_b["dirctor"]) # ['안소니', '조']

# 딕셔너리의 요소에 접근하기 
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

print("name:", dictionary["name"]) # name: 7D 건조 망고
print("type:", dictionary["type"]) # type: 당절임
print("ingredient:", dictionary["ingredient"]) # ingredient: ['망고', '설탕', '메타중아황산나트륨', '치자황색소']
print("origin:", dictionary["origin"]) # origin: 필리핀
print("--------------------------------------------")

# 값 변경
dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"]) #  name: 8D 건조 망고
