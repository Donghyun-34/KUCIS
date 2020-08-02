"""
만든 사람 : 김동현
만든 날짜 : 2020.07.16
내용 : 외부 파일에서 단어의 뜻을 가져와서 영단어를 맞추는 단어 게임 만들기
특이점
1. 원래는 순차적으로 읽어와서 퀴즈를 내는 문제였지만 퀴즈라는 주제에 맞추어 랜덤성을 추가하였습니다.
    (1) random 모듈 사용
        1) random.sample(x, y) : 반복 가능한 객체 x에서 y만큼의 값을 무순서하게 가져온다.
            1. 각 값에는 Unique가 보장된다. -> 중복이 없다.
            2. 추출의 대상이 되는 객체의 값은 변화지 않는다.
            3. 새로운 리스트가 반환된다.
        2) random.suffle(x) : x의 요소들을 무작위하게 섞어준다.
            1. 요소들을 변경할 수 있어야 하기 때문에 반드시 리스트 형이 대상이 되어야한다.
            2. 대상 리스트의 값 자체가 변화된다.
"""
import random

with open("Vocabulary/vocabulary.txt", "r", encoding="UTF8") as f:
    word = []
    mean = []
    for line in f.readlines():
        word.append(line.strip().split(': ')[0])
        mean.append(line.strip().split(': ')[1])

    list = [i for i in range(0, len(word))]

    # Version 1 : random.sample 사용 -> 반환형 있음
    # Version 2 : random.suffle 사용 -> 반환 X, 대상 리스트 자체 값이 변환
    while 1:
        for i in random.sample(list, len(word)):
            ans = input("%s: " % mean[i])
            if ans == word[i]:
                print("맞았습니다!\n")
            elif ans == 'q':
                exit()
            else:
                print("아쉽습니다. 정답은 %s입니다.\n" % word[i])