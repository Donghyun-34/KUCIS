def survival_classifier(seat_belt, highway, speed, age):
    # 코드를 쓰세요
    if seat_belt == True:
        return 0
    elif highway == False:
        return 0
    elif speed < 100:
        return 0
    elif age < 50:
        return 0
    else:
        return 1


print(survival_classifier(False, True, 110, 55))
print(survival_classifier(True, False, 40, 70))
print(survival_classifier(False, True, 80, 25))
print(survival_classifier(False, True, 120, 60))
print(survival_classifier(True, False, 30, 20))