import math
res = 1
for _ in range(5):
    a = int(input())
    res *= a
    if math.sqrt(res) == int(math.sqrt(res)):
        print("found")
        exit()
print("not found")

"""
for문에서 _의 의미 : 아무 의미 없이 반복만 수행한다는 의미
"""