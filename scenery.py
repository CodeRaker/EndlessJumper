import pygame as pg
from settings import *

class Background(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.groups = game.all_sprites
        self._layer = 1
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load('images/background.png').convert()
        self.image = pg.transform.scale(self.image, (Width, Height))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.scroll = False
        self.debug = False

    def update(self):
        if self.scroll and not self.game.thor.standStill:
            if self.game.thor.moveLeft:
                if self.debug:
                    print(str('scrollleft'))
                self.rect.x += 2
                for enemy in self.game.enemies:
                    enemy.rect.x += 2
            else:
                if self.debug:
                    print(str('scrollright'))
                self.rect.x -= 2
                for enemy in self.game.enemies:
                    enemy.rect.x -= 2
        if self.rect.left < 0:
            self.game.screen.blit(self.image, (self.rect.right, 0))
        elif self.rect.right > Width:
            self.game.screen.blit(self.image, (self.rect.left - self.rect.width, 0))
        if self.rect.x < -Width or self.rect.x > Width:
            self.rect.x = 0
