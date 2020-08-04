import sensor, image, lcd, time

lcd.init()

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((320, 240))
sensor.run(1)
sensor.set_vflip(0)
sensor.set_hmirror(0)

while True:
    img = sensor.snapshot()
    img.draw_rectangle((10, 10, 50, 50), (0, 0, 255), thickness = 2, fill = False)
    # (10, 10, 50, 50) : 좌표
    # (0, 0, 255) : 사각형 색깔
    # thickness : 선 굵기
    # fill : 안을 채울지 결정(False : 채우기 없음, True : 채우기 있음)
    lcd.display(img)
