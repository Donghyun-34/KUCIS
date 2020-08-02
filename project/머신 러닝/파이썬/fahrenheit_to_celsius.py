# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    # 코드를 입력하세요.
    celsius_list = []
    for i in range(0, len(fahrenheit)):
        c_temp = ((fahrenheit[i]-32)*5)/9
        celsius_list.append(c_temp)

    return celsius_list

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

temperature_list = fahrenheit_to_celsius(temperature_list)
celsius_list = []
for i in range(0, len(temperature_list)):
    celsius_list.append(round(temperature_list[i], 1))

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
print("섭씨 온도 리스트: " + str(celsius_list))  # 섭씨 온도 출력
