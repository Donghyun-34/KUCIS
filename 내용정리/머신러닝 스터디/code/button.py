from Maix import GPIO
import time

btn_time = 0

def btn_function(pin_num):
    current_time = time.ticks()
    global btn_time
    # print(current_time - btn_time)
    if (current_time - btn_time) >= 500:
        print("버튼이 눌렸습니다.")
        btn_time = time.ticks()

fm.register(8, fm.fpioa.GPIOHS0)
btn = GPIO(GPIO.GPIOHS0, GPIO.IN)

btn.irq(btn_function, GPIO.IRQ_RISING)
