"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 13일 월요일
내용 : 리스트의 더하기와 extend 함수
"""
a = [1, 2, 3]
origin_address = id(a)

a = a + [4, 5]
plus_address = id(a)

print('a 리스트의 원래 주소는 %d이고 + 이후의 주소는 %d 이다.\n\n' % (origin_address, plus_address))

b = [1, 2, 3]
origin_address = id(b)

b.extend([4, 5])
extend_address = id(b)

print('b 리스트의 원래 주소는 %d이고 extend 이후의 주소는 %d 이다.\n\n' % (origin_address, extend_address))
"""
위의 결과를 통해 알 수 있는 점은 다음과 같습니다.
리스트의 + 연산은 두 개의 리스트를 더한 새로운 리스트를 반환하는 반면,
extend 함수의 경우에는 원래의 리스트에 추가할 내용을 추가하는 함수라는 것을 알 수 있습니다.
"""