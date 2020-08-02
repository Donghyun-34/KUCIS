"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 14일 화요일
내용 : 피보나치 함수
사용 기법 : 큰 순번의 피보나치 수 까지 검색하기 위해서 동적 프로그래밍의 메모이제이션 기법을 활용.
"""
print("해당 프로그램의 최대 범위를 입력하세요 : ")
MAX_RNAGE = int(input())

data = [0 for i in range(MAX_RNAGE+1)] # 캐싱을 할 저장 공간


try:
    def fibo(n):
        if n <= 2:
            return 1
        elif data[n] != 0:
            return data[n]
        else:
            data[n] = fibo(n - 1) + fibo(n - 2)
            return data[n]


    print("몇 번째 피보나치 수가 궁금한가요 : ")
    num = int(input())

    print(fibo(num))
except IndexError as e:
    print("해당 프로그램의 최대 범위는 %d번째 피보나치 수 까지 입니다!!!!!" %MAX_RNAGE)