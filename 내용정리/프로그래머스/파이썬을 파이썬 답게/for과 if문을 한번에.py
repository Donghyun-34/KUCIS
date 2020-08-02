def solution(mylist):
    answer = [x**2 for x in mylist if x % 2 == 0]
    return answer

print(solution([3, 2, 6, 7]))