import pyxel

pyxel.init(200,200)
pyxel.mouse(True)

a = 0
b = 0
c = 0
d = 0
pyxel.cls(7)

def update():
    global a, b, c, d
    if pyxel.btnp(pyxel.KEY_SPACE):
        a = pyxel.mouse_x
        b = pyxel.mouse_y
    if pyxel.btn(pyxel.KEY_SPACE):
        pyxel.cls(7)
    if pyxel.btn(pyxel.KEY_SPACE):
        c = pyxel.mouse_x
        d = pyxel.mouse_y


def draw():
    global a, b, c, d
    pyxel.cls(7)
    pyxel.line(a, b, c, d, 0)

pyxel.run(update, draw)
