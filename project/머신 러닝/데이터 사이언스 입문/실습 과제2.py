"""
실습과제2 : 강의실 배정하기1
"""
import pandas as pd

df = pd.read_csv('data/enrolment_2.csv')

# 코드를 작성하세요.
count_Audi = (df['course name'].value_counts() >= 80)
count_LR = (df['course name'].value_counts() >= 40) & (df['course name'].value_counts() < 80)
count_MR = (df['course name'].value_counts() >= 15) & (df['course name'].value_counts() < 40)
count_SR = (df['course name'].value_counts() >= 5) & (df['course name'].value_counts() < 15)

Audi = list(count_Audi[count_Audi].index)
LR = list(count_LR[count_LR].index)
MR = list(count_MR[count_MR].index)
SR = list(count_SR[count_SR].index)
closed = df['status'] == 'not allowed'

df['room assignment'] = 'not assigned'

for i in Audi:
    df.loc[df['course name'] == i, 'room assignment'] = 'Auditorium'
for i in LR:
    df.loc[df['course name'] == i, 'room assignment'] = 'Large room'
for i in MR:
    df.loc[df['course name'] == i, 'room assignment'] = 'Medium room'
for i in SR:
    df.loc[df['course name'] == i, 'room assignment'] = 'Small room'

df.loc[closed, 'room assignment'] = 'not assigned'

# 정답 출력
df