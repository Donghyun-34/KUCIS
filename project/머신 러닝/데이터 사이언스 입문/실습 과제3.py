"""
실습과제3 : 강의실 배정하기2
"""
import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

# 코드를 작성하세요.
df.rename(columns={'room assignment' : 'room number'}, inplace=True)

room_name = list(df['room number'].unique())
room_name.sort()
sort_list = []

for i, name in enumerate(room_name):
    list1 = (df['room number'] == name)
    list2 = df[list1]
    sort_list.append(list(list2['course name'].unique()))
    sort_list[i].sort()

change_name = ['Auditorium', 'Large', 'Medium', 'Small']
change_name.sort()
for i in range(0, len(room_name)-1):
    for cnt, name in enumerate(sort_list[i]):
        df.loc[df['course name'] == name, 'room number'] = (change_name[i] + '-' + str(cnt+1))
df.loc[df['status'] == 'not allowed', 'room number'] = 'not assigned'

# 정답 출력
df