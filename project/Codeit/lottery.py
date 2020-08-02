"""
만든 사람 : 김동현
만든 날짜 : 2020.07.16
내용 : 로또 프로그램
"""
import random


def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        num = random.randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers


def draw_winning_numbers():
    w_num = generate_numbers(7)

    return sorted(w_num[:6]) + w_num[6:]


def count_matching_numbers(list1, list2):
    lens = len(set(list1).intersection(list2[:6]))
    bouns_lens = len(set(list1).intersection(list2[6:]))
    return lens, bouns_lens


def check(list1, list2):
    price = 0
    same_num, bouns = count_matching_numbers(list1, list2)
    if same_num == 3:
        price = 5000
    elif same_num == 4:
        price = 50000
    elif same_num == 5:
        if bouns == 0:
            price = 1000000
        else:
            price = 50000000
    elif same_num == 6:
        price = 1000000000
    else:
        price = 0

    return price