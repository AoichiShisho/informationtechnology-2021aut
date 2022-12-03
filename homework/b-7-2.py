import pyxel

pyxel.init(200,200)
pyxel.mouse(True)

a = 1
x = 0
y = 0

def update():
    global a
    if pyxel.btnp(pyxel.KEY_SPACE):
        a = -1
    if pyxel.btnr(pyxel.KEY_SPACE):
        a = 1

def draw():
    global a, x, y

    if a == -1:
        x = pyxel.mouse_x
        y = pyxel.mouse_y

    pyxel.cls(7)
    pyxel.line(0, 0, x, y, 0)

pyxel.run(update, draw)