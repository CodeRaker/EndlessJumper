import pygame as pg
from settings import *
from player import *
from enemy import *
from colorpalette import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Width, Height))
        pg.display.set_caption('Endless Jumper')
        self.rgb = RGBColors()
        self.clock = pg.time.Clock()
        self.frameRate = 60
        self.running = True
        self.loadAssets()

    def loadAssets(self):
        self.enemyCount = 1
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.player = Player(self)
        self.enemies = pg.sprite.Group()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

        pressed = pg.key.get_pressed()

        # if pressed[pg.K_w]:
        #     self.player.rect.y -= 3
        # if pressed[pg.K_s]:
        #     self.player.rect.y += 3
        if pressed[pg.K_a]:
            self.player.rect.x -= 3
        if pressed[pg.K_d]:
            self.player.rect.x += 3
        if pressed[pg.K_SPACE]:
            if not self.player.boost:
                self.player.boost = True
        if not pressed[pg.K_SPACE]:
            if self.player.boost:
                self.player.boost = False

        enemyHits = pg.sprite.spritecollide(self.player, self.enemies, False, pg.sprite.collide_mask)
        if enemyHits:
            for enemy in enemyHits:
                enemy.die = True


    def update(self):
        if self.enemyCount != 0:
            Enemy(self)
            self.enemyCount -= 1
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(self.rgb.black)
        self.all_sprites.draw(self.screen)

    def run(self):
        while self.running:
            self.clock.tick(self.frameRate)
            self.events()
            self.update()
            self.draw()
            pg.display.flip()

g = Game()
while g.running:
    g.run()
pg.quit()
