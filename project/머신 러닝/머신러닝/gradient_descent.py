import numpy as np
import matplotlib.pyplot as plt
"""
matplotlib.pyplot 모듈 설명 : 경사 하강을 통한 실제 변화를 시각화 하기 위해 사용
1. scatter(x, y) : x축과 y축을 가지는 그래프 구현
2. plot() : 앞에서 구현한 그래프 위에 
3. show() : 지금까지 그린 그래프 출력
"""

def prediction(theta_0, theta_1, x):
    """주어진 학습 데이터 벡터 x에 대해서 모든 예측 값을 벡터로 리턴하는 함수"""
    return theta_0 + (theta_1 * x)


def prediction_difference(theta_0, theta_1, x, y):
    """모든 예측 값들과 목표 변수들의 오차를 벡터로 리턴해주는 함수"""
    return prediction(theta_0, theta_1, x) - y


def gradient_descent(theta_0, theta_1, x, y, iterations, alpha):
    """주어진 theta_0, theta_1 변수들을 경사 하강를 하면서 업데이트 해주는 함수"""
    m = len(x)
    cost_list = [] # 손실 함수의 결과값 저장

    for i in range(iterations):  # 정해진 번만큼 경사 하강을 한다
        error = prediction_difference(theta_0, theta_1, x, y)  # 예측값들과 입력 변수들의 오차를 계산
        cost = (error @ error) / (2 * m) # 손실함수 값 계산
        cost_list.append(cost)

        theta_0 = theta_0 - alpha * error.mean()
        theta_1 = theta_1 - alpha * (error * x).mean()

        if i % 10 == 0:
            plt.scatter(house_size, house_price)
            plt.plot(house_size, prediction(theta_0, theta_1, x), color='red')
            plt.show()

    return theta_0, theta_1, cost_list


# 입력 변수(집 크기) 초기화 (모든 집 평수 데이터를 1/10 크기로 줄임)
house_size = np.array([0.9, 1.4, 2, 2.1, 2.6, 3.3, 3.35, 3.9, 4.4, 4.7, 5.2, 5.75, 6.7, 6.9])

# 목표 변수(집 가격) 초기화 (모든 집 값 데이터를 1/10 크기로 줄임)
house_price = np.array([0.3, 0.75, 0.45, 1.1, 1.45, 0.9, 1.8, 0.9, 1.5, 2.2, 1.75, 2.3, 2.49, 2.6])

# theta 값들 초기화 (아무 값이나 시작함)
theta_0 = 2.5
theta_1 = 0

# 학습률 0.1로 200번 경사 하강
theta_0, theta_1, cost_l = gradient_descent(theta_0, theta_1, house_size, house_price, 200, 0.1)

print(theta_0, theta_1)