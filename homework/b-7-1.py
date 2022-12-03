import pyxel

pyxel.init(200,200)

a = 0
b = -1

def update():
    global a, b
    if pyxel.btnp(pyxel.KEY_SPACE):
        b*=-1
    a += b

def draw():
    pyxel.cls(7)
    pyxel.circ(200+a, 200+a, 10, 0)

pyxel.run(update, draw)
