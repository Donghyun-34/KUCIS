"""
점프 투 파이썬 06장 메모장 만들기
만든이 : 김동현
만든 날짜 : 2020년 07월 13일 월요일
교제에서 요구한 기능
1. 메모 추가하기
2. 메모 조회하기(검색하기)
스스로 추가한 기능
1. 메모장 선택하기
"""
import sys

f_name = sys.argv[1]
option = sys.argv[2]
memo = sys.argv[3]

if option == '-a':
    f = open(f_name, 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open(f_name, 'r')
    memo = f.read()
    print(memo)
    f.close()

