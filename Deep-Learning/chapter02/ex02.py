# 선형회귀 (linear regression) : 평균 제곱 오차 (mean square error : MSE)
# : 임의의 직선을 그어 이에 대한 평균 제곱 오차를 구하고, 
#  이 값(오차)을 가장 작게 만들어주는 a와 b 값을 찾아 가는 작업 
import numpy as np

#가상의 기울기 a와 y 절편 b
fake_a_b=[3,76]

# x 값과 y값
data = [[2, 81], [4, 93], [6, 91], [8, 97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

# y=ax + b에 a,b 값 대입하여 결과를 출력하는 함수
def predict(x):
   return fake_a_b[0]*x + fake_a_b[1]

# MSE 함수 (평균 제곱 공식) 
def mse(y, y_hat):
   return ((y - y_hat) ** 2).mean()
   # 예측값(y_hat)과 실제 값(y)을 각각 mse ()라는 함수의 y_hat와 y자리에 입력해서 평균 제곱을 구한다 

# MSE 함수를 각 y값에 대입하여 최종 값을 구하는 함수
def mse_val(predict_result,y):
   return mse(np.array(predict_result), np.array(y))

# 예측값이 들어갈 빈 리스트
predict_result = []

# 모든 x값을 한 번씩 대입하여 predict_result 리스트완성.
for i in range(len(x)):
   predict_result.append(predict(x[i]))
   print("공부시간=%.f, 실제점수=%.f, 예측점수=%.f" % (x[i], y[i], predict(x[i])))

# 최종 MSE 출력
print("MSE 최종값: " + str(mse_val(predict_result,y)))

