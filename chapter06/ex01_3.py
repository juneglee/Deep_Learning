#  try 구문 내부에서 return 키워드를 사용하는 경우  

# try 구문 내부에서 return 키워드를 사용하는 경우 
def test():
    print("test() 함수의 첫 줄입니다.") #
    try:
        print("try 구문이 실행되었습니다.") #
        return
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.") #
    print("test() 함수의 마지막 줄입니다.")
test()
print("---------------------------------------")

# fianlly 키워드 활용
def write_text_file(filename, text):
    try:
        file = open(filename, "w") #
        return
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        file.close()
write_text_file("test.txt", "안녕하세요!")
print("---------------------------------------")

# 반복문과 함꼐 사용하는 경우 
print("프로그램이 시작되었습니다.") #
while True:
    try:
        print("try 구문이 실행되었습니다.")
        break
        print("try 구문의 break 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.") #
    print("while 반복문의 마지막 줄입니다.") #
print("프로그램이 종료되었습니다.") #