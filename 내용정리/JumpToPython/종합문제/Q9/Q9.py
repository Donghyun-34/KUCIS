"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 14일 월요일
내용 : 평균값 구하기 -> 파일 입출력 이용
"""
try:
    f1 = open("sample.txt", 'r')
    list = f1.readlines()
    f1.close()

    sum = 0
    for num in list:
        sum += int(num)

    f2 = open("result.txt", 'w')
    f2.write(str(sum))
    f2.close()

except ValueError as e:
    print("파일의 내용 중에 숫자가 아닌 내용이 들어있습니다.")