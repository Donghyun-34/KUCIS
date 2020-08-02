# 필요한 라이브러리 import
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import pandas as pd  

wine_data = datasets.load_wine()


# 입력 변수를 사용하기 편하게 pandas dataframe으로 변환
data = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)

# 목표 변수를 사용하기 편하게 pandas dataframe으로 변환
label = pd.DataFrame(wine_data.target, columns=['Y/N'])

# 코드를 쓰세요
train_data, test_data, train_label, test_label = train_test_split(data, label, test_size=0.2, random_state=5)
train_label = train_label.values.ravel()

model = LogisticRegression(solver='saga', max_iter=7500)

model.fit(train_data, train_label)

test_predict = model.predict(test_data)
score = model.score(test_data, test_label)

# 테스트 코드
print(test_predict, score)