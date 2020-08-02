def cal():
    a, b = map(int, input().strip().split(' '))
    result = f"{a // b} {a % b}"
    print(result)
    print(*divmod(a, b))

cal()

"""
divmod : 몫과 나머지를 튜플 형태로 반환해준다.
// : 몫을 정수형으로 반환, / : 몫을 실수형으로 반환
* : 다양한 역할이 있지만 여기서는 unpacking의 역할을 한다.
    튜플이나 리스트 등의 괄호를 제거하고 반환
"""