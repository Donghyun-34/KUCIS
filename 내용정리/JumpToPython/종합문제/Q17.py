"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 14일 화요일
내용 : 기초 메타 문자
"""
import re

p = re.compile("a[.]{3,}b")

print (p.match("acccb"))    # None
print (p.match("a....b"))   # 매치 객체 출력
print (p.match("aaab"))     # None
print (p.match("a.cccb"))   # None

"""
정규 표현식에서 {x,}는 앞의 문자가 x번 이상 반복 되어야 한다는 것을 의미한다.
"""