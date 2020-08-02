import string

def print_alpha():
    num = int(input().strip())

    if num == 0:
        print(string.ascii_lowercase)  # 소문자 abcdefghijklmnopqrstuvwxyz
    else:
        print(string.ascii_uppercase)  # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ

print_alpha()
print_alpha()

list1 = [3, 2, 1]
list2 = sorted(list1)

print(list2)
print(list1)
"""
string.ascii_letters #대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789
sorted()를 사용하면 원본은 유지한 채 새로운 정렬된 리스트를 얻을 수 있다.
-> list의 sort 메소드를 이용하면 원본 자체가 정렬 되기 때문에 원본의 순서 자체가 변경된다.
"""