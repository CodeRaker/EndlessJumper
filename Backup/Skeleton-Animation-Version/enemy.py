import pygame as pg
from settings import *
from random import randint

class Enemy(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self._layer = 2
        self.groups = game.all_sprites, game.enemies
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load('images/player_01.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (25,50))
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x = randint(-100,0)
        self.rect.y = Height - self.rect.height
        self.die = False

    def update(self):
        self.rect.x += 1
        if self.rect.x > Width:
            self.rect.x = randint(-100,0)

        if self.die:
            self.kill()
            self.game.enemyCount += 2

        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
