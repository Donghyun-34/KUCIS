import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class GradientDescent():
    def __init__(self, learning_rate=0.01, threshold=0.01, max_iterations=1000):
        self._learning_rate = learning_rate
        self._threshold = threshold
        self._max_iterations = max_iterations
        self._W = None

    def fit(self, x_data, y_data):
        num_examples, num_features = np.shape(x_data)
        
        self._W = np.ones(num_features)
        x_data_transposed = x_data.transpose()

        for i in range(self._max_iterations):
            # 실제값과 예측값의 차이
            diff = np.dot(x_data, self._W) - y_data

            # diff를 이용하여 cost 생성 : 오차의 제곱합 / 2 * 데이터 개수
            cost = np.sum(diff ** 2) / (2 * num_examples)
            print("{0} Epoch cost : {1}".format(i, cost))

            # transposed X * cost / n
            gradient = np.dot(x_data_transposed, diff) / num_examples

            # W벡터 업데이트
            self._W = self._W - self._learning_rate * gradient

            # 판정 임계값에 다다르면 학습 중단
            if cost < self._threshold:
                return self._W

        return self._W



df = pd.read_csv('./creditcard.csv')
feature_names = ['V1', 'V3', 'V4', 'V7', 'V9', 'V10', 'V11', 'V12', 'V14', 'V16', 'V17', 'V18']

data = df[feature_names]
target = df['Class']

X = np.array(data)
y = np.array(target)

X_train, X_test, y_train, y_test = train_test_split(data, target, train_size=0.70, test_size=0.30, random_state=1)

model = GradientDescent()

theta = model.fit(X, y)
