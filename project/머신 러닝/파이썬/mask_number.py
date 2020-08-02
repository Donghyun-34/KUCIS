import re

def mask_security_number(number):
    # 코드를 입력하세요.
    security_number = re.compile(r"(\d{6}[-]?\d{3})\d{4}")
    return security_number.sub("\g<1>****", number)


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))