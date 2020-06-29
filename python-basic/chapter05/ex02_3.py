# 리턴

# 자료 없이 리턴하기 
def return_test():
    print("A 위치입니다.")
    return # 리턴합니다.
    print("B 위치입니다.")
return_test() # A 위치입니다.

# 자료와 함께 리턴하기
def return_test():
    return 100
value = return_test()
print(value) # 100

# 아무것도 리턴하지 않기 
def return_test():
    return
value = return_test()
print(value) # None
