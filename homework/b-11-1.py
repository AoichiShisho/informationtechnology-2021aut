import pyxel
import random
import math

pyxel.init(200, 200)

padx = 100
score = 0
life = 5

pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)
pyxel.sound(1).set(note='C2', tone='T', volume='3', effect='N', speed=30)

class Ball:
    speed = 1

    def __init__(self):
        self.x = random.randint(0, 199)
        self.y = 0
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)


balls = [Ball()]


def update():
    global balls, padx, score, life

    for i in balls:
        i.x += i.vx * Ball.speed
        i.y += i.vy * Ball.speed

        if i.x >= 200 or i.x <= 0:
            i.vx = i.vx * -1

        if i.y >= 195:
            i.y = 0

            if Ball.speed <= 3:
                Ball.speed += 0.2

            if padx - 30 <= i.x <= padx + 30:
                pyxel.play(0, 0)
                score = score + 1

                if score!=0 and score%3==0:
                    balls.append(Ball())
                    Ball.speed = 1

            else:
                pyxel.play(0, 1)
                life = life - 1

        padx = pyxel.mouse_x

def draw():
    global balls, padx, score, life
    if life < 0:
        pyxel.text(80, 100, "GAME OVER", 0)

    else:
        pyxel.cls(7)

        for i in balls:
            pyxel.circ(i.x, i.y, 10, 6)

        pyxel.rect(padx-20, 195, 40, 5, 14)
        pyxel.text(10, 10, "score: " + str(score), 0)
        pyxel.text(10, 20, "life: " + str(life), 0)

pyxel.run(update, draw)