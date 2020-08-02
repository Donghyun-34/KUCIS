from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd

boston_data = load_boston()

# 입력 변수
Data = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
# 목표 변수
Label = pd.DataFrame(boston_data.target, columns=['MEDV'])

# 여기서 ['CRIM']과 [['CRIM]]의 결과는 동일하지만 [['CRIM]]의 경우에는 열 이름이 'CRIM'으로 지정.
crim_data = Data[['CRIM']]

# training set과 test set 구별
"""
(1) x : 입력 변수
(2) y : 목표 변수
(3) test_size : 전체 데이터의 몇 퍼센트를 test set으로 할지를 지정
(4) random_state : test set을 어떻게 정할지에 대한 옵션
"""
train_data, test_data, train_labels, test_labels = train_test_split(crim_data, Label, test_size=0.2, random_state=5)

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(train_data, train_labels)

# test_data 예측
test_prediction = model.predict(test_data)

# RMSE 계산
rmse = mean_squared_error(test_labels, test_prediction) ** 0.5

print(rmse)