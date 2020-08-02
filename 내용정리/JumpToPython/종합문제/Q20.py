"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 14일 화요일
내용 : 긍정형 전방 탐색 기법
"""
import re

pattern = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pattern.match("pahkey@gmail.com"))
print(pattern.match("kim@daum.net"))
print(pattern.match("lee@myhome.co.kr"))
"""
분석
1. .* : 모든 문자가 와도 상관없다.
2. [@], [.] : '@', '.' 문자가 있어야 한다.
3. (?=...) : ...에 해당되는 정규식과 매치되어야 한다는 으미. -> 긍정형 전방 탐색
4. com$|net$ : com으로 끝나거나 net으로 끝나야 한다는 의미 -> $가 문자열의 끝을 의미
"""