import pygame as pg

class HealthPoints(pg.sprite.Sprite):

    def __init__(self, game):
        self.game = game
        self.ctrl = game.ctrl
        self._layer = 5
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.font = pg.font.SysFont('Consolas', 30)
        self.image = self.font.render('', False, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

    def update(self):
        self.image = self.font.render('HP: ' + str(self.ctrl.Player.health), False, (255,255,255))


class HealthBar(pg.sprite.Sprite):

    def __init__(self, game):
        self.game = game
        self.ctrl = game.ctrl
        self._layer = 5
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((100,20))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.y = 90
        self.rect.x = 50

    def update(self):
        self.image = pg.transform.scale(self.image, (self.ctrl.Player.health, 20))


class PlayerStats(HealthPoints, HealthBar, pg.sprite.Sprite):
    
    def __init__(self, game):
        self.HealthPoints = HealthPoints(game)
        self.HealthBar = HealthBar(game)
