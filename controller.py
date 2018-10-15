import pygame as pg
from settings import *

class ThorController:
    def __init__(self):
        self.initMovement()
        self.initCharacterStats()

    def initMovement(self):
        self.standing = True
        self.moveLeft = False
        self.moveRight = False
        self.jumping = False
        self.falling = False
        self.attacking = False
        self.facingRight = False
        self.groundLevel = 0
        self.standLock = False

    def initCharacterStats(self):
        self.health = 100
        self.jumpHeight = jumpHeight

    def getKeys(self):
        pressed = pg.key.get_pressed()

        if pressed[pg.K_a]:
            self.move('left')

        if pressed[pg.K_d]:
            self.move('right')

        if pressed[pg.K_SPACE] or pressed[pg.K_w]:
            self.jump()

        if pressed[pg.K_q]:
            self.attack()

        elif not pressed[pg.K_a] and not pressed[pg.K_d]:
            self.standLock = False
            self.stand()

    def stand(self):
        if not self.standLock:
            self.clearMovement()
            self.standing = True

    def attack(self):
        if not self.attacking:
            self.attacking = True

    def move(self, direction):
        self.standLock = True
        if direction == 'left':
            self.moveRight = False
            self.facingRight = False
            self.moveLeft = True
        elif direction == 'right':
            self.moveLeft = False
            self.facingRight = True
            self.moveRight = True

    def jump(self):
        if not self.jumping:
            self.jumpInit = True
            self.jumping = True

    def clearMovement(self):
        self.moveRight = False
        self.moveLeft = False
