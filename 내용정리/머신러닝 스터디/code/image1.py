import sensor, image, lcd, time

lcd.init()

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((320, 240))
sensor.run(1)
sensor.set_vflip(0)
sensor.set_hmirror(0)

img = sensor.snapshot()

for i in range(0, 761000, 320):
    img[i] = (0, 255, 0)
    lcd.display(img)

img[640:960] = (0, 255, 0)
lcd.display(img)
