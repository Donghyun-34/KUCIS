"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 14일 화요일
내용 : 숫자의 총합 구하기
"""
print("insert number\n")
num = input()

num_list = num.split(',')

sum = 0
for i in num_list:
    sum += int(i)

print(sum)