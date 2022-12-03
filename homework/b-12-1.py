import pyxel
import random
import math

pyxel.init(200,200)

pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=5)
pyxel.sound(1).set(note='C2', tone='T', volume='3', effect='N', speed=30)

class Ball:
    speed=2
    def __init__(self):
        self.x = random.randint(0, 199)
        self.y = 0
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)

    def move(self):
        self.x += self.vx * Ball.speed
        self.y += self.vy * Ball.speed
        if self.x >= 200 or self.x <= 0:
            self.vx = -self.vx

class Pad:
    def __init__(self):
        self.x = 100

balls = [Ball(), Ball(), Ball()]
pad = Pad()

gameover = False
score = 0
miss = 0

def update():
    global gameover, pad, score, miss, balls

    pad.x = pyxel.mouse_x

    if gameover == False:
        for ball in balls:
            ball.move()

            if ball.y >= 200:
                miss += 1
                if miss >= 10:
                    gameover = True
                pyxel.play(0, 1)

                ball.x = random.randint(0, 199)
                ball.y = 0
                angle = math.radians(random.randint(30, 150))
                ball.vx = math.cos(angle)
                ball.vy = math.sin(angle)
                
                Ball.speed += 0.3
   
                if Ball.speed > 5:
                    Ball.speed = 5
         
            if ball.y >= 195 and pad.x - 20 <= ball.x <= pad.x + 20:
                score += 1
                pyxel.play(0, 0)
               
                ball.x = random.randint(0, 199)
                ball.y = 0
                angle = math.radians(random.randint(30, 150))
                ball.vx = math.cos(angle)
                ball.vy = math.sin(angle)
                
                Ball.speed += 0.3
                if Ball.speed > 5:
                    Ball.speed = 5


def draw():
    global gameover, pad, score, miss,balls
    pyxel.cls(7)
    if gameover == True:
        pyxel.text(10, 100, 'Game over!', 0)
    else:
        for ball in balls:
            pyxel.circ(ball.x, ball.y, 10, 6)
        pyxel.rect(pad.x-20, 195, 40, 5, 14)
    pyxel.text(10, 10, 'Score: ' + str(score), 0)
    pyxel.text(70, 10, 'Miss: ' + str(miss), 0)


pyxel.run(update, draw)
