"""
점프 투 파이썬 05장 연습
만든이 : 김동현
만든 날짜 : 2020년 07월 12일 일요일
"""
"""
class MyError(Exception):
    def __str__(self):
        return "허용되지 않은 별명입니다"

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
"""
def two_times(x):
    return x*2

print(list(map(two_times, [1, 2, 3, 4])))