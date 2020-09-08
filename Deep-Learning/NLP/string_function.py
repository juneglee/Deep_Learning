# upper()
# lower()
# capitalize()
# title()
# swapcase()
#
# Text =  "hello"
# upper_text = Text.upper()
# print(upper_text) # HELLO
#
# lower_text = upper_text.lower()
# print(lower_text) # hello
# print("--------------------")
#
# sentence = "hellw python"
# capitalize_sentence = sentence.capitalize()
# print(capitalize_sentence) # Hellw python
#
# title_sentence = sentence.title()
# print(title_sentence) # Hellw Python
#
# swapped_title_sentence = title_sentence.swapcase()
# print(swapped_title_sentence) # hELLW pYTHON

# 공백 제거
# strip()
# rstrip()
# lstrip()
# replace(a, b)
# 개행문자도 제거한다

text = " hello python \n"
print(text)
print(text.strip())
print(text.rstrip())
print(text.lstrip())

print(text.replace(" ", "."))
print(text.replace("hello", "bye"))

# split()
# join()
# solitlines()

text = 'hello python'
print(text)

print(text.split())
print(text.split('p'))

test = "1, 62, 7, 543, 13\n"
split_test = test.strip().split(',')
print(split_test)
print(list(map(int, test.strip().split(','))))

join_split_test = "@".join(split_test)

test = 'hello python\n this is nlp tutorial\n string function examples\n'
print(test)
print(test.splitlines())

# 구성 문자열 판별
# isdigit()
# isalpha()
# isalnum()
# islower()
# isupper()
# isspace()
# startswith(‘hi’)
# endswith(‘hi’)

test = '123'
print(test.isdigit())

text = 'abc'
print(text.isalpha())

text = '1a2b3c'
print(text.isdigit())
print(text.isalpha())
print(text.isalnum())

text = 'hello'
print(text.islower())
print(text.isspace())

text = "Hello"
print(text.isupper())
print(text.isspace()) # False

text = 'hello'
print(text.startswith('h')) # True
print(text.endswith("o")) # True

# 검색
# count
# find
# find()
# rfind
# index
# rindex

text = "hi1 hi2 hi3 hi4"
print(text.count("hi"))
print(text.find("hi"))
print(text.find('hi', 1))
print(text.rfind('hi'))
print(text.index('hi'))
print(text.index('hi5')) # error