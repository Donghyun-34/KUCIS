"""
만든 사람 : 김동현
만든 날짜 : 2020.07.16
내용 : 사용자의 입력 값을 파일에 입력
"""
with open("Vocabulary/vocabulary.txt", "w", encoding="UTF8") as f:
    while 1:
        eng = input("영어 단어를 입력하세요: ")
        if eng == 'q':
            exit()
        kor = input("한국어 뜻을 입력하세요: ")
        if kor == 'q':
            exit()
        f.write(eng + ': ' + kor + '\n')