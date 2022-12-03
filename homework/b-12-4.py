import random
import pyxel
import math

class Ball:
    speed = 1

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
            self.vx = self.vx*-1

        if self.y >= 195:
            Ball.speed+=0.2
            return True
        else:
            return False

class Pad:
    def __init__(self):
        self.x = 100

    def catch(self, arg):
        if self.x - 30 <= arg.x <= self.x + 30:
            arg.restart()
            return False
        else:
            arg.restart()
            return True

class App:
    def __init__(self):
        pyxel.init(200, 200)
        pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)
        pyxel.sound(1).set(note='C2', tone='T', volume='3', effect='N', speed=30)

        self.life = 5
        self.score = 0

        self.balls = [Ball()]
        self.pad = Pad()

        pyxel.run(self.update, self.draw)

    def update(self):
        for i in self.balls:
            if i.move():
                if self.pad.catch(i):
                    pyxel.play(0, 1)
                    print("miss")
                    self.life -= 1
                else:
                    pyxel.play(0, 0)
                    self.score += 1

                    if self.score != 0 and self.score%3==0:
                        self.balls.append(Ball())
                        Ball.speed = 1
                    print("catch")

        self.pad.x = pyxel.mouse_x

    def draw(self):
        if self.life < 0:
          pyxel.text(80, 100, "GAME OVER", 0)

        else:
            pyxel.cls(7)

            for i in self.balls:
                pyxel.circ(i.x, i.y, 10, 6)

                pyxel.rect(self.pad.x-20, 195, 40, 5, 14)
                pyxel.text(10, 10, "score: " + str(self.score), 0)
                pyxel.text(10, 20, "life: " + str(self.life), 0)

App()