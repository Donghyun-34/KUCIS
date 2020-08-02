"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 13일 월요일
내용 : 리스트의 더하기와 extend 함수
"""
import re

p = re.compile("[a-z]+")
# [a-z]+ 는 소문자로 이루어진 단어를 의미한다.

m = p.search("5 python")
# search는 주어진 문자열 중에서 정규 표현식과 매치되는 정보(match되는 인덱스, match되는 단어)를 반환한다.

m.start() + m.end()