import pyxel

pyxel.init(200,200)
pyxel.mouse(True)

a = 0
b = 0
c = 0
d = 0
count = 0

def update():
    global a, b, c, d, count
    if pyxel.btnp(pyxel.KEY_SPACE):
        count += 1
    if count >= 3:
        count = 0
        pyxel.cls(7)
    
    if count == 0:
        a = pyxel.mouse_x
        b = pyxel.mouse_y
    if count == 1:
        c = pyxel.mouse_x
        d = pyxel.mouse_y

def draw():
    pyxel.cls(7)
    if count >= 1:
        pyxel.line(a, b, c, d, 0)

pyxel.run(update, draw)
