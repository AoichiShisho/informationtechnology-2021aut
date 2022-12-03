import pyxel

pyxel.init(200, 200, scale=2)
pyxel.cls(7)
for a in range(10, 200, 20):
    for b in range(10, 200, 20):
        if (a+b) <= 100:
            c = 2
        elif (a+b) <= 200:
            c = 3
        elif (a+b) <= 300:
            c = 6
        elif (a+b) <= 400:
            c = 14
        pyxel.circ(a, b, 10, c)
pyxel.show()
