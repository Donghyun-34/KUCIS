import pandas as pd

df = pd.read_csv('laptops.csv')

# 큰 데이터프래임의 Series 다루기 연습

print(df['brand'])

# 중복 값 삭제
print(df['brand'].unique())

# 각 요소들의 등장 횟수 계산
print(df['brand'].value_counts())

# 특정 Series에 대한 요약 정보 확인
print(df['brand'].describe())