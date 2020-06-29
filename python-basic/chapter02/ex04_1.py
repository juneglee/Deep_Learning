# 숫자와 문자열의 다양한 기능 
# 
# 문자열 format() 함수 
# - 문자열을 가지고 있는 함수 
# - "{}".format(10) 형식이며 
# -  중괄호의 개수와 괄호안의 매개변수의 개수가 반드시 같아야한다

String_a = "{}".format(10)
String_b = "{} {}".format(10, 20)
String_c = "{} {} {}".format(10, 20, 30)  
print(String_a) # 10
print(String_b) # 10 20 
print(String_c) # 10 20 30
print("----------------------")
print(type(String_a)) # str
print(type(String_b)) # str
print(type(String_c)) # str

String_d = "포르쉐 {}".format(911)
print(String_d) # 포르쉐 911

# format() 함수의 다양한 기능
output_a = "{:d}".format(52)     #52
# 특정 칸에 출력
output_b = "{:5d}".format(52)    #   52
output_c = "{:10d}".format(52)   #        52
# 빈칸을 0으로 채우기 
output_d = "{:05d}".format(52)   #00052
output_e = "{:05d}".format(-52)  #-0052
# 기호와 함께 출력하기
output_f = "{:+d}".format(52)    #+52 
output_g = "{:+d}".format(-52)   #-52 
output_h = "{: d}".format(52)    # 52 # 공백이 채워지지 않는다  
output_i = "{: d}".format(-52)   #-52 
#조합하기
output_j = "{:+5d}".format(52)   #  +52 
output_k = "{:+5d}".format(-52)  #  -52
output_l = "{:=+5d}".format(52)  #+  52
output_m = "{:=-5d}".format(-52) #-  52 
output_n = "{:+05d}".format(52)  #+0052
output_o = "{:-05d}".format(-52) #-0052 

# 부동 소수점 출력의 다양한 형태
output_1 = "{:f}".format(52.273) #52.273000 # 정수와 유사하다 
output_2 = "{:15.3f}".format(52.273) # ... 52.273
output_3 = "{:15.2f}".format(52.273) # ...  52.27
output_4 = "{:15.1f}".format(52.273) # ...   52.2

# 의미 없는 부동 소수점 제거  
output_g1 = 52.0
output_g2 = "{:g}".format(output_g1)
print(output_g1) # 52.0 
print(output_g2) # 52






 