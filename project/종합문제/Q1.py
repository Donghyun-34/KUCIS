"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 13일 월요일
내용 : 문자열 바꾸기
"""
source_str = "a:b:c:d"

t_list = source_str.split(":")
"#".join(t_list)
print("#".join(t_list))

"""
활용
"""
print("변경하고자 하는 문자열을 입력해주세요 : ")
source_str = input()

print("구분자와 변경하고자 하는 구분자를 입력하세요 : ")
token = input()
t_token = token.split(' ')

t_list = source_str.split(t_token[0])

print(t_token[1].join(t_list))
