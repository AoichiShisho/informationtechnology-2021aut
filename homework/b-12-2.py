import pyxel
import random
import math

pyxel.init(200, 200)

pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=5)
pyxel.sound(1).set(note='C1', tone='T', volume='3', effect='N', speed=15)


class Ball:
    speed = 1

    def __init__(self):
        self.restart()

    def move(self):
        self.x += self.vx * Ball.speed
        self.y += self.vy * Ball.speed
        if self.x <= 0 or self.x >= 200:
            self.vx =- self.vx

        if self.y >= 200:
            self.restart()
            Ball.speed += 0.1
            if Ball.speed > 5:
                Ball.speed = 5
            return True
        else:
            return False

    def restart(self):
        self.x = random.randint(0, 199)
        self.y = 0
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)

class Pad:
    def __init__(self):
        self.x = 100

balls = [Ball(), Ball(), Ball()]
pad = Pad()

gameover = False
score = 0
life = 5

def update():
    global balls, gameover, speed, pad, score, life

    pad.x = pyxel.mouse_x
    if gameover == False:
        for ball in balls:
            if ball.move() == False:
                if ball.y >= 195 and pad.x - 40 <= ball.x <= pad.x + 40:
                    score = score + 1
                    pyxel.play(0, 0)
            if ball.move() == True:
                life -= 1

            if life == 0:
                gameover = True
                pyxel.play(0, 0)


def draw():
    global gameover, pad, score, life, balls
    pyxel.cls(7)
    if gameover == True:
        pyxel.text(10, 100, 'GAME OVER!', 0)
    else:
        for ball in balls:
            pyxel.circ(ball.x, ball.y, 10, 6)
        pyxel.rect(pad.x-20, 195, 40, 5, 14)
    pyxel.text(10, 10, 'score: ' + str(score), 0)
    pyxel.text(10, 20, 'life: ' + str(life), 0)

pyxel.run(update, draw)
