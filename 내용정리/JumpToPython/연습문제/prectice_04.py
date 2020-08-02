"""
점프 투 파이썬 연습문제 04장
만든이 : 김동현
만든 날짜 : 2020년 07월 11일 토요일
"""
"""
=============================Q1문제 홀짝 판별
"""
print("\n1번째 문제\n")


def is_add(a):
    if a % 2 == 0:
        print("%d는 짝수입니다\n" %a)
    else:
        print("%d는 홀수입니다\n" %a)


is_add(4)
is_add(9)
"""
=============================Q2문제 입력 값의 평균 값을 계산해주는 함수 구현 -> 입력 값의 개수는 제한이 없고, 평균을 구할 때 len 함수 활용
"""
print("\n2번째 문제\n")


def cal_average(*args):
    sum = 0
    for a in args:
        sum += a
    ave = sum/len(args)
    print(ave)


cal_average(90, 85, 95, 79, 80)

"""
=============================Q3문제 형변환을 사용해서 오류 수정하자
"""
print("\n3번째 문제\n")

input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)

"""
=============================Q4문제 문자열 출력 방식 비교
"""
print("\n4번째 문제\n")

print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python") # ,를 사용하면 출력 값 사이에 space가 출력된다.
print("".join(["you", "need", "python"]))

"""
=============================Q5문제 test.txt 파일에 문자열 저장 후 다시 읽어와서 출력하기
"""
print("\n5번째 문제\n")

f1 = open("test1.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test1.txt", 'r')
print(f2.read())

"""
=============================Q6문제 사용자의 입력을 파일에 저장하는 프로그램(a 속성 사용)
"""
print("\n6번째 문제\n")

f = open("text.txt", 'a')
f.write(input())
f.close()

"""
=============================Q7문제 파일 내용 중 특정 문자열 변경 - replace 함수 활용
"""
print("\n7번째 문제\n")

f = open("test2.txt", 'r')

list = f.readlines()
f.close()

f = open("test2.txt", 'w')
for a in list:
    a = a.replace("java", "python")
    f.write(a)