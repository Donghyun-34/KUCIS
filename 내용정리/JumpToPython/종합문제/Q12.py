"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 14일 화요일
내용 : 오류와 예외 처리
결과 분석 : 11번 줄에서 정의되어 있지 않은 인덱스로 접근([1,2,3]은 0~2번의 인덱스를 보유)하고 있기
때문에 여기서 바로 IndexError가 발생해서 except IndexError로 이동하기 때문에 + 3이 수행되고
다음으로 finally로 이동하기 때문에 위의 두 except는 실행 되지 않기 때문이다.
"""
result = 0

try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError as e:
    print(e)
    result += 1
except ZeroDivisionError as e:
    print(e)
    result += 2
except IndexError as e:
    print(e)
    result += 3
finally:
    result += 4

print(result)