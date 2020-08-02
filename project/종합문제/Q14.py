"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 14일 화요일
내용 : 문자열 압축하기 -> 문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우에
그 반복 횟수를 표시해 문자열을 압축하여 표시하시오.
"""
""" Version 1 : 시작 문자를 공백으로 시작
s = input()

char = ""
cnt = 0
result = ""

for comp_char in s:
    if char != comp_char:
        char = comp_char
        if cnt:  # 문자열의 첫 번째 문자인 경우에 대한 예외 처리
            result += str(cnt)
        result += comp_char
        cnt = 1
    else:
        cnt += 1

if cnt:
    result += str(cnt)

print(result)
"""

# Version 2 : 시작 문자를 문자열의 첫 문자로 시작
s = input()

char = s[0]
cnt = 1
result = ""

for comp_char in s[1:]:
    if char != comp_char:
        result += char
        char = comp_char
        result += str(cnt)
        cnt = 1
    else:
        cnt += 1

if cnt:
    result += char
    result += str(cnt)

print(result)