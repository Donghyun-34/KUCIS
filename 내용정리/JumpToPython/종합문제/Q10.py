"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 14일 화요일
내용 : 사칙연산 계산기
"""


class Calculator:

    def __init__(self, num_list):
        self.num_list = num_list
        self.list_len = len(num_list)

    def sum(self):
        sum = 0
        for i in self.num_list:
            sum += int(i)
        return sum

    def avg(self):
        sum = self.sum()
        return sum/self.list_len


cal1 = Calculator([1, 2, 3, 4, 5])

print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6, 7, 8, 9, 10])

print(cal2.sum())
print(cal2.avg())