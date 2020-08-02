"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 14일 화요일
내용 : 역순 저장 -> 파일 입출력 이용
"""
f1 = open("text.txt", 'r')
list = f1.readlines()
f1.close()

f2 = open("text.txt", 'w')
list.reverse()
for str in list:
    if str == "EEE":
        f2.write(str + '\n')
    else:
        f2.write(str)

f2.close()