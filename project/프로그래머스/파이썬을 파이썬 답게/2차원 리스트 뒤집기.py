def solution(mylist):
    answer = list(map(list, zip(*mylist)))
    print(answer)


mylist = [[1,2,3], [4,5,6], [7,8,9]]
solution(mylist)

"""
1. 앞에서도 사용했던 *을 사용해서 이차원 배열을 Unpacking 했다.
2. 이후 zip을 이용해서 각 요소별로 새로이 묶고, list화 시켜서 반환했다.
3. zip은 각 iterables 의 요소들을 모으는 이터레이터를 만들어주는 함수이다.
    -> 이를 활용해서, 여러 개의 Iterable을 동시에 순회할 때 사용하거나 두개의 리스트를 합쳐서 딕셔너리를 생성할 때 사용.
"""