from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

from math import sqrt

import pandas as pd
import numpy as np

File_Path = '../datasets/admission_data.csv'
admission_df = pd.read_csv(File_Path).drop('Serial No.', axis=1)

admission_df.haed()

polynomial_transformer = PolynomialFeatures(6)
polynomial_features = polynomial_transformer.fit_transform(admission_df.values)
features = polynomial_transformer.get_feature_names(admission_df.columns)

label = admission_df[['Chance of Admit ']]

train_data, test_data, train_label, test_label = train_test_split(admission_df, label, test_size=0.3, random_state=5)

model = Lasso(alpha=0.001, max_iter=1000, normalize=True)
"""
alpha : 정규화 식에서의 람다 값 지정.
max_iter : 경사 하강법 반복 횟수 지정.
normalize : True로 지정 시, 자동으로 Feature Scaling 적용

이는 L2 정규화 모델 Ridge 에서도 동일하게 적용된다.
"""
model.fit(train_data, train_label)

train_predict = model.predict(train_data)
test_predict = model.predict(test_data)

mse = mean_squared_error(train_label, train_predict)
print("training set에서의 성능")
print("=====================")
print(sqrt(mse))

mse = mean_squared_error(test_label, test_predict)
print("testing set에서의 성능")
print("=====================")
print(sqrt(mse))