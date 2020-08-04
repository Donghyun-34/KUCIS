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
    a = 100
    img.draw_string(10, 10, "string %d"%(a), (255,255,255), scale = 2)
    lcd.display(img)
