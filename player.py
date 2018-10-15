import pygame as pg
from settings import *
from random import randint
from controller import ThorController
from imageloader import ImageLoader
vec = pg.math.Vector2

class Thor(ThorController, ImageLoader, pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.ctrl = ThorController()
        self.imageLoader = ImageLoader()
        self.groups = game.all_sprites
        self._layer = 3
        pg.sprite.Sprite.__init__(self, self.groups)
        self.initGraphics()

    def initGraphics(self):
        self.frameWalk = 0
        self.frameWalkInvert = False
        self.frameStand = 0
        self.frameStandInvert = False
        self.frameAttack = 0
        self.walkAnimation = self.imageLoader.LoadImages(7, 'images/walk/', 'walk', 'png', True)
        self.standAnimation = self.imageLoader.LoadImages(10, 'images/stand/', 'stand', 'png', True)
        self.attackAnimation = self.imageLoader.LoadImages(14, 'images/attack/', 'attack', 'png', True)
        self.walkAnimation = self.imageLoader.ScaleImages(self.walkAnimation)
        self.standAnimation = self.imageLoader.ScaleImages(self.standAnimation)
        self.attackAnimation = self.imageLoader.ScaleImages(self.attackAnimation)
        self.image = self.standAnimation[0]
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.centerx = Width / 2
        self.rect.y = Height - self.rect.height

    def update(self):
        self.ctrl.getKeys()

        if self.ctrl.jumping:
            if not self.ctrl.falling:
                self.rect.y -= 5
            else:
                self.rect.y += 5
            if self.ctrl.jumpHeight == 0 and not self.ctrl.falling:
                self.ctrl.falling = True
                self.ctrl.jumpHeight = jumpHeight
            elif self.ctrl.jumpHeight == 0 and self.ctrl.falling:
                self.ctrl.jumping = False
                self.ctrl.falling = False
                self.ctrl.jumpHeight = jumpHeight
            self.ctrl.jumpHeight -= 1

        if self.ctrl.attacking:
            if self.game.frameCounter %2 == 0:
                self.image = self.attackAnimation[self.frameAttack]
                if self.ctrl.facingRight:
                    self.image = pg.transform.flip(self.image, True, False)
                self.mask = pg.mask.from_surface(self.image)
                self.frameAttack += 1
                if self.frameAttack + 1 > len(self.attackAnimation):
                    self.frameAttack = 0
                    self.ctrl.attacking = False

        elif self.ctrl.moveLeft:
            if self.game.frameCounter %2 == 0:
                self.image = self.walkAnimation[self.frameWalk]
                self.mask = pg.mask.from_surface(self.image)
            if self.rect.centerx > Width * 0.2:
                self.game.background.scroll = False
                self.rect.x -= 5
            else:
                self.game.background.scroll = True
            if not self.ctrl.jumping:
                self.frameWalk += 1
            if self.frameWalk + 1 > len(self.walkAnimation):
                self.frameWalk = 0

        elif self.ctrl.moveRight:
            if self.game.frameCounter %2 == 0:
                self.image = self.walkAnimation[self.frameWalk]
                self.image = pg.transform.flip(self.image, True, False)
                self.mask = pg.mask.from_surface(self.image)
            if self.rect.centerx < Width * 0.8:
                self.game.background.scroll = False
                self.rect.x += 5
            else:
                self.game.background.scroll = True
            if not self.ctrl.jumping:
                self.frameWalk += 1
            if self.frameWalk + 1 > len(self.walkAnimation):
                self.frameWalk = 0

        elif self.ctrl.standing:
            if not self.frameStandInvert:
                self.image = self.standAnimation[::-1][self.frameStand]
            else:
                self.image = self.standAnimation[self.frameStand]
            if self.ctrl.facingRight:
                self.image = pg.transform.flip(self.image, True, False)
            self.mask = pg.mask.from_surface(self.image)
            self.frameStand += 1
            if self.frameStand + 1 > len(self.standAnimation):
                self.frameStandInvert = not self.frameStandInvert
                self.frameStand = 0

        if self.ctrl.health == 0:
            self.kill()
