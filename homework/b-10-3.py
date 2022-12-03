import pyxel
import random
import math

pyxel.init(200,200)

ballx = [random.randint(0, 199)]
bally = [0]
angle = math.radians(random.randint(30, 150))
vx = [math.cos(angle)]
vy = [math.sin(angle)]

padx = 100
speed = 1
score = 0
failure = 0
gameover = False

pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)
pyxel.sound(1).set(note='C1', tone='T', volume='5', effect='N', speed=30)

def update():
    global ballx, bally, vx, vy, padx, speed, score, failure, gameover, amount, angle

    if failure >= 10:
        gameover = True
    
    if not gameover:  
        for i in range(0, len(ballx)):
            ballx[i] += vx[i] * speed
            bally[i] += vy[i] * speed

            if ballx[i] > 200 or ballx[i] < 0:
                vx[i] = vx[i] * -1

            if bally[i] >= 200:
                if padx - 30 <= ballx[i] <= padx + 30:
                    pyxel.play(0, 0)
                    score += 1

                    if score!=0 and score%10==0:
                        ballx.append(random.randint(0, 199))
                        bally.append(0)
                        angle = math.radians(random.randint(30, 150))
                        vx.append(math.cos(angle))
                        vy.append(math.sin(angle))
                        speed = 1
                else:
                    pyxel.play(0, 1)
                    failure += 1

                if speed <= 3:
                    speed += 0.25

                bally[i] = 0

            padx = pyxel.mouse_x


def draw():
    global ballx, bally, vx, vy, padx, score, failure, gameover

    if gameover:
        pyxel.cls(0)
        pyxel.text(30, 100, "GAME OVER", 7)
        pyxel.text(30, 110, "Your final score was " + str(score), 7)
    else:
        pyxel.cls(7)
        for i in range(0, len(ballx)):
            pyxel.circ(ballx[i], bally[i], 10, 6)
            pyxel.rect(padx-20, 195, 40, 5, 14)
            pyxel.text(10, 10, "score " + str(score), 1)
            pyxel.text(100, 10, "Failure:" + str(failure), 0)

pyxel.run(update, draw)