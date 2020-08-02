"""
만든 사람 : 김동현
만든 날짜 : 2020.07.17
내용 : 숫자 야구
특이점
1. 0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑는다.
2. 숫자 3개를 하나씩 순서대로 입력 받는다.
3. 횟수의 제한은 없으나 몇 번만에 맞추었는지가 출력되어야 한다.
"""
import random


def generate_numbers():
    tmp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return random.sample(tmp, 3)


def take_guess():
    user_input = []

    cnt = 1
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    while len(user_input) < 3:
        try:
            num = int(input("%d번째 숫자를 입력하세요: " % cnt))
        # 공백 또는 숫자가 아닌 입력 값이 들어온 경우에 대한 예외 처리
        except ValueError as e:
            print("숫자가 아닌 다른 값을 입력 하였습니다. 숫자만 입력해 주시기 바랍니다.")
            continue

        if num in user_input:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            continue
        elif num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        else:
            user_input.append(num)
            cnt += 1

    return user_input


def get_score(guess, solution):
    str_cnt = 0
    bal_cnt = 0

    for i in guess:
        if i in solution:
            if guess.index(i) == solution.index(i):
                str_cnt += 1
            else:
                bal_cnt += 1

    return str_cnt, bal_cnt


Answer = generate_numbers()
try_cnt = 0

while 1:
    user_guess = take_guess()
    str_res, bal_res = get_score(user_guess, Answer)
    print("%dS %dB\n" % (str_res, bal_res))
    try_cnt += 1
    if str_res == 3:
        print("축하합니다. %d번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다." % try_cnt)
        exit()
