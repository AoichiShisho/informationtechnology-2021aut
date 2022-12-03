import pyxel
import random

class Player:
    def __init__(self):
        self.x = 128 - 30
        self.y = 205
        self.vx = 0
        self.vy = 0
        self.lane = 0

class App():
    def __init__(self):
        pyxel.init(255, 255, caption="Car Rush!", fps=30)
        pyxel.load("resources.pyxres")
        
        self.play = False
        self.player = Player()
        self.ground = 205
        self.gravity = 2.5
        self.jumping = False
        self.score = 0
        self.finalscore = 0
        
        self.colorbool = 2

        self.timer = 0
        #対向車描画用の変数
        self.leftcar = 0
        self.centercar = 0
        self.rightcar = 0

        #プレイヤーの位置まで来た時の対向車の座標
        self.leftcar_x = 37
        self.centercar_x = 106
        self.rightcar_x = 171
        #y座標は共通しているため変数は一つのみ設定
        self.car_y = 195

        #煙を表示させるための変数
        self.rightsmoke = 0
        self.leftsmoke = 0
        self.centersmoke = 0

        self.rightsmokebool = False
        self.leftsmokebool = False
        self.centersmokenum = 0

        #適当な車線から対向車線を生成
        self.choose_bool = False
        self.chooser = 2

        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.play == False:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.play = True
            self.score = 0

        if self.play:
            self.score+=1

    def draw(self):
        #タイトル画面時
        if self.play == False:
            
            pyxel.image(2).load(0, 0, "blue.png")
            pyxel.cls(0)
            pyxel.blt(0, 0, 2, 0, 0, 255, 255)
            #色のチェンジ
            pyxel.blt(120, 80, 0, 0, 16, 16, 16, 0)
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                if 120 <= pyxel.mouse_x <= 136:
                    if 80 <= pyxel.mouse_y <= 96:
                        self.colorbool += 1
                        if self.colorbool%2==0:
                            pyxel.play(0, 0)
                        if self.colorbool%2==1:
                            pyxel.play(0, 1)

            pyxel.text(100, 235, "High Score: " + str(self.finalscore), 7)

        #プレイ時
        if self.play == True:
            #背景の描写
            pyxel.blt(0, 0, 1, 0, 0, 255, 255)

            #ハイスコアを更新する
            if self.score > self.finalscore:
                self.finalscore = self.score

            self.timer += 1
            #1秒に一度どれかのレーンに対向車を生成
            if self.timer >= 30:
                self.chooser = random.randint(-1, 1)
                self.timer = 0
            if self.chooser == -1:
                self.leftcar += 1
            elif self.chooser == 0:
                self.centercar += 1
            elif self.chooser == 1:
                self.rightcar += 1

            #左レーンの対向車の描画
            if 2 <= self.leftcar <= 4:
                pyxel.blt(112, 141, 0, 64, 0, 8, 4, 7)
            if 4 <= self.leftcar <= 6:
                pyxel.blt(109, 143, 0, 72, 0, 9, 6, 7)
            if 6 <= self.leftcar <= 8:
                pyxel.blt(103, 144, 0, 81, 0, 14, 9, 7)
            if 8 <= self.leftcar <= 10:
                pyxel.blt(97, 148, 0, 95, 0, 18, 10, 7)
            if 10 <= self.leftcar <= 12:
                pyxel.blt(92, 154, 0, 64, 8, 21, 12, 7)
            if 12 <= self.leftcar <= 14:
                pyxel.blt(86, 161, 0, 85, 11, 23, 13, 7)
            if 14 <= self.leftcar <= 16:
                pyxel.blt(76, 167, 0, 108, 11, 29, 19, 7)
            if 16 <= self.leftcar <= 18:
                pyxel.blt(61, 178, 0, 64, 80, 40, 27, 7)
            if 18 <= self.leftcar <= 20:
                pyxel.blt(self.leftcar_x, self.car_y, 0, 64, 44, 64, 36, 7)
                self.leftcar = 0
                self.score += 1000
                self.chooser = 2
                if (self.player.lane == -1 and self.car_y <= self.player.y <= self.car_y+36):
                    self.play = False

            #中央レーンの対向車の描画
            if 2 <= self.centercar <= 4:
                pyxel.blt(126, 141, 0, 64, 0, 8, 4, 7)
            if 4 <= self.centercar <= 6:
                pyxel.blt(125, 143, 0, 72, 0, 9, 6, 7)
            if 6 <= self.centercar <= 8:
                pyxel.blt(123, 144, 0, 81, 0, 14, 9, 7)
            if 8 <= self.centercar <= 10:
                pyxel.blt(121, 148, 0, 95, 0, 18, 10, 7)
            if 10 <= self.centercar <= 12:
                pyxel.blt(119, 154, 0, 64, 8, 21, 12, 7)
            if 12 <= self.centercar <= 14:
                pyxel.blt(118, 161, 0, 85, 11, 23, 13, 7)
            if 14 <= self.centercar <= 16:
                pyxel.blt(115, 167, 0, 108, 11, 29, 19, 7)
            if 16 <= self.centercar <= 18:
                pyxel.blt(110, 178, 0, 64, 80, 40, 27, 7)
            if 18 <= self.centercar <= 20:
                pyxel.blt(self.centercar_x, self.car_y, 0, 64, 44, 64, 36, 7)
                self.centercar = 0
                self.score += 1000
                self.chooser = 2
                if (self.player.lane == 0 and self.car_y <= self.player.y <= self.car_y+36):
                    self.play = False

            #右レーンの対抗戦の描画
            if 2 <= self.rightcar <= 4:
                pyxel.blt(136, 141, 0, 64, 0, 8, 4, 7)
            if 4 <= self.rightcar <= 6:
                pyxel.blt(138, 143, 0, 72, 0, 9, 6, 7)
            if 6 <= self.rightcar <= 8:
                pyxel.blt(139, 144, 0, 81, 0, 14, 9, 7)
            if 8 <= self.rightcar <= 10:
                pyxel.blt(141, 148, 0, 95, 0, 18, 10, 7)
            if 10 <= self.rightcar <= 12:
                pyxel.blt(143, 154, 0, 64, 8, 21, 12, 7)
            if 12 <= self.rightcar <= 14:
                pyxel.blt(147, 161, 0, 85, 11, 23, 13, 7)
            if 14 <= self.rightcar <= 16:
                pyxel.blt(151, 167, 0, 108, 11, 29, 19, 7)
            if 16 <= self.rightcar <= 18:
                pyxel.blt(155, 178, 0, 64, 80, 40, 27, 7)
            if 18 <= self.rightcar <= 20:
                pyxel.blt(self.rightcar_x, self.car_y, 0, 64, 44, 64, 36, 7)
                self.rightcar = 0
                self.score += 1000
                self.chooser = 2
                if (self.player.lane == 1 and self.car_y <= self.player.y <= self.car_y+36):
                    self.play = False

            #右または左押したら煙を生成するBoolを1にする
            if pyxel.btnp(pyxel.KEY_RIGHT):
                self.rightsmokebool = True
                self.leftsmokebool = False
            if pyxel.btnp(pyxel.KEY_LEFT):
                self.leftsmokebool = True
                self.rightsmokebool = False
            #右レーンで煙を表示させる
            if self.player.lane == 1 and self.player.x >= 178 and self.rightsmokebool == True:
                self.rightsmoke += 1
                if 2 <= self.rightsmoke <= 4:
                    pyxel.blt(self.player.x + 64, self.player.y + 16, 0, 64, 112, 16, 16, 7)
                if 4 <= self.rightsmoke <= 6:
                    pyxel.blt(self.player.x + 68, self.player.y + 12, 0, 64, 112, 16, 16, 7)
                if 6 <= self.rightsmoke <= 8:
                    pyxel.blt(self.player.x + 72, self.player.y +  8, 0, 96, 112,  8, 16, 7)
                if 8 <= self.rightsmoke <= 10:
                    pyxel.blt(self.player.x + 76, self.player.y +  4, 0, 104, 112, 8, 16, 7)
                    self.rightsmoke = 0
                    self.rightsmokebool = False

            #左レーンで煙を表示させる
            if self.player.lane == -1 and self.player.x <= 18 and self.leftsmokebool == True:
                self.leftsmoke += 1
                if 2 <= self.leftsmoke <= 4:
                    pyxel.blt(self.player.x - 4, self.player.y + 16, 0, 112, 112, 16, 16, 7)
                if 4 <= self.leftsmoke <= 6:
                    pyxel.blt(self.player.x - 8, self.player.y + 12, 0, 128, 112, 16, 16, 7)
                if 6 <= self.leftsmoke <= 8:
                    pyxel.blt(self.player.x - 12, self.player.y + 8, 0, 144, 112,  8, 16, 7)
                if 8 <= self.leftsmoke <= 10:
                    pyxel.blt(self.player.x - 16, self.player.y + 4, 0, 152, 112, 16, 16, 7)
                    self.leftsmoke = 0
                    self.leftsmokebool = False

            #中央レーンで煙を表示させる
            if pyxel.btnp(pyxel.KEY_LEFT):
                self.centersmokenum = -1
                pyxel.play(0, 1)
            if pyxel.btnp(pyxel.KEY_RIGHT):
                self.centersmokenum = 1
                pyxel.play(0, 1)

            if self.player.lane == 0 and 96 <= self.player.x <= 100:
                #左側に煙を生成する
                if self.centersmokenum == -1:
                    self.centersmoke += 1
                    if 2 <= self.centersmoke <= 4:
                        pyxel.blt(self.player.x - 4, self.player.y + 16, 0, 112, 112, 16, 16, 7)
                    if 4 <= self.centersmoke <= 6:
                        pyxel.blt(self.player.x - 8, self.player.y + 12, 0, 128, 112, 16, 16, 7)
                    if 6 <= self.centersmoke <= 8:
                        pyxel.blt(self.player.x - 12, self.player.y + 8, 0, 144, 112,  8, 16, 7)
                    if 8 <= self.centersmoke <= 10:
                        pyxel.blt(self.player.x - 16, self.player.y + 4, 0, 152, 112, 16, 16, 7)
                        self.centersmoke = 0
                        self.centersmokenum = 0
                #右側に煙を生成する
                if self.centersmokenum == 1:
                    self.centersmoke += 1
                    if 2 <= self.centersmoke <= 4:
                        pyxel.blt(self.player.x + 64, self.player.y + 16, 0, 64, 112, 16, 16, 7)
                    if 4 <= self.centersmoke <= 6:
                        pyxel.blt(self.player.x + 68, self.player.y + 12, 0, 64, 112, 16, 16, 7)
                    if 6 <= self.centersmoke <= 8:
                        pyxel.blt(self.player.x + 72, self.player.y +  8, 0, 96, 112,  8, 16, 7)
                    if 8 <= self.centersmoke <= 10:
                        pyxel.blt(self.player.x + 76, self.player.y +  4, 0, 104, 112, 8, 16, 7)
                        self.centersmoke = 0
                        self.centersmokenum = 0
                

            #プレイヤーの車を描画
            if self.colorbool%2==0:
                pyxel.blt(self.player.x, self.player.y, 0, 0, 94, 64, 34, 11)
            if self.colorbool%2==1:
                pyxel.blt(self.player.x, self.player.y, 0, 0, 46, 64, 34, 11)
            #スコアの描画
            pyxel.text(10, 10, "Score: " + str(self.score), 0)

            #プレイヤーの縦横移動における設定
            self.player.vy += self.gravity
            self.player.y += self.player.vy
            self.player.x += self.player.vx

            #着地を固定させる
            if self.player.y > self.ground - 1:
                self.player.y = self.ground
                self.jumping = False

            #スペースを押した時ジャンプさせる
            if pyxel.btnp(pyxel.KEY_SPACE):
                if self.jumping == False:
                    self.player.vy = -20
                    self.jumping = True
                    pyxel.play(0, 0)

            #左矢印を押した時左レーンへ行く
            if pyxel.btnp(pyxel.KEY_LEFT):
                if self.player.lane > -1:
                    if self.player.vx >= -50:
                        self.player.vx -= 50
                        self.player.lane -= 1
            #右矢印を押した時右レーンへ行く
            if pyxel.btnp(pyxel.KEY_RIGHT):
                if self.player.lane < 1:
                    if self.player.vx <= 50:
                        self.player.vx += 50
                        self.player.lane += 1
            
            #左レーンの時動きを止める
            if self.player.lane == -1 and self.player.x <= 18:
                self.player.vx = 0
                self.player.x = 18
            #中央レーンの時動きを止める
            elif self.player.lane == 0 and 78 <= self.player.x <= 118:
                self.player.vx = 0
                self.player.x = 98
            #右レーンの時動きを止める
            elif self.player.lane == 1 and self.player.x >= 178:
                self.player.vx = 0
                self.player.x = 178
            

App()