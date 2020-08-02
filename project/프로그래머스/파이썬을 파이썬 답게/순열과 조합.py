import itertools

def solution(mylist):
    mylist.sort()
    answer1 = list(map(list, itertools.permutations(mylist)))
    print(answer1)
    answer1 = list(map(list, itertools.combinations(mylist, 2)))
    print(answer1)

solution([1, 2, 3])

"""
파이썬에서 순열과 조합을 다루기 위해서는 itertools의 permutations와 conbinations를 사용하면 된다.

1. 순열 : permutations
    - 순서를 중요시 하는, 즉 값의 중복을 허용하는 순열을 생성한다.
    
2. 조합 : conbinations
    - 순서를 상관하지 않는, 즉 순서만 다르고 값들은 동일한 경우 같은 것으로 치부하고 중복을 제거한 조합을 생성해준다. 
    이때 반드시 조합의 크기를 지정해주어야 한다. -> 안주면 에러 발생
    - 발생 에러 : TypeError
        > 발생 원인 : combinations 함수는 길이에 대한 default 설정을 해놓지 않아서 호출 시 
        전달해주지 않으면 빈 값이 되므로 오류가 발생한다.
"""