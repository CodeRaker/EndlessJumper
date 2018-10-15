import pygame as pg

class Gamestats(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self._layer = 5
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.font = pg.font.SysFont('Consolas', 30)
        self.image = self.font.render('', False, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

    def update(self):
        self.image = self.font.render('HP: ' + str(self.game.thor.health), False, (255,255,255))

class HealthBar(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self._layer = 5
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((100,20)) #width, height
        self.image.fill((0,255,0)) #color
        self.rect = self.image.get_rect() #get dimensions
        self.rect.y = 90
        self.rect.x = 50

    def update(self):
        self.image = pg.transform.scale(self.image, (self.game.thor.health, 20))
