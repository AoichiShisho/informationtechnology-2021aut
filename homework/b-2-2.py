import pyxel
import math

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(0, 201, 10):
    b = math.radians(a)
    pyxel.line(a, 0, 0, 200-a, 0)
pyxel.show()
