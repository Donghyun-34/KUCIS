from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import pandas as pd

iris_data = load_iris()

iris_pd = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
iris_label_pd = pd.DataFrame(iris_data.target, columns=['class'])

train_data, test_data, train_label, test_label = train_test_split(iris_pd, iris_label_pd, test_size=0.2, random_state=5)

train_label = train_label.values.ravel()
"""
필수는 아니지만 사용하지 않으면 경고창 출력
"""

model = LogisticRegression(solver='saga', max_iter=2000)
""" Optional parameter
solver : 모델을 최적화를 할 때 어떤 알고리즘을 사용할 지를 지정
max_iter : 최적화 과정의 반복 횟수 지정 -> 물론 횟수 내에서 충분히 최적화 되었다고 판단되면 언제든지 중단 될 수 있다.
"""

# 학습
model.fit(train_data, train_label)

# 예측
model.predict(test_data)

# 예측 결과 비교
accurancy = model.score(test_data, test_label)

print(accurancy)