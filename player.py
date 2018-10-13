import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self._layer = 2
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load('images/player_01.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (75,150))
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x = 100
        self.rect.y = Height - self.rect.height

        #Boost variables
        self.boost = False
        self.boostDepleted = False
        self.boostCount = 0

        #Attack variables
        self.slashAttack = False

    def update(self):

        #Boost events
        if not self.boostDepleted and self.boost:
            self.rect.y -= 5
            self.boostCount += 1
            if self.boostCount > 25:
                self.boostDepleted = True
        elif not self.boost and self.boostCount > 0 or self.boostDepleted:
            self.rect.y += 5
            self.boostCount -= 1
            if self.boostCount == 0:
                self.boostDepleted = False

        if slashAttack:
            slashAttack = False

        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
        #self.mask = pg.mask.from_surface(self.image)
