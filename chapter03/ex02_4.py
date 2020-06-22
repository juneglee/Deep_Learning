# False로 변환되는 값
# - None / '0' / 빈 컨테이너는 False
print("# if 조건문에 0 넣기")
if 0:
    print("0은 True로 변환됩니다")
else:
    print("0은 False로 변환됩니다")
    print()

    print("# if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 True로 변환됩니다")
else:
    print("빈 문자열은 False로 변환됩니다")

# Pass 키워드 
# 골격을 잡아놓고 나중에 처리하기 위해서 만들어짐
number = input("정수 입력> ")
number = int(number)

# 빈 공간을 사용할 경우 indentationError가 발생한다 
# if number > 0:
    # 양수일 때: 아직 미구현 상태입니다.
# else:
    # 음수일 때: 아직 미구현 상태입니다.

# 이때 사용하기 위해서 pass를 사용하여 골격을 잡아 놓을 수 있다 
if number > 0:
    pass
else:
    pass

# raise NotImplementedError : 아직 구현하지 않은 부분이라고 오류를 강제로 발생할 수 있다 
if number > 0:
    raise NotImplementedError 
else:
    raise NotImplementedError 