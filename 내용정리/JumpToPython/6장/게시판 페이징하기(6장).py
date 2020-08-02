"""
점프 투 파이썬 06장 게시판 페이징 하기
만든이 : 김동현
만든 날짜 : 2020년 07월 13일 월요일
"""


def getTotalPage(n, m):
    if n % m == 0:
        return int(n/m)
    return int(n/m + 1)


print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))
