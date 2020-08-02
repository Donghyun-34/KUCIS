"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 13일 월요일
내용 : 딕셔너리 값 추출하기 + Error Handling
"""

# Version1 Error Handling
try:
    a = {'A': 90, 'B': 80}

    a['C']

except KeyError:
    a['C'] = 70
    print(a['C'])

# Version2 딕셔너리 get 함수 활용
b = {'A': 90, 'B': 80}

print(b.get('C', 70))
"""
딕셔너리의 get 함수는 첫번째 인자에 해당하는 값이 딕셔너리 객체에 존
재하면 해당 key의 value를 반환하지만, 없으면 두번째 인자로 전달해준 default 값을 반환한다.
"""