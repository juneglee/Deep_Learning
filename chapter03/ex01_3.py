#날짜/시간 활용하기 
import datetime
now = datetime.datetime.now()

# 날짜/시간 출력하기 
print(now.year , "년")
print(now.month , "월")
print(now.day , "일")
print(now.hour , "시")
print(now.minute , "분")
print(now.second , "초")
print("---------------------------------------")

# 날짜/시간을 한줄로 출력하기 
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))
print("---------------------------------------")

# 오전과 오후를 구분하기
if now.hour < 12:
    print("현재 시간은 {}시로 오전입니다.".format(now.hour))
if now.hour > 12:
    print("현재 시간은 {}시로 오후입니다.".format(now.hour))
print("---------------------------------------")

# 계절을 구분하기
if 3 <= now.month <= 5:
    print("이번 시간은 {}월로 봄입니다.".format(now.month))
if 6 <= now.month <= 8:
    print("이번 시간은 {}월로 여름입니다.".format(now.month))
if 9 <= now.month <= 11:
    print("이번 시간은 {}월로 가을입니다.".format(now.month))
if now.month == 12 or 1 <= now.month <= 2:
    print("이번 시간은 {}월로 겨울입니다.".format(now.month))
