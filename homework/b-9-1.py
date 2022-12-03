import pyxel
import random
import math

pyxel.init(200,200)

ballx = random.randint(0, 199)
bally = 0
angle = math.radians(random.randint(30, 150))
vx = math.cos(angle)
vy = math.sin(angle)
padx = 100
speed = 3
score = 0

def update():
    global ballx, bally, vx, vy, padx, speed, score

    ballx += vx*speed
    bally += vy*speed

    if bally >= 200:
        ballx = random.randint(0, 199)
        bally = 0
        speed += 1

    if ballx > 200:
        vx *= -1

    if ballx < 0:
        vx *= -1

    if (ballx > (padx-20)) & (ballx < (padx+20)) & (bally > 195):
        score += 1

    padx = pyxel.mouse_x

def draw():
    global ballx, bally, vx, vy, padx
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(10, 10, "score " + str(score), 1)

pyxel.run(update, draw)
