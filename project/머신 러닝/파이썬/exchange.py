# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    # 코드를 입력하세요.
    # 환율 : 1달러 = 1000원
    usd_amount = []
    for i in krw:
        usd_amount.append(i/1000)
    return usd_amount


# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    # 코드를 입력하세요.
    # 환율 : 1,000엔 = 8달러
    jpy_amount = []
    for i in usd:
        jpy_amount.append((i/8)*1000)
    return jpy_amount


# 원화(￦)으로 각각 얼마인가요?
amounts = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(amounts))

# amounts를 원화(￦)에서 달러($)로 변환하기
# 코드를 입력하세요.

# 달러($)로 각각 얼마인가요?
usd_mnt = krw_to_usd(amounts)
print("미국 화폐: " + str(usd_mnt))

# amounts를 달러($)에서 엔화(￥)으로 변환하기
# 코드를 입력하세요.

# 엔화(￥)으로 각각 얼마인가요?
jpy_mnt = usd_to_jpy(usd_mnt)
print("일본 화폐: " + str(jpy_mnt))