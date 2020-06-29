# 문자열, 리스트 , 딕셔너리와 관련된 기본 함수 

# 리스트에 적용할 수 있는 기본함수 : min(), max(), sum()
# 리스트 뒤집기 : reversed()
# 현재 인덱스가 몇 번째인지 확인하기 : enumerate()
# 딕셔너리로 쉽게 반복문 작성하기 : item()
# 리스트 안에 for 문 사용하기 : 리스트 내포 

# 리스트에 적용할 수 있는 기본함수 : min(), max(), sum()
numbers = [103, 52, 273, 37, 77]
print(min(numbers)) # 37
print(min(103, 52, 273, 37, 77)) # 37
print(max(numbers)) # 273
print(max(103, 52, 273, 37, 77)) # 273
print(sum(numbers)) # 542
print("===================================")

# 리스트 뒤집기 : reversed()
list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)
print("# reversed() 함수")
print("reversed([1, 2, 3, 4, 5]):", list_reversed) # 이터레이터 참조
print("list(reversed([1, 2, 3, 4, 5])):", list(list_reversed))
print("------------------------------------")
print("# reversed() 함수와 반복문")
print("for i in reversed([1, 2, 3, 4, 5]):")
for i in reversed(list_a):
    print("-", i)
# reversed() 함수는 두번 출력하여도 제너레이터이기 때문에 
# 함수의 결과를 여러번 활용하지 않는다 
print("===================================")

# 현재 인덱스가 몇 번째인지 확인하기 : enumerate()
example_list = ["요소A", "요소B", "요소C"]
print("# 단순 출력")
print(example_list)  # ['요소A', '요소B', '요소C']
print("------------------------------------")
print("# enumberate() 함수 적용 출력")
print(enumerate(example_list)) # <enumerate object at 0x01659A48>
print("------------------------------------")
print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))  # [(0, '요소A'), (1, '요소B'), (2, '요소C')]
print("------------------------------------")
# for 반복문과 enumerate() 함수 조합해서 사용하기
print("# 반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))
print("===================================")

# 딕셔너리로 쉽게 반복문 작성하기 : item()
example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C",
    }
print("# 딕셔너리의 items() 함수")
print("items():", example_dictionary.items())
print("------------------------------------")
print("# 딕셔너리의 items() 함수와 반복문 조합하기")
for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))
print("===================================")

# 반복문 사용한 리스트 생성 
array = []
for i in range(0, 20, 2):
    array.append(i * i)
print(array) # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
print("------------------------------------")
# 리스트 안에 for 문 사용하기 
# 리스트 내포
# 리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것]
array = [i * i for i in range(0, 20, 2)]
print(array)
print("------------------------------------")
# 조건을 활용한 리스트 내포
# 리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것 if 조건문]
array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]
print(output)



