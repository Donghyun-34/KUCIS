"""
점프 투 파이썬 06장 하위 디렉터리 검색하기
만든이 : 김동현
만든 날짜 : 2020년 07월 13일 월요일
"""
import os

for (path, dir, files) in os.walk("c:/Users\82102\AppData\Local"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))