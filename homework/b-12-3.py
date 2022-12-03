import pyxel
import random
import math

pyxel.init(200, 200)

padx = 100
life = 5

pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)
pyxel.sound(1).set(note='C2', tone='T', volume='3', effect='N', speed=30)

class Ball:
    speed = 1
    score = 0

    def __init__(self):
        self.restart()

    def restart(self):
        self.x = random.randint(0, 199)
        self.y = 0
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)

    def move(self):
        self.x += self.vx * Ball.speed
        self.y += self.vy * Ball.speed

        if self.x >= 200 or self.x <= 0:
            self.vx = self.vx * -1

        if self.y >= 195:
            Ball.speed += 0.2
            return True
        else:
            return False


class Pad:
    def __init__(self):
        self.x = 100

    def catch(self,arg):
            if self.x - 30 <= arg.x <= self.x + 30:
                pyxel.play(0,0)
                Ball.score += 1

                if Ball.score != 0 and Ball.score % 3 == 0:
                    balls.append(Ball())
                    Ball.speed = 1
                arg.restart()
                return False
            else:
                pyxel.play(0, 1)
                arg.restart()
                return True

balls = [Ball()]
pad = Pad()

def update():
    global balls, pad, speed, score, life

    for i in balls:
        if i.move():
            if pad.catch(i):
                life -= 1

    pad.x = pyxel.mouse_x

def draw():
    global balls, pad, score, life
    if life < 0:
        pyxel.text(80, 100, "GAME OVER", 0)

    else:
        pyxel.cls(7)

        for i in balls:
            pyxel.circ(i.x, i.y, 10, 6)

        pyxel.rect(pad.x - 20, 195, 40, 5, 14)
        pyxel.text(10, 10, "score:" + str(Ball.score), 0)
        pyxel.text(10, 20, "life:" + str(life), 0)

pyxel.run(update, draw)
