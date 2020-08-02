"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 14일 화요일
내용 : DashInsert 함수 -> 숫자로 구성된 문자열을 입력받은 뒤
문자열 안에서 홀수가 연속되면 두 수 사이에 -를 추가하고, 짝수가 연속되면 *를 추가하는 기능을 갖고 있다.
"""
num = "4546793"
num_list = list(map(int, num))  # 이후 연산에서 편의를 위해서 숫자 문자열을 숫자 리스트로 변경
res_str = ""

for cnt, number in enumerate(num_list):
    res_str += str(number)
    if cnt < len(num_list)-1:
        num_is_odd = (num_list[cnt] % 2 == 1)  # 현재 수가 홀순지 짝순지 판단(홀수면 True, 짝수면 False)
        next_num_is_odd = (num_list[cnt+1] % 2 == 1)  # 다음 수가 홀순지 짝순지 판단(홀수면 True, 짝수면 False)
        if num_is_odd and next_num_is_odd:
            res_str += "-"
        elif not num_is_odd and not next_num_is_odd:
            res_str += "*"

print(res_str)