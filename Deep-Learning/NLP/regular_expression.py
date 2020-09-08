import re

# . 한 개의 임의의 문자
r = re.compile("a.c")
print(r.search("abd")) # None
print(r.search("abc")) # <re.Match object; span=(0, 3), match='abc'>

# ? 앞의 문자가 존재 or 미존재
r = re.compile("abc?") # c는 없어도 되고, 있더도 되지만, a와 b는 반드시 있어야 한다. 이때 abc는 하나만 존재해야 한다
print(r.search("abc")) # <re.Match object; span=(0, 3), match='abc'>
print(r.search("ab")) # <re.Match object; span=(0, 2), match='ab'>

# * 앞의 문자가 0개 이상
r = re.compile("ab*c") # b 는 0개 이상이라서 있어도 되고 없어도 되며, 마찬가지로 b를 제외한 a c는 하나만 존재 
print(r.search("ac")) # <re.Match object; span=(0, 2), match='ac'>
print(r.search("abc")) # <re.Match object; span=(0, 3), match='abc'>
print(r.search("abbbc")) # <re.Match object; span=(0, 5), match='abbbc'>

# + 앞의 문자가 1개 이상
r = re.compile("ab+c")
print(r.search("ac")) # None
print(r.search("abc")) # <re.Match object; span=(0, 3), match='abc'>
print(r.search("abbbc")) # <re.Match object; span=(0, 5), match='abbbc'>

# ^ 시작되는 글자를 지정
r = re.compile("^bc")
print(r.search("abc")) # None
print(r.search("bc")) # <re.Match object; span=(0, 2), match='bc'>

# {숫자} 해당 문자를 숫자만큼 반복
r = re.compile("ab{2}c")
print(r.search("abc")) # None
print(r.search("abbc")) # <re.Match object; span=(0, 4), match='abbc'>
print(r.search("abbbc")) # None

# {숫자1, 숫자2} 해당 문자를 숫자1 이상, 숫자2 이하만큼 반복
r = re.compile("ab{2,4}c")
print(r.search("abc")) # None
print(r.search("abbc")) # <re.Match object; span=(0, 4), match='abbc'>
print(r.search("abbbc")) # <re.Match object; span=(0, 5), match='abbbc'>
print(r.search("abbbbc")) # <re.Match object; span=(0, 6), match='abbbbc'>
print(r.search("abbbbbc")) # None

# {숫자,} 해당 문자를 숫자 이상 만큼 반복
r = re.compile("ab{2,}c")
print(r.search("abc")) # None
print(r.search("abbc")) # <re.Match object; span=(0, 4), match='abbc'>
print(r.search("abbbc")) # <re.Match object; span=(0, 5), match='abbbc'>
print(r.search("abbbbc")) # <re.Match object; span=(0, 6), match='abbbbc'>
print(r.search("abbbbbc")) # <re.Match object; span=(0, 7), match='abbbbbc'>

# [문자] 문자들 중 한개의 문자와 매치
# [a-zA-Z]는 알파벳 전부를 의미, [0-9]는 숫자 전부를 의미
r = re.compile("[abc]")
print(r.search("a")) # <re.Match object; span=(0, 1), match='a'>
print(r.search("d")) # None

# [^문자] 제외한 모든 문자를 매치
r = re.compile("[^abc]")
print(r.search("a")) # None
print(r.search("d")) # <re.Match object; span=(0, 1), match='d'>