"""
만든 사람 : 김동현
만든 날짜 : 2020.07.16
내용 : 텍스트 파일에서 내용을 읽어와서 금액을 구분하고 일 평균 매출액 계산
특이점
1. 파일에서 내용을 읽어 올때 strip을 이용해서 공백과 개행문자 제거
2. split을 이용해서 "날짜: 금액" 형식으로 입력 된 값을 구분
"""
money = 0
day = 0

with open("chicken.txt", "r", encoding="UTF8") as f:
    for line in f:
        money += int((line.strip().split(": ")[1]))
        day += 1

print(money//day)  # // : 몫만 표시하고자 사용
