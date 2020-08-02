import pandas as pd


pf = pd.read_csv('iphone.csv', index_col=0)
pf.loc['iPhone 7':'iPhone X'] = '0'
pf.iloc[[1, 3], [2, 4]] = '1'


# 데이터 프래임에 값 변경/추가/삭제

    # 변경
pf.loc['iPhone 8', '디스플레이'] = 4.4
pf.loc['iPhone 8'] = ['2020-07-21', '4.4', '3GB', 'iOS 13.0', 'Yes']

    # 새로운 값 추가
pf.loc['iPhone XR'] = ['2020-07-21', '4.4', '3GB', 'iOS 13.0', 'Yes']

    # 값 삭제
pf.drop('iPhone XR', axis='index', inplace=False)

"""
이때 inplace 값에 따라 원본에 저장 여부를 결정 할 수 있다.
False : 원본에 저장 하지 않음
True : 원본에 저장
"""

pf.drop(['iPhone 7', 'iPhone XR'], axis='index', inplace=True)

# 데이터 프래임의 index/column 설정하기

df = pd.read_csv('liverpool.csv', index_col=0)
    # column의 이름 변경
df.rename(columns={'position': 'Position', 'born':'Born'}, inplace=True)

    # index의 이름 변경
df.index.name = 'Player Name'

    # index와 column 서로 바꾸기
df.set_index('Position', inplace=True)
"""
set_index를 사용해서 index 값을 변경하기 전에 주의해야 할 점
1. 변경 전의 내용은 그냥 사라지기 때문에 해당 내용을 계속 하고자 하면 미리 따로 저장을 해놓거나 DF에 추가해놓아야 한다.
"""
print(df)
print(df.index)