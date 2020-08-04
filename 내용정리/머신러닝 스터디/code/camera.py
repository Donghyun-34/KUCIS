import sensor, image, lcd, time

# lcd 초기화 -> 필수이다!!!!
lcd.init()

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
# 화면 크기 조절
sensor.set_windowing((320, 240))
sensor.run(1)
# 상하 반전( 0 : 사용 안함, 1 : 사용 )
sensor.set_vflip(0)
# 좌우 반전( 0 : 사용 안함, 1 : 사용 )
sensor.set_hmirror(1)
# time 함수에서 clock 하나 생성1
clock = time.clock()

while True:
# 시간 측정 시작
    clock.tick()
    img = sensor.snapshot()
    # 초당 프레임 수 반환(fps = frame per second)
    fps=clock.fps()
    lcd.display(img)
