import pygame as pg
from settings import *
from random import randint

class Enemy(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self._layer = 3
        self.groups = game.all_sprites, game.enemies
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load('images/enemies/hacker.png')
        self.image = pg.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect() #get dimensions
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x = randint(-100,0)
        self.rect.y = Height - self.rect.height
        self.die = False
        self.cooldown = 0

    def update(self):
        self.rect.x += 1
        if self.rect.x > Width:
            self.rect.x = randint(-100,0)

        if self.cooldown > 0:
            self.cooldown -= 5

        if self.die:
            self.kill()
            self.game.enemyCount += 1
