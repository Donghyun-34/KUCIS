import sensor, image, lcd, time
from Maix import GPIO
import KPU as kpu

from machine import Timer,PWM

# there are 3 timers and each timer has 4 channels
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
S1 = PWM(tim, freq=50, duty=0, pin=12)
tim2 = Timer(Timer.TIMER0, Timer.CHANNEL1, mode=Timer.MODE_PWM)
S2 = PWM(tim2, freq=50, duty=0, pin=13)

# 4.25 < a < 13 / 5.25 < b < 9.25
def servoPosition(a, b):
    if a < 4.25:
        a = 4.25
    if a > 13:
        a = 13
    if b < 5.25:
        b = 5.25
    if b > 9.25:
        b = 9.25

    S1.duty(a)
    S2.duty(b)

servopos1 = 7.5
servopos2 = 7.5
servoPosition(servopos1, servopos2)

def pos(x, y):
    global servopos1
    global servopos2

    if x > 180:
        servopos1 = servopos1  + 0.1
    if x < 140:
        servopos1 = servopos1  - 0.1
    if y > 135:
            servopos2 = servopos2  + 0.1
    if y < 105:
            servopos2 = servopos2  - 0.1
    servoPosition(servopos1, servopos2)

btn_time = 0

def btn_function(pin_num):
    current_time = time.ticks()
    global btn_time
    # print(current_time - btn_time)
    if (current_time - btn_time) >= 500:
        btn_time = time.ticks()

fm.register(8, fm.fpioa.GPIOHS0)
btn = GPIO(GPIO.GPIOHS0, GPIO.IN)




lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
task = kpu.load(0x500000) # you need put model(face.kfpkg) in flash at address 0x500000
# task = kpu.load("/sd/face.kmodel")
a = kpu.set_outputs(task, 0, 20, 15, 30)
anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
a = kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)
while(True):
    btn.irq(btn_function, GPIO.IRQ_RISING)
    img = sensor.snapshot()
    code = kpu.run_yolo2(task, img)
    if code:
        for i in code:
            print(i)
            a = img.draw_rectangle(i.rect())
            pos(i.x()+i.w()/2, i.y()+i.h()/2)
    a = lcd.display(img)
a = kpu.deinit(task)
