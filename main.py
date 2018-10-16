import pygame as pg
from settings import *
from player import Player
from enemy import Enemy
from scenery import Background
from gamestats import PlayerStats
from colorpalette import RGBColors
from snowflakes import SnowFlake
from controller import GameController


class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((screen_width, screen_height))
        pg.display.set_caption('Little Thor')
        self.rgb = RGBColors()
        self.clock = pg.time.Clock()
        self.frame_rate = frame_rate
        self.frame_counter = 0
        self.running = True
        self.load_assets()

    def load_assets(self):
        self.ctrl = GameController(self)
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.enemies = pg.sprite.Group()
        self.snowflakes = pg.sprite.Group()
        self.Player = Player(self)
        self.Background = Background(self)
        self.Enemy = Enemy(self)
        self.Playerstats = PlayerStats(self)


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_v:
                self.ctrl.Environment.change_snow()

    def update(self):

        self.all_sprites.update()
        self.Background.update()
        enemy_collisions = pg.sprite.spritecollide(self.Player, self.enemies, False, pg.sprite.collide_mask)
        snowflake_collisions = pg.sprite.spritecollide(self.Player, self.snowflakes, False, pg.sprite.collide_mask)

        if enemy_collisions:
            for e in enemy_collisions:
                if self.ctrl.Player.attacking:
                    e.kill()
                    Enemy(self)
                elif e.cooldown == 0 and self.ctrl.Player.health > 0:
                    self.ctrl.Player.health -= 5
                    e.cooldown = 100

        if self.ctrl.Environment.snowing:
            if self.ctrl.Environment.snowflakes_count != 0:
                SnowFlake(self)
                self.ctrl.Environment.snowflakes_count -= 1

            if snowflake_collisions:
                for s in snowflake_collisions:
                    if not self.ctrl.Player.stand_lock:
                        s.collision = True

            if self.ctrl.Environment.wind_time != 0:
                self.ctrl.Environment.wind_time -= 1
            elif self.ctrl.Environment.wind_time == 0:
                self.ctrl.Environment.change_wind(self.frame_rate)

    def draw(self):
        self.Background.draw_background(self.screen)
        self.all_sprites.draw(self.screen)

    def run(self):
        while self.running:
            self.frame_counter += 1
            self.clock.tick(self.frame_rate)
            self.events()
            self.update()
            self.draw()
            pg.display.flip()
            if self.frame_counter == self.frame_rate:
                self.frame_counter = 0

g = Game()
while g.running:
    g.run()
pg.quit()
