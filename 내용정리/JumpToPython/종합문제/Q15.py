"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 14일 화요일
내용 : Duplicate Numbers
"""
def dup_num(num):
    result = []

    for n in num:
        if n in result:  # 중복되는 숫자가 나오는 순간 False 반환
            return False
        result.append(n)

    return len(result) == 10  # 중복되는 숫자가 없었다 하더라도, 0~9 사이의 모든 수가 있어야 True 반환


print(dup_num("0123456789"))
print(dup_num("01234"))
print(dup_num("01234567890"))
print(dup_num("6789012345"))
print(dup_num("012322456789"))