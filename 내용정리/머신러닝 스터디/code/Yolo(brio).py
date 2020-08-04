import sensor,image,lcd,time
import KPU as kpu

lcd.init(freq=15000000)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(0)
sensor.run(1)
clock = time.clock()
classes = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']
task = kpu.load(0x500000)
anchor = (1.08, 1.19, 3.42, 4.41, 6.63, 11.38, 9.42, 5.11, 16.62, 10.52)
a = kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)
while(True):
    clock.tick()
    img = sensor.snapshot()
    code = kpu.run_yolo2(task, img)
    print(clock.fps())
    if code:
        img.draw_string(10, 10, "target detected", (0,255,0), scale = 2)
        for i in code:
            a=img.draw_rectangle(i.rect())
            for i in code:
                img.draw_string(i.x(), i.y(), classes[i.classid()], (255,255,255), scale = 2)
                img.draw_string(i.x(), i.y()+24, '%.3f'%i.value(), (0,0,255))
            a = lcd.display(img)
    else:
        img.draw_string(10, 10, "target not detected", (255,0,0), scale = 2)
        a = lcd.display(img)
a = kpu.deinit(task)
