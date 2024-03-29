# sys 모듈
# : 시스템과 관련된 정보를 가지고 있는 모듈 
# 
import sys
print(sys.argv)
print("---")

# 컴퓨터 환경과 관련된 정보를 출력합니다.
print("getwindowsversion:()", sys.getwindowsversion())
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

# 프로그램을 강제로 종료합니다.
sys.exit()