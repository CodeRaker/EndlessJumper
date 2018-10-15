import pygame as pg
from settings import *
from random import randint
vec = pg.math.Vector2

class Thor(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game

        self.groups = game.all_sprites
        self._layer = 3
        pg.sprite.Sprite.__init__(self, self.groups)
        self.walk_anim = []
        self.walk_anim_right = []
        self.stand_anim = []
        self.attack_anim = []
        for i in range(0,7):
            image = pg.image.load('images/walk/walk' + str(i) + '.png').convert_alpha()
            image = pg.transform.scale(image, (image.get_width() // 2, image.get_height() // 2))
            self.walk_anim.append(image)

        for i in range(0,10):
            image = pg.image.load('images/stand/stand' + str(i) + '.png').convert_alpha()
            image = pg.transform.scale(image, (image.get_width() // 2, image.get_height() // 2))
            self.stand_anim.append(image)

        for i in range(0,14):
            image = pg.image.load('images/attack/attack' + str(i) + '.png').convert_alpha()
            image = pg.transform.scale(image, (image.get_width() // 2, image.get_height() // 2))
            self.attack_anim.append(image)

        self.frameWalk = 0
        self.frameWalkInvert = False
        self.frameAttack = 0

        self.image = self.stand_anim[0]
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

        self.rect.centerx = Width / 2
        self.rect.y = Height - self.rect.height

        self.debug = False


        #Player Movement variables
        self.standStill = True
        self.moveLeft = False
        self.moveRight = False
        self.jump = False
        self.fall = False
        self.attack = False
        self.facingRight = False
        self.groundLevel = 0
        self.jumpHeight = jumpHeight

        #Player Stats variables
        self.health = 100


    def update(self):
        self.getKeys()

        #Attack
        if self.attack:
            if self.debug:
                print(str('attack'))
            self.standStill = False
            if self.game.frameCounter %2 == 0:
                self.image = self.attack_anim[self.frameAttack]
                if self.facingRight:
                    self.image = pg.transform.flip(self.image, True, False)
                self.mask = pg.mask.from_surface(self.image)
                self.frameAttack += 1
                if self.frameAttack + 1 > len(self.attack_anim):
                    self.frameAttack = 0
                    self.attack = False

        #Left
        elif self.moveLeft:
            if self.debug:
                print(str('moveleft'))
            self.image = self.walk_anim[self.frameWalk]
            self.mask = pg.mask.from_surface(self.image)
            if self.rect.centerx > Width * 0.2:
                self.game.background.scroll = False
                self.rect.x -= 5
            else:
                self.game.background.scroll = True
            self.frameWalk += 1
            if self.frameWalk + 1 > len(self.walk_anim):
                self.frameWalk = 0

        #Right
        elif self.moveRight:
            if self.debug:
                print(str('moveright'))
            self.image = self.walk_anim[self.frameWalk]
            self.image = pg.transform.flip(self.image, True, False)
            self.mask = pg.mask.from_surface(self.image)
            if self.rect.centerx < Width * 0.8:
                self.game.background.scroll = False
                self.rect.x += 5
            else:
                self.game.background.scroll = True
            self.frameWalk += 1
            if self.frameWalk + 1 > len(self.walk_anim):
                self.frameWalk = 0

        #Jump
        if self.jump:
            if self.debug:
                print(str('jump'))
            if not self.fall:
                self.rect.y -= 5
            else:
                self.rect.y += 5
            if self.jumpHeight == 0 and not self.fall:
                self.fall = True
                self.jumpHeight = jumpHeight
            elif self.jumpHeight == 0 and self.fall:
                self.jump = False
                self.fall = False
                self.jumpHeight = jumpHeight
            self.jumpHeight -= 1

        #Stand
        elif self.standStill:
            if self.debug:
                print(str('stand'))
            if not self.frameWalkInvert:
                self.image = self.stand_anim[::-1][self.frameWalk]
            else:
                self.image = self.stand_anim[self.frameWalk]
            if self.facingRight:
                self.image = pg.transform.flip(self.image, True, False)
            self.mask = pg.mask.from_surface(self.image)
            self.frameWalk += 1
            if self.frameWalk + 1 > len(self.stand_anim):
                self.frameWalkInvert = not self.frameWalkInvert
                self.frameWalk = 0

        if self.health == 0:
            self.kill()



    def getKeys(self):
        pressed = pg.key.get_pressed()

        #Up
        if pressed[pg.K_w]:
            pass

        #Down
        if pressed[pg.K_s]:
            pass

        #Left
        if pressed[pg.K_a]:
            if not self.moveLeft:
                self.clearMovement()
                self.moveLeft = True
                self.facingRight = False

        #Right
        if pressed[pg.K_d]:
            if not self.moveRight:
                self.clearMovement()
                self.moveRight = True
                self.facingRight = True

        #Jump
        if pressed[pg.K_SPACE]:
            if not self.jump:
                self.jumpInit = True
                self.jump = True

        #Attack
        if pressed[pg.K_q]:
            if not self.attack:
                self.attack = True

        #Nothing
        if not pressed[pg.K_a] and not pressed[pg.K_d]:
            if not self.standStill:
                self.clearMovement()
                self.standStill = True

    def clearMovement(self):
        self.standStill = False
        self.moveLeft = False
        self.moveRight = False
        self.frameWalk = 0


    # def rotate(self):
    #     self.image = pg.transform.rotozoom(self.orig_image, self.angle, 1)
    #
    #     center = self.rect.center
    #     self.rect = self.image.get_rect()
    #     self.rect.center = center
