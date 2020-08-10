import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np

iris_data = load_iris()

x = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
y = pd.DataFrame(iris_data.target, columns=['Class'])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)
y_train = y_train.values.ravel()

model = RandomForestClassifier(n_estimators=100, max_depth=4)
"""
n_estimators : 몇개의 결정 트리를 만들지를 결정하는 속성, 기본 값은 10
max_depth : 각 결정 트리들의 최대 깊이를 설정하는 속성
"""

model.fit(x_train, y_train)
prediction_data = model.predict(x_test)
score = model.score(x_test, y_test)
feature_importance = model.feature_importances_  # 각 속성들의 속성 중요도 반환

indices_sorted = np.argsort(feature_importance)

plt.figure()
plt.title("Feature Importances")
plt.bar(range(len(feature_importance)), feature_importance[indices_sorted])
plt.xticks(range(len(feature_importance)), x.columns[indices_sorted], rotation=90)
plt.show()