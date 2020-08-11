import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix
from imblearn.over_sampling import SMOTE
from sklearn.utils import resample
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


class LogisticRegression:
    def __init__(self, learning_rate=0.1, threshold=0.01, max_iterations=100000, fit_intercept=True, verbose=False):
        self._learning_rate = learning_rate  # 학습 계수
        self._max_iterations = max_iterations  # 반복 횟수
        self._threshold = threshold  # 학습 중단 계수
        self._fit_intercept = fit_intercept  # 절편 사용 여부를 결정
        self._verbose = verbose  # 중간 진행사항 출력 여부

    # theta(W) 계수들 return
    def get_coeff(self):
        return self._W

    # 절편 추가
    def add_intercept(self, x_data):
        intercept = np.ones((x_data.shape[0], 1))
        return np.concatenate((intercept, x_data), axis=1)

    # 시그모이드 함수(로지스틱 함수)
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def cost(self, h, y):
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()

    def fit(self, x_data, y_data):
        num_examples, num_features = np.shape(x_data)

        if self._fit_intercept:
            x_data = self.add_intercept(x_data)

        # weights initialization
        self._W = np.zeros(x_data.shape[1])

        for i in range(self._max_iterations):
            z = np.dot(x_data, self._W)
            hypothesis = self.sigmoid(z)

            # 실제값과 예측값의 차이
            diff = hypothesis - y_data

            # cost 함수
            cost = self.cost(hypothesis, y_data)
            gradient = np.dot(x_data.transpose(), diff) / num_examples

            # gradient에 따라 theta 업데이트
            self._W -= self._learning_rate * gradient

            # 판정 임계값에 다다르면 학습 중단
            if cost < self._threshold:
                return False

            # 100 iter 마다 cost 출력
            if (self._verbose == True and i % 100 == 0):
                print('cost :', cost)
                print('diff :', diff)

    def predict_prob(self, x_data):
        if self._fit_intercept:
            x_data = self.add_intercept(x_data)

        return self.sigmoid(np.dot(x_data, self._W))

    def predict(self, x_data):
        # 0,1 에 대한 판정 임계값은 0.5 -> round 함수로 반올림
        return self.predict_prob(x_data).round()

df = pd.read_csv('./creditcard.csv')
feature_names = ['V1', 'V3', 'V4', 'V7', 'V9', 'V10', 'V11', 'V12', 'V14', 'V16', 'V17', 'V18']

data = df[feature_names]
target = df['Class']

X_train, X_test, y_train, y_test = train_test_split(data, target, train_size=0.70, test_size=0.30, random_state=1)


X = pd.concat([X_train, y_train], axis=1)

# separate minority and majority classes
not_fraud = X[X.Class == 0]
fraud = X[X.Class == 1]

# upsample minority
fraud_upsampled = resample(fraud,
                          replace=True, # sample with replacement
                          n_samples=len(not_fraud), # match number in majority class
                          random_state=27) # reproducible results

# combine majority and upsampled minority
upsampled = pd.concat([not_fraud, fraud_upsampled])

X_train = upsampled[feature_names]
y_train = upsampled['Class']

X = np.array(X_train)
y = np.array(y_train)

skf = StratifiedKFold(n_splits=4, shuffle=False, random_state=None)

model = LogisticRegression(learning_rate=0.01, verbose=True)

accuracy = []
recall = []
precision = []
f1 = []

for i, (idx_of_train, idx_of_test) in enumerate(skf.split(X, y)):
    X_train, X_test = X[idx_of_train], X[idx_of_test]
    y_train, y_test = y[idx_of_train], y[idx_of_test]

    model.fit(X_train, y_train)
    predict_data = model.predict(X_test)

    accuracy.append(accuracy_score(predict_data, y_test))
    recall.append(recall_score(predict_data, y_test))
    precision.append(precision_score(predict_data, y_test))
    f1.append(f1_score(predict_data, y_test))
    print("accuracy_score : {0}\n"
          "recall_score : {1}\n"
          "precision_score : {2}\n"
          "f1_score : {3}\n".format(accuracy[i], recall[i], precision[i], f1[i]))

accuracy_avg = sum(accuracy)/len(accuracy)
recall_avg = sum(recall)/len(recall)
precision_avg = sum(precision)/len(precision)
f1_avg = sum(f1)/len(f1)

"""
class_names = ['not_fraud', 'fraud']
matrix = confusion_matrix(y_test, predict_data)
# Create pandas dataframe
dataframe = pd.DataFrame(matrix, index=class_names, columns=class_names)
# Create heatmap
sns.heatmap(dataframe, annot=True, cbar=None, cmap="Blues", fmt='g')
plt.title("Confusion Matrix"), plt.tight_layout()
plt.ylabel("True Class"), plt.xlabel("Predicted Class")
plt.show()
"""