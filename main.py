import pygame as pg
from settings import *
from player import *
from colorpalette import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Width, Height))
        pg.display.set_caption('Little Thor')
        self.rgb = RGBColors()
        self.clock = pg.time.Clock()
        self.frameRate = frameRate
        self.frameCounter = 0
        self.running = True
        self.loadAssets()

    def loadAssets(self):
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.thor = Thor(self)


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.KEYDOWN and event.key == pg.K_v:
                self.thor.debug = not self.thor.debug

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(self.rgb.gray)
        self.all_sprites.draw(self.screen)

    def run(self):
        while self.running:
            self.frameCounter += 1
            self.clock.tick(self.frameRate)
            self.events()
            self.update()
            self.draw()
            pg.display.flip()
            if self.frameCounter == self.frameRate:
                self.frameCounter = 0

g = Game()
while g.running:
    g.run()
pg.quit()
