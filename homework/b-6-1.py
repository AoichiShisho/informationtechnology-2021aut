import pyxel

pyxel.init(200,200)

a = 0

def update():
    global a
    a += 1
    if a == 100:
        a = a-200

def draw():
    global a
    pyxel.cls(7)
    pyxel.circ(100+a, 100+a, 10, 0)

pyxel.run(update, draw)
