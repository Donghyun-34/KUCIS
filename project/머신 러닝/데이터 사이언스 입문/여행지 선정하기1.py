import pandas as pd

world_df = pd.read_csv('world_cities.csv', index_col=0)

# 1번. 총 몇 개의 도시와 몇 개의 나라가 있는지 알아맞혀 보세요.
print(world_df['City / Urban area'].describe())
print(world_df['Country'].describe())

# 2번. 인구 밀도(명/sqKm) 가 10000 이 넘는 도시는 총 몇 개인지 알아보세요.
world_df['인구 밀도'] = world_df['Population']/world_df['Land area (in sqKm)']
print(world_df[world_df['인구 밀도']>10000].info())

# 3번. 인구 밀도가 가장 높은 도시를 찾아봅시다.
print(world_df.sort_values(by='인구 밀도', ascending=False).head(1))

# 2_1번. 4개의 도시를 가지고 있는 국가 찾기
count = world_df['Country'].value_counts()
print(count[count == 4])