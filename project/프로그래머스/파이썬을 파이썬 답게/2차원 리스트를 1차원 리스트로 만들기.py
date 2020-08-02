def solution(mylist):
    """
    Version 1. itertools.chain()
    answer = list(itertools.chain(*mylist))
    print(answer)
    """

    """
    Version 2. itertools.chain.from_iterable()
    answer = list(itertools.chain.from_iterable(mylist))
    print(answer)
    """

    """
    Version 3. list comprehension
    answer = [ y for x in mylist for y in x]
    print(answer)
    """

    """
    Version 4. sum()
    """
    answer = sum(mylist, [])
    print(answer)

solution([['A', 'B'], ['X', 'Y'], ['1']])
"""
다양한 방법이 존재하는데 그 중 몇가지를 정리하면 다음과 같다.
1. itertools.chain()
    : 파이썬의 표준 라이브러리 중 하나인 itertools를 사용한다.
        - itertools.chain() : 인자로 받은 iterator들의 원소를 연결해서 반환해준다.
            > 이때 인자로 이차원 리스트를 바로 전달하면 단순히 하나의 iterator로 인식되므로 입력값이 그대로 반환된다.
            > 그렇기 때문에 *를 이용해서 Unpacking을 해주어야 한다.
2. itertools.chain.from_iterable()
    : 1의 방법은 매번 인자의 형태를 신경써서 언팩킹의 필요 유무를 판단해야 한다는 단점이 존재하고, 이를 해결하기 위한 방법이
    2의 방법이다.
        - from_iterable() : 인자로 들어온 iterator의 요소들을 하나하나 분해해서 반환해준다.
3. list comprehension
    : 컴프리헨션을 활용해서 해결하는 것인데 가독성이 그렇게 좋지는 않다.
        - 사용 예시 : [y for x in list for y in x]
        - 해석
            > 앞의 for x in list 먼저 실행된다. : 리스트의 각 요소들을 x에 담는다.
            > 이후 for y in x가 실행된다. : 즉, 앞의 구문에서 추출한 각 요소들을 리스트의 요소로 삽입한다.
4. sum()
    : sum() 함수는 원래 sum(iterable[, start])의 형태를 띄고있고, start와 iterable의 요소를 더해 반환하는 함수이다.
    기본적으로 sum([1, 2, 3, 4])와 같은 형태로 사용되며 의미는 다음과 같다.
        - start는 디폴트 값으로 0이 되고, 1, 2, 3, 4를 더한 결과를 반환한다.
        - 위에서 처럼 2차원 리스트를 1차원 리스트로 합칠 때 사용할 때는 위처럼 사용하면 오류가 발생한다.
            > 발생하는 오류 = TypeError : unsupported operand type(s) for +: 'int' and 'list'
            > 발생 원인 : sum의 디폴트 start 값이 0이기 때문에, start 값을 따로 지정해주지 않으면 0 + list가 되는것이다.
            > 해결 방법 : 그렇기 때문에, list를 대상으로 sum을 할 때는 추가적으로 []를 start로 지정해 주어야 한다.

5. Numpy
    : 외부 라이브러리인 Numpy를 사용하는 방식으로 주어진 인자를 ndarray 객체로 바꾸어서 사용한다.
        - reshape(x, y) 메서드 : 배열의 차원을 변경할 때 사용하는 메소드이다.
            > x : low의 크기 지정
            > y : column의 크기 지정
            > x나 y에 -1이 있는 경우 : -1이 아닌 값에 따라 가변적으로 결정된다는 의미.
                >> -1이 아닌 나머지 값을 기반으로 해서 전체 요소를 다 표현할 수 있는 값으로 자동 설정 된다.
                >> 전체 요소가 12인 경우 적용 예시
                    >>> x = -1, y = 3 -> x = 4
                    >>> x = -1, y = 6 -> x = 2
                    >>> x = 3, y = -1 -> y = 4
                    >>> x = 2, y = -1 -> y = 6
        - flatten() 메서드 : 다차원 배열을 1차원 배욜로 변환 해준다.
"""