"""
점프 투 파이썬 연습문제 03장
만든이 : 김동현
만든 날짜 : 2020년 07월 11일 토요일
"""
"""
=============================Q1문제 코드 결과값 분석
"""
print("\n1번째 문제\n")
a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

"""
=============================Q2문제 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자.
"""
print("\n2번째 문제\n")
sum = 0
a = 1

while a < 1001:
    if a % 3 == 0:
        sum += a
    a += 1

print(sum)

"""
=============================Q3문제 while문을 사용해 별 찍기를 하시오.
"""
print("\n3번째 문제\n")
a = 1

while a < 6:
    print('*' * a)
    a += 1

"""
=============================Q4문제 for문을 사용해 1부터 100까지의 숫자를 출력하시오
"""
print("\n4번째 문제\n")

for a in range(1, 101):
    print(a, end=" ")

"""
=============================Q5문제 for문을 사용하여 A 학급의 평균 점수를 구해 보자.
"""
print("\n5번째 문제\n")

list = [70, 60, 55, 75, 95, 90, 80, 85, 100]
sum = 0

for a in range(0, len(list)):
    sum += list[a]

print(sum/len(list))

"""
=============================Q6문제 다음의 코드를 리스트 내포로 표현하시오
"""
"""
                numbers = [1, 2, 3, 4, 5]
                result = []
                for n in numbers:
                    if n % 2 == 1:
                        result.append(n*2)
"""
print("\n6번째 문제\n")

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 ==1]

print(result)