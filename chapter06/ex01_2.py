#  파일이 제대로 닫혔는지 확인 

# 파일이 제대로 닫혔는지 확인 
try:
    file = open("info.txt", "w")
    file.close()
except Exception as e:
    print(e)
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)
print("---------------------------------------")

# 파일 처리 중간에 예외 발생
try:
    file = open("info.txt", "w")
    예외.발생()
    file.close()
except Exception as e:
    print(e)
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)
print("---------------------------------------")

# finally 구문 사용해 파일 닫기 
try:
    file = open("info.txt", "w")
    예외.발생()
except Exception as e:
    print(e)
finally:
    file.close()
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)
print("---------------------------------------")

# try exceop 구문 끝난 후 파일 닫기 
try:
    file = open("info.txt", "w")
    예외.발생해라()
except Exception as e:
    print(e)

file.close()
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)
print("---------------------------------------")

