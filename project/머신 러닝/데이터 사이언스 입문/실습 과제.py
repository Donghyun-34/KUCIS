"""
data/enrolment_1.csv가 없어서 실행은 못 시키지만 일단 코드를 저장하기 위해서 기록.
"""
import pandas as pd

df = pd.read_csv('data/enrolment_1.csv')

# 코드를 작성하세요.
df['status'] = 'allowed' # DataFrame에 새로운 column 추가
df.loc[(df['year'] == 1) & (df['course name'] == 'information technology'), 'status'] = 'not allowed'
df.loc[(df['year'] == 4) & (df['course name'] == 'commerce'), 'status'] = 'not allowed'
"""
df.loc[]를 사용하면 안에 boolean 값을 사용해서 조건에 부합되거나 부합되지 않는 값만 출력 시킬 수 가 있다.
"""
disable3 = df['course name'].value_counts() < 5
disable3_list = list(disable3[disable3].index)

for i in disable3_list:
    df.loc[df['course name'] == i, 'status'] = 'not allowed'
"""
위의 경우에는 단순히 값을 비교하는 것이 아니라 value_counts()를 이용해서 뽑아낸 Series가 비교의 대상이 되기 때문에 바로 loc에
대입할 수 없기 때문에 해당 boolean 연산의 결과를 새로운 Series 객체에 저장해주고
해당 값에서 True 값을 가지고 있는 index를 list로 변환해서 새로운 list 객체에 저장해주었다.
이후 해당 리스트 값을 이용해서 for문을 이용해서 하나하나 값을 변경해주었다.
"""
# 정답 출력
df