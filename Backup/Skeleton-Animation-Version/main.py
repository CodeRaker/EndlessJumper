import pygame as pg
from settings import *
from player import *
#from enemy import *
from colorpalette import *

vec = pg.math.Vector2

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Width, Height))
        pg.display.set_caption('Little Thor')
        self.rgb = RGBColors()
        self.clock = pg.time.Clock()
        self.frameRate = 60
        self.running = True
        self.loadAssets()

    def loadAssets(self):
        # self.enemyCount = 1
        self.all_sprites = pg.sprite.LayeredUpdates()
        #self.player = Player(self)
        # self.enemies = pg.sprite.Group()
        self.tBody = pg.sprite.Group()
        self.tBodyParts = {'beard':0,'cloth':1,'eyebrows':2,'face':3,'hair':4,'hammer':5,'left_leg':6,'left_lower_arm':7,'left_upper_arm':8,'necklace':9,'right_leg':10,'right_lower_arm':11,'right_upper_arm':12,'torso':13}
        for bodypart in self.tBodyParts:
            self.Thor = Thor(self, bodypart)
        self.hammerTime = False


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.KEYDOWN and event.key == pg.K_q:
                print('Q')
                if not self.hammerTime:
                    self.tHammerTimer = 50
                    self.hammerTime = True
                    self.hammerAttack()

        pressed = pg.key.get_pressed()

        if pressed[pg.K_w]:             #W - UP
            self.torso.rect.y -= 3

        if pressed[pg.K_s]:             #S - DOWN
            self.torso.rect.y += 3

        if pressed[pg.K_a]:             #A - LEFT
            self.torso.rect.x -= 5
            self.tAnimation()

        if pressed[pg.K_d]:             #D - RIGHT
            self.torso.rect.x += 5
            self.tAnimation()

        if not pressed[pg.K_a] and not pressed[pg.K_d]:
            self.tWalkTimer = 0
            self.tAnimation()

    def tAnimation(self):
        self.initTorso = self.torso.rect.y
        if self.tWalkTimer == 0:
            self.tAnimationReset()

        elif self.tWalkTimer >= 150 or self.tWalkTimer < 50:
            self.tWalkTimer -= 5
            self.left_leg.angle += 2
            self.right_leg.angle -= 2

            if not self.hammerTime:
                self.left_upper_arm.angle -= 1
                self.left_lower_arm.angle += 1

            self.right_upper_arm.angle += 1
            self.right_lower_arm.angle -= 1
            self.necklace.angle -= 1
            self.torso.rect.y += 1
            self.tAnimationRotate()

        elif self.tWalkTimer < 150 and self.tWalkTimer >= 50:
            self.tWalkTimer -= 5
            self.left_leg.angle -= 2
            self.right_leg.angle += 2

            if not self.hammerTime:
                self.left_upper_arm.angle += 1
                self.left_lower_arm.angle -= 1

            self.right_upper_arm.angle -= 1
            self.right_lower_arm.angle += 1
            self.necklace.angle += 1
            self.torso.rect.y -= 1
            self.tAnimationRotate()

    def tAnimationReset(self):
        self.tWalkTimer = 200
        self.left_leg.angle = self.left_leg.initAngle
        self.right_leg.angle = self.right_leg.initAngle

        if not self.hammerTime:
            self.left_upper_arm.angle = self.left_upper_arm.initAngle
            self.left_lower_arm.angle = self.left_lower_arm.initAngle

        self.right_upper_arm.angle = self.right_upper_arm.initAngle
        self.right_lower_arm.angle = self.right_lower_arm.initAngle
        self.necklace.angle = self.necklace.initAngle
        self.torso.rect.y = self.initTorso
        self.tAnimationRotate()

    def tAnimationRotate(self):
        self.left_leg.rotate()
        self.right_leg.rotate()

        if not self.hammerTime:
            self.left_upper_arm.rotate()
            self.left_lower_arm.rotate()

        self.right_upper_arm.rotate()
        self.right_lower_arm.rotate()
        self.necklace.rotate()

    def hammerAttack(self):
        if self.tHammerTimer != 0:
            self.tHammerTimer -= 1
            self.left_upper_arm.angle -= 1
            self.left_lower_arm.angle -= 1
            self.left_upper_arm.rotate()
            self.left_lower_arm.rotate()
        else:
            self.tHammerTimer = 0
            self.hammerTime = False


    def update(self):
        #primary anchor point
        self.torso.update()

        #secondary anchor point
        self.left_upper_arm.update()
        self.right_upper_arm.update()
        self.face.update()
        self.beard.update()

        #tertiary anchor point
        self.left_lower_arm.update()
        self.right_lower_arm.update()

        #endpoint
        self.left_leg.update()
        self.right_leg.update()
        self.hammer.update()
        self.cloth.update()
        self.hair.update()
        self.eyebrows.update()
        self.necklace.update()

        if self.hammerTime:
            self.hammerAttack()


    def draw(self):
        self.screen.fill(self.rgb.gray)
        self.all_sprites.draw(self.screen)

    def run(self):
        while self.running:
            self.clock.tick(self.frameRate)
            self.events()
            self.update()
            self.draw()
            pg.display.flip()

g = Game()
while g.running:
    g.run()
pg.quit()
