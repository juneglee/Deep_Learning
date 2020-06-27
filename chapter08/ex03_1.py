# 덱스트 데이터 & 바이너리 데이터 
# 파일은 크게 덱트스 데이터와 바이너리 데이터로 구분된다 .
# 덱스트 데이터 
# 컴퓨터는 내부적으로 모든 처리를 0과 1로 이루어진 이진(binary) 숫자 수행 
# 바이너리 데이터 
# 텍스트 에디터로 열었을 때 의미를 이해할 수 없는 데이터 
#
# 인코딩과 디코딩 
# 인코딩 : 바이너리 데이터를 읽어서 이미지로 보여주려는 변환
# 디코딩 : 인코딩한 것을 반대로 돌리는 것 

# 이미지 읽어 들이고 저장하기 
from urllib import request

# urlopen() 함수로 구글의 메인 페이지를 읽습니다.
target = request.urlopen("http://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

# write binary[바이너리 쓰기] 모드로
file = open("output.png", "wb")
file.write(output)
file.close()

# 인트리 포인트 (entry point)
# : python 명령어를 사용해서 첫 진입 파일을 엔트리 포인트라고 부릅니다 

# __name__=="__main__" 
#: 현재 파일이 엔트리 포인트인지 확인할 때 사용하는 코드 

