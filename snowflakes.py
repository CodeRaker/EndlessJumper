from random import randint
import pygame as pg
from settings import *


class SnowFlake(pg.sprite.Sprite):

    def __init__(self, game):
        self.game = game
        self.ctrl = game.ctrl
        self._layer = 3
        self.groups = game.all_sprites, game.snowflakes
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load('images\snowflake.png').convert_alpha()
        self.randsize = randint(3,6)
        self.image = pg.transform.scale(self.image, (self.randsize, self.randsize))
        self.rect = self.image.get_rect()
        self.rect.y = randint(-screen_height,0)
        self.rect.x = randint(0,screen_width)
        self.ttl = 500
        self.collision = False
        self.has_spawned_clone = False

    def update(self):
        if not self.collision:
            self.rect.y += 1
            self.rect.x += randint(-1,1) + self.ctrl.Environment.wind_direction
        if self.ttl == 0:
            self.kill()
            self.ctrl.Environment.snowflakes_on_ground -= 1
        if self.rect.y > screen_height - self.rect.height:
            self.collision = True
        if self.collision == True:
            if not self.has_spawned_clone:
                SnowFlake(self.game)
                self.has_spawned_clone = True
                self.ctrl.Environment.snowflakes_on_ground +=1
            self.ttl -= 1
        if self.rect.x > screen_width + self.rect.width:
            self.rect.x = 0
        elif self.rect.x < 0 - self.rect.width:
            self.rect.x = screen_width
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.center = center
        self.collision = False
