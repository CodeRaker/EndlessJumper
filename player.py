import pygame as pg
from settings import *
from random import randint
from imageloader import ImageLoader
vec = pg.math.Vector2


class Player(ImageLoader, pg.sprite.Sprite):

    def __init__(self, game):
        self.game = game
        self.ctrl = game.ctrl
        self.ImageLoader = ImageLoader()
        self.groups = game.all_sprites
        self._layer = 3
        pg.sprite.Sprite.__init__(self, self.groups)
        self.init_graphics()

    def init_graphics(self):
        self.frame_selector_walk = 0
        self.frame_selector_walk_invert = False
        self.frame_selector_stand = 0
        self.frame_selector_stand_invert = False
        self.frame_selector_attack = 0
        self.animation_walk = self.ImageLoader.load_images(7, 'images/walk/walk', 'png', True)
        self.animation_stand = self.ImageLoader.load_images(10, 'images/stand/stand', 'png', True)
        self.animation_attack = self.ImageLoader.load_images(14, 'images/attack/attack', 'png', True)
        self.animation_walk = self.ImageLoader.down_scale_images(self.animation_walk, 2)
        self.animation_stand = self.ImageLoader.down_scale_images(self.animation_stand, 2)
        self.animation_attack = self.ImageLoader.down_scale_images(self.animation_attack, 2)
        self.image = self.animation_stand[0]
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.centerx = screen_width / 2
        self.rect.y = screen_height - (self.rect.height + 10)

    def update(self):
        self.ctrl.Player.get_keys()
        if self.ctrl.Player.jumping:
            if not self.ctrl.Player.falling:
                self.rect.y -= 5
            else:
                self.rect.y += 5
            if self.ctrl.Player.jump_height == 0 and not self.ctrl.Player.falling:
                self.ctrl.Player.falling = True
                self.ctrl.Player.jump_height = jump_height
            elif self.ctrl.Player.jump_height == 0 and self.ctrl.Player.falling:
                self.ctrl.Player.jumping = False
                self.ctrl.Player.falling = False
                self.ctrl.Player.jump_height = jump_height
            self.ctrl.Player.jump_height -= 1
        if self.ctrl.Player.attacking:
            if self.game.frame_counter %2 == 0:
                self.image = self.animation_attack[self.frame_selector_attack]
                if self.ctrl.Player.facing_right:
                    self.image = pg.transform.flip(self.image, True, False)
                self.mask = pg.mask.from_surface(self.image)
                self.frame_selector_attack += 1
                if self.frame_selector_attack + 1 > len(self.animation_attack):
                    self.frame_selector_attack = 0
                    self.ctrl.Player.attacking = False
        elif self.ctrl.Player.move_left:
            if self.game.frame_counter %2 == 0:
                self.image = self.animation_walk[self.frame_selector_walk]
                self.mask = pg.mask.from_surface(self.image)
            if self.rect.centerx > screen_width * 0.2:
                self.game.Background.scroll = False
                self.rect.x -= 5
            else:
                self.game.Background.scroll = True
            if not self.ctrl.Player.jumping:
                self.frame_selector_walk += 1
            if self.frame_selector_walk + 1 > len(self.animation_walk):
                self.frame_selector_walk = 0
        elif self.ctrl.Player.move_right:
            if self.game.frame_counter %2 == 0:
                self.image = self.animation_walk[self.frame_selector_walk]
                self.image = pg.transform.flip(self.image, True, False)
                self.mask = pg.mask.from_surface(self.image)
            if self.rect.centerx < screen_width * 0.8:
                self.game.Background.scroll = False
                self.rect.x += 5
            else:
                self.game.Background.scroll = True
            if not self.ctrl.Player.jumping:
                self.frame_selector_walk += 1
            if self.frame_selector_walk + 1 > len(self.animation_walk):
                self.frame_selector_walk = 0

        elif self.ctrl.Player.standing:
            if not self.frame_selector_stand_invert:
                self.image = self.animation_stand[::-1][self.frame_selector_stand]
            else:
                self.image = self.animation_stand[self.frame_selector_stand]
            if self.ctrl.Player.facing_right:
                self.image = pg.transform.flip(self.image, True, False)
            self.mask = pg.mask.from_surface(self.image)
            self.frame_selector_stand += 1
            if self.frame_selector_stand + 1 > len(self.animation_stand):
                self.frame_selector_stand_invert = not self.frame_selector_stand_invert
                self.frame_selector_stand = 0
        if self.ctrl.Player.health == 0:
            self.kill()
