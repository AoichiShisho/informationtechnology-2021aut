import pyxel
import random
import math

pyxel.init(200,200)

ballx = [random.randint(0, 199)]
bally = [0]
angle = math.radians(random.randint(30, 150))
vx = [math.cos(angle)]
vy = [math.sin(angle)]

redballx = [random.randint(0, 199)]
redbally = [0]
redangle = math.radians(random.randint(30, 150))
redvx = [math.cos(redangle)]
redvy = [math.sin(redangle)]

yellowballx = [random.randint(0, 199)]
yellowbally = [0]
yellowangle = math.radians(random.randint(30, 150))
yellowvx = [math.cos(yellowangle)]
yellowvy = [math.sin(yellowangle)]

padx = 100
speed = 1
score = 0
addscore = 1
failure = 0
gameover = False

pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)
pyxel.sound(1).set(note='C1', tone='T', volume='5', effect='N', speed=30)
pyxel.sound(2).set(note='F3', tone='T', volume='5', effect='N', speed=30)

class Ball:
    def

def update():
    global ballx, bally, vx, vy, padx, speed, score, addscore, failure, gameover, amount, angle, redballx, redbally, redvx, redvy, yellowballx, yellowbally, yellowvx, yellowvy

    if failure >= 10:
        gameover = True
    
    if not gameover:  
        for i in range(0, len(ballx)):
            ballx[i] += vx[i] * speed
            bally[i] += vy[i] * speed

            redballx[i] += redvx[i] * speed
            redbally[i] += redvy[i] * speed

            yellowballx[i] += yellowvx[i] * speed
            yellowbally[i] += yellowvy[i] * speed

            if ballx[i] > 200 or ballx[i] < 0:
                vx[i] = vx[i] * -1

            if redballx[i] > 200 or redballx[i] < 0:    
                redvx[i] = redvx[i] * -1

            if yellowballx[i] > 200 or yellowballx[i] < 0:
                yellowvx[i] = yellowvx[i] * -1

            if bally[i] >= 200:
                if padx - 30 <= ballx[i] <= padx + 30:
                    pyxel.play(0, 0)
                    score += addscore

                    if score!=0 and score%10==0:
                        ballx.append(random.randint(0, 199))
                        bally.append(0)
                        angle = math.radians(random.randint(30, 150))
                        vx.append(math.cos(angle))
                        vy.append(math.sin(angle))
                else:
                    pyxel.play(0, 1)
                    failure += 1

                if speed <= 3:
                    speed += 0.25

                bally[i] = 0

            if redbally[i] >= 200:
                if padx - 30 <= redballx[i] <= padx + 30:
                    pyxel.play(0, 1)
                    score += -1
                    failure += 1

                    if score!=0 and score%10==0:
                        redballx.append(random.randint(0, 199))
                        redbally.append(0)
                        angle = math.radians(random.randint(30, 150))
                        redvx.append(math.cos(angle))
                        redvy.append(math.sin(angle))
                redbally[i] = 0

            if yellowbally[i] >= 200:
                if padx - 30 <= yellowballx[i] <= padx + 30:
                    pyxel.play(0, 2)
                    addscore += 1

                    if score!=0 and score%10==0:
                        yellowballx.append(random.randint(0, 199))
                        yellowbally.append(0)
                        angle = math.radians(random.randint(30, 150))
                        yellowvx.append(math.cos(angle))
                        yellowvx.append(math.sin(angle))
                yellowbally[i] = 0

            padx = pyxel.mouse_x


def draw():
    global ballx, bally, vx, vy, padx, score, failure, gameover, redballx, redbally, yellowballx, yellowbally

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

        for i in range(0, len(redballx)):
            pyxel.circ(redballx[i], redbally[i], 10, 8)

        for i in range(0, len(ballx)):
            #if score>=10:
            pyxel.circ(yellowballx[i], yellowbally[i], 10, 10)

pyxel.run(update, draw)
