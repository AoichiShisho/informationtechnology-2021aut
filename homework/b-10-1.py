import pyxel
import random
import math

pyxel.init(200,200)

ballx = []
bally = []
vx = []
vy = []
padx = 100
speed = 3
score = 0

amount = 3

for i in range(0, amount):
    ballx.append(random.randint(0, 199))
    bally.append(0)

    angle = math.radians(random.randint(30, 150))
    vx.append(math.cos(angle))
    vy.append(math.sin(angle))

pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)
pyxel.sound(1).set(note='C1', tone='T', volume='5', effect='N', speed=30)

def update():
    global ballx, bally, vx, vy, padx, speed, score

    for i in range(0, amount):
        ballx[i] += vx[i]
        bally[i] += vy[i]

        if ballx[i] > 200 or ballx[i] < 0:
            vx[i] = vx[i] * -1

        if bally[i] >= 200:
            if padx - 30 <= ballx[i] <= padx + 30:
                pyxel.play(0, 0)
                score = score + 1
            else:
                pyxel.play(0, 1)

            bally[i] = 0
            speed += 1
            vx[i] = vx[i]*speed
            vy[i] = vy[i]*speed

        padx = pyxel.mouse_x

def draw():
    global ballx, bally, vx, vy, padx
    pyxel.cls(7)

    for i in range(0, amount):
        pyxel.circ(ballx[i], bally[i], 10, 6)
        pyxel.rect(padx-20, 195, 40, 5, 14)
        pyxel.text(10, 10, "score " + str(score), 1)

pyxel.run(update, draw)

