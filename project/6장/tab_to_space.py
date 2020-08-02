"""
점프 투 파이썬 06장 탭 문자를 공백 4개로 바꾸기
만든이 : 김동현
만든 날짜 : 2020년 07월 13일 월요일

기본 형식
1. argv로 외부에서 입력 값을 받아서 소스 파일의 탭을 분석해서 탭을 전부 스페이스 4개로 
변환 후 해당 결과를 목적 파일에 저장하는 프로그램
"""
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)

f = open(dst, 'w')
f.write(space_content)
f.close()