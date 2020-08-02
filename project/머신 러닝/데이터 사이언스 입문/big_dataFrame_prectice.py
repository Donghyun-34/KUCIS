import pandas as pd

df = pd.read_csv('laptops.csv')

# 앞에서부터 원하는 만큼 잘라서 보기
print(df.head(4))
print(df.head(20))

# 뒤에서부터 원하는 만큼 잘라서 보기
print(df.tail(4))
print(df.tail(20))

# DataFrame의 크기 분석
print(df.shape)
"""
shape의 결과 중 앞의 수가 총 row 수, 뒤의 수가 column의 수이다.
"""

# DataFrame의 column의 종류 확인하기
print(df.columns)
print(df.info()) # 각 column의 상세 정보 확인

# DataFrame의 column들의 통계값 확인하기
print(df.describe())

# DataFrame의 row를 원하는 기준으로 정렬하기
df.sort_values(by='price', ascending=False, inplace=True)
"""
sort_values의 속성 설명
1. by : 정렬의 기준 값 설정
2. ascending : 오름차순, 내림차순 설정
    1) False : 내림차순
    2) True : 오름차순
3. inplace : 원본의 값 자체를 바꿀 지 안 바꿀지 결정
    1) False : 원본에는 영향 X -> 결과 값을 계속 사용하고자 하면 따로 저장 필요
    2) True : 원본 자체를 변경
"""
print(df)