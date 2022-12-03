import random
import math
import pyxel

pyxel.init(200, 200)

score = 0
life = 5

pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)
pyxel.sound(0).set(note='C2', tone='T', volume='3', effect='N', speed=30)

class Ball:
    speed = 1

    def __init__(self):
        self.x = random.randint(0, 199)
        self.y = 0
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)

class Pad:
    def __init__(self):
        self.x = 100

balls = [Ball()]
pad = Pad()

def update():
    global balls, pad, speed, score, life
    for i in balls:
        i.x += i.vx*Ball.speed
        i.y += i.vx*Ball.speed

        if i.x >= 200 or i.x <= 0:
            i.vx = i.vx * -1