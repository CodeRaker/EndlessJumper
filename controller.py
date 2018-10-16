import pygame as pg
from settings import *
from random import randint


class PlayerController:

    def __init__(self):
        self.init_movement()
        self.init_character_stats()

    def init_movement(self):
        self.standing = True
        self.move_left = False
        self.move_right = False
        self.jumping = False
        self.falling = False
        self.attacking = False
        self.facing_right = False
        self.stand_lock = False

    def init_character_stats(self):
        self.health = 100
        self.jump_height = jump_height

    def get_keys(self):

        pressed = pg.key.get_pressed()

        if pressed[pg.K_a]:
            self.move('left')

        if pressed[pg.K_d]:
            self.move('right')

        if pressed[pg.K_SPACE] or pressed[pg.K_w]:
            self.jump()

        if pressed[pg.K_q]:
            self.attack()

        elif not pressed[pg.K_a] and not pressed[pg.K_d]:
            self.stand_lock = False
            self.stand()

    def stand(self):
        if not self.stand_lock:
            self.clear_movement()
            self.standing = True

    def attack(self):
        if not self.attacking:
            self.attacking = True

    def move(self, direction):
        self.stand_lock = True
        if direction == 'left':
            self.move_right = False
            self.facing_right = False
            self.move_left = True
        elif direction == 'right':
            self.move_left = False
            self.facing_right = True
            self.move_right = True

    def jump(self):
        if not self.jumping:
            self.jump_init = True
            self.jumping = True

    def clear_movement(self):
        self.move_right = False
        self.move_left = False


class EnvironmentController:

    def __init__(self, game):
        self.game = game
        self.init_environment()

    def init_environment(self):
        self.snowing = False
        self.snowflakes_count = 0
        self.snowflakes_on_ground = 0
        self.wind_direction = randint(-1,1)
        self.wind_time = 1000

    def change_wind(self, frameRate):
        self.wind_time = randint(0,frameRate*60)
        self.wind_direction = randint(-1,1)

    def change_snow(self):
        if self.snowing:
            for snowflake in self.game.snowflakes:
                snowflake.kill()
        self.snowing = not self.snowing
        self.snowflakes_count = 300
        self.snowflakes_on_ground = 0


class GameController(PlayerController, EnvironmentController):
    
    def __init__(self, game):
        self.Player = PlayerController()
        self.Environment = EnvironmentController(game)
