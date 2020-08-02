"""
만든 사람 : 김동현
만든 날짜 : 2020.07.16
내용 : 1~20 사이의 렌덤한 숫자를 맞추는 게임
특징
1. 남은 기회를 매번 출력 해준다.
2. 정답을 맞추면 몇번만에 맞추었는지 출력한다.
3. 사용자의 입력이 정답보다 큰지 작은지를 Up과 Down으로 알려준다.
4. 기회를 전부 소진하면 정답을 알려주고 프로그램을 종료한다.
"""
import random

answer = random.randint(1, 20)
life = 4
try_cnt = 0

for _ in range(4):
    num = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: ".format(life)))
    life -= 1
    try_cnt += 1
    if num < answer:
        print("Up")
    elif num > answer:
        print("Down")
    else:
        print("축하합니다. {}번만에 숫자를 맞추셨습니다.".format(try_cnt))
        exit()
print("아쉽습니다. 정답의 {}였습니다.".format(answer))