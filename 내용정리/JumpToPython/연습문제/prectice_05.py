"""
점프 투 파이썬 연습문제 05장
만든이 : 김동현
만든 날짜 : 2020년 07월 13일 월요일
"""
"""
=============================Q1문제 class 상속을 해보아라
"""
print("\n1번째 문제\n")

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

"""
=============================Q2문제 class 상속 활욜
"""
print("\n2번째 문제\n")

class MaxLimitCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

    def minus(self, val):
        self.value -= val
        if self.value < 0:
            self.value = 0

"""
=============================Q3문제 all과 chr 연습
"""
print("\n3번째 문제\n")

print(all([1, 2, abs(-3)-3]))
#all : 입력 값의 요소들이 모두 참이어야 True 반환, abs : 입력 값의 절대값 반환
print(chr(ord('a')) == 'a')
#chr : 입력 값에 대응되는 문자 반환, ord : 문자의 아스키 값 반환

"""
=============================Q4문제 filter와 lambda 활용헤서 리스트에서 음수 제거하기
"""
print("\n4번째 문제\n")

list_1 = [1, -2, 3, -5, 8, -3]

print(list(filter(lambda x: x>0, list_1)))

"""
=============================Q5문제 hex 사용해보기
"""
print("\n5번째 문제\n")

hex_num = hex(234)

int_num = int(0xea)

print(hex_num, int_num)

"""
=============================Q6문제 map과 lambda 활용하기
"""
print("\n6번째 문제\n")

list_2 = [1, 2, 3, 4]

print(list(map(lambda a: a*3, list_2)))
# map : 두 번째 인자로 전달 받은 입력 값을 첫번째로 전달받은 함수에 대입한 결과 값을 반환해준다.

"""
=============================Q7문제 리스트의 최대값과 최소값의 합 구하기
"""
print("\n7번째 문제\n")

list_3 = [-8, 2, 7, 5, -3, 5, 0, 1]

sum = max(list_3) + min(list_3)
# 최댓값 : 7, 최소값 : -8

print(sum)

"""
=============================Q8문제 소수 반올림(round)
"""
print("\n8번째 문제\n")

num = 17/3

print(round(num, 4))

"""
=============================Q9문제 argv 활용하기
"""
import sys

print("\n9번째 문제\n")

sum =0

for a in sys.argv:
    if a != sys.argv[0]:
        sum += int(a)

print(sum)

"""
=============================Q10문제 os 모듈 활용하기
"""
import os

print("\n10번째 문제\n")

os.chdir("C:\\Users\\82102")
dic = os.popen("dir")
print(dic.read())

"""
=============================Q11문제 glob 모듈 활용하기
"""
import glob

print("\n11번째 문제\n")

print(glob.glob("C:\\Users\\82102\\PycharmProjects\\project\\*.py"))

"""
=============================Q12문제 time 모듈 활용하기
"""
import time

print("\n12번째 문제\n")

print(time.strftime("%Y/%m/%d %H:%M:%S"))

"""
=============================Q13문제 random 모듈 활용하기
"""
import random

print("\n13번째 문제\n")
list = []
a = 0

while a < 6:
    num = random.randint(1, 45)
    if num not in list:
        list.append(num)
        a += 1

print(sorted(list))