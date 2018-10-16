import pygame as pg


class WidgetBackground(pg.sprite.Sprite):

    def __init__(self, game):
        self._layer = 4
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load('images/stats-widget.png')
        self.image = pg.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.rect = self.image.get_rect()
        self.rect.x = 15
        self.rect.y = 15


class HealthPoints(pg.sprite.Sprite):

    def __init__(self, game):
        self.game = game
        self.ctrl = game.ctrl
        self._layer = 5
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.font = pg.font.SysFont('Consolas', 16)
        self.image = self.font.render('', False, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.right = 120
        self.rect.y = 88

    def update(self):
        self.image = self.font.render(str(self.ctrl.Player.health), False, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.right = 141
        self.rect.y = 88


class HealthBar(pg.sprite.Sprite):

    def __init__(self, game):
        self.game = game
        self.ctrl = game.ctrl
        self._layer = 5
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.healthbar_width = 118
        self.image = pg.Surface((self.healthbar_width,10))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.y = 112
        self.rect.x = 43

    def update(self):
        if self.ctrl.Player.health == 100:
            self.image = pg.transform.scale(self.image, (self.healthbar_width, 10))
        elif self.ctrl.Player.health > 0:
            if self.ctrl.Player.health == 5:
                float_health = float('0.0' + str(self.ctrl.Player.health))
            else:
                float_health = float('0.' + str(self.ctrl.Player.health))
            self.image = pg.transform.scale(self.image, (round(self.healthbar_width * float_health), 10))
        else:
            self.image = pg.transform.scale(self.image, (0, 0))


class PlayerStats(HealthPoints, HealthBar, WidgetBackground, pg.sprite.Sprite):

    def __init__(self, game):
        self.HealthPoints = HealthPoints(game)
        self.HealthBar = HealthBar(game)
        self.WidgetBackground = WidgetBackground(game)
