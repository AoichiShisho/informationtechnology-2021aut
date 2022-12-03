import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(10, 400, 20):
    for b in range(10, 400, 20):
        if (a+b) <= 20:
            c = 0
        elif (a+b) <= 40:
            c = 1
        elif (a+b) <= 60:
            c = 5
        elif (a+b) <= 80:
            c = 12
        elif (a+b) <= 100:
            c = 3
        elif (a+b) <= 120:
            c = 11
        elif (a+b) <= 140:
            c = 10
        elif (a+b) <= 160:
            c = 9
        elif (a+b) <= 180:
            c = 8
        elif (a+b) <= 200:
            c = 2
        elif (a+b) <= 220:
            c = 2
        elif (a+b) <= 240:
            c = 1
        elif (a+b) <= 260:
            c = 5
        elif (a+b) <= 280:
            c = 12
        elif (a+b) <= 300:
            c = 3
        elif (a+b) <= 320:
            c = 11
        elif (a+b) <= 340:
            c = 10
        elif (a+b) <= 360:
            c = 9
        elif (a+b) <= 380:
            c = 8
        elif (a+b) <= 400:
            c = 2
        pyxel.circ(a, b, 10, c)
pyxel.show()
