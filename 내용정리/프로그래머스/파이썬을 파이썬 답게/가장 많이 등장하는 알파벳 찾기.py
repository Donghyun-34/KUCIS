import collections

my_str = list(input().strip())
answer1 = collections.Counter(my_str).most_common()

result = list(answer1[0][0])
max_cnt = answer1[0][1]

for word, cnt in answer1[1:]:
    if cnt < max_cnt:
        break
    result.append(word)

result.sort()

print("".join(result))

"""
collections의 Counter 클래스를 이용해서 각 알파벳들의 등장 빈도수를 체크했다.
1. collections.Counter().most_common() : 빈도 수 가 가장 큰 단어 순으로 정렬해서 ('문자', 빈도 수) 형으로
반환해주는 함수
"""