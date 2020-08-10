import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import numpy as np

iris_data = load_iris()

X = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
y = pd.DataFrame(iris_data.target, columns=['Class'])

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

model = DecisionTreeClassifier(max_depth=4)
"""
속성 설명
max_depth : 결정 트리의 최대 깊이 지정
"""
model.fit(x_train, y_train)
predict_data = model.predict(x_test)
model.score(x_test, y_test)  # 모델 성능 평가

feature_importance = model.feature_importances_  # 모델의 속성 중요도 반환

indices_sorted = np.argsort(feature_importance)

plt.figure()
plt.title("Feature Importances")
plt.bar(range(len(feature_importance)), feature_importance[indices_sorted])
plt.xticks(range(len(feature_importance)), X.columns[indices_sorted], rotation=90)
plt.show()