"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 14일 화요일
내용 : 한 줄 구구단
"""
print("구구단을 출력할 숫자를 입력하세요 : ")
num = int(input())

for i in range(1, 10):
    print(num * i, end=" ")