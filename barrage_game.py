import math
import random
import pyxel


class Bullet:
    def __init__(self, angle):
        self.init(angle)

    def init(self, angle):
        self.r = 1
        self.color = 10

        self.x = 100
        self.y = 0
        self.angle = angle
        self.radian = math.radians(self.angle)
        self.vx = math.cos(self.radian)
        self.vy = math.sin(self.radian)
        self.speed = 2

    def update(self):
        self.x += self.vx * self.speed
        self.y += self.vy * self.speed


class Player:
    def __init__(self):
        self.init()

    def init(self):
        self.width = 5
        self.height = 5
        self.color = 5

        self.x = 100
        self.y = 180
        self.up = 4
        self.down = 4
        self.left = 4
        self.right = 4

    def update(self):
        if (pyxel.btn(pyxel.KEY_UP)):
            self.y -= self.up
        elif (pyxel.btn(pyxel.KEY_DOWN)):
            self.y += self.down
        elif (pyxel.btn(pyxel.KEY_LEFT)):
            self.x -= self.left
        elif (pyxel.btn(pyxel.KEY_RIGHT)):
            self.x += self.right

    def is_miss(self, bullet):
        return self.x <= bullet.x <= self.x + self.width and self.y <= bullet.y <= self.y + self.height


class App:
    def __init__(self):
        pyxel.init(200, 200)

        self.init()

        pyxel.run(self.update, self.draw)

    def init(self):
        self.scene = 0

        self.bullets = []
        self.player = Player()

    def update(self):
        if self.scene == 0:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.scene += 1
        elif self.scene == 1:
            if pyxel.frame_count % 15 == 0:
                for i in range(1 + random.randint(0, 9), 180, 10):
                    self.bullets.append(Bullet(i))

            for bullet in self.bullets:
                bullet.update()
                if self.player.is_miss(bullet):
                    self.scene += 1
            self.player.update()
        elif self.scene == 2:
            if pyxel.btnp(pyxel.KEY_TAB):
                self.init()

    def draw(self):
        pyxel.cls(7)
        if self.scene == 0:
            pyxel.text(60, 100, "push SPACE to start", 0)
        elif self.scene == 1:
            for bullet in self.bullets:
                pyxel.circ(bullet.x, bullet.y, bullet.r, bullet.color)
            pyxel.rect(self.player.x, self.player.y, self.player.width, self.player.height, self.player.color)
        elif self.scene == 2:
            pyxel.text(80, 100, "GAME OVER", 0)

App()