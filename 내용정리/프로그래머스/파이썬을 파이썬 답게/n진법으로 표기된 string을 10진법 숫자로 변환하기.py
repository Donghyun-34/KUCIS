def Conversion():
    """ Version 1 : 앞에서 부터 계산
    num, base = map(int, input().strip().split(' '))

    sum = 0

    num_str = str(num)
    cnt = base ** (len(num_str)-1)
    for i in num_str:
        sum += int(i) * cnt
        cnt //= base

    print(sum)
    """

    """ Version 2 : 뒤에서 부터 계산
    num, base = map(int, input().strip().split(' '))

    sum = 0
    cnt = 1

    num_str = str(num)
    for idx, i in enumerate(num_str[::-1]):
        sum += int(i) * (base ** idx)
    
    print(sum)
    """
    # Version 3 : 파이썬의 int(x, base) 함수 활용
    num, base = map(int, input().strip().split(' '))

    print(int(str(num), base))

Conversion()

"""
int(x, base) : base 진법으로 주어진 x를 10진법으로 변환해서 반환해준다.
"""