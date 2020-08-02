# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
num_list = [1, 7, 3, 6, 5, 2, 13, 14]
# 코드를 입력하세요
for i in num_list:
    numbers.append(i)
print(numbers)

# numbers에서 홀수 제거
# 코드를 입력하세요
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        del numbers[i]
    else:
        i += 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
# 코드를 입력하세요
numbers.sort()
print(numbers)
