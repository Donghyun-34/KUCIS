def solution(mylist):
    """
    Version C
    answer = []
    for i in mylist:
        answer.append(len(i))

    return answer
    """
    # Version Python
    return list(map(len, mylist))
# map : 첫번째 인자로 주어진 함수에 두 번째 인자로 주어진 값을 반복적으로 대입해서 결과값 반환

print(solution([[1, 3, 4, 5], [1, 2]]))