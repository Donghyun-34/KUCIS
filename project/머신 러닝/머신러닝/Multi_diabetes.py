# 필요한 라이브러리 import
from sklearn import datasets
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd

diabetes_dataset = datasets.load_diabetes()

# 지난 과제 코드를 가지고 오세요.
polynomial_transformer = PolynomialFeatures(2)
polynomial_data = polynomial_transformer.fit_transform(diabetes_dataset.data)
polynomial_feature_names = polynomial_transformer.get_feature_names(diabetes_dataset.feature_names)
X = pd.DataFrame(polynomial_data, columns = polynomial_feature_names)
# 목표 변수
y = pd.DataFrame(diabetes_dataset.target, columns=['diabetes'])

# 코드를 쓰세요
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=5)
model = LinearRegression()
# 학습시키기
model.fit(x_train, y_train)

y_test_prediction = model.predict(x_test)
y_test_prediction


mse = mean_squared_error(y_test, y_test_prediction)

print(mse ** 0.5)