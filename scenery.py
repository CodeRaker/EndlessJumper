import pygame as pg
import os
from settings import *

class Background:

    def __init__(self, game):
        self.game = game
        self.ctrl = game.ctrl
        self.images = {}
        image_list = os.listdir('images/scene')
        for image in image_list:
            original_image = pg.image.load('images/scene/' + image).convert_alpha()
            scaled_image = pg.transform.scale(original_image, (screen_width, screen_height))
            self.images[str(image)] = scaled_image

        self.scroll = False
        self.image_mountains = self.images['mountains.png']
        self.image_grass_back = self.images['grass-back.png']
        self.image_grass_front = self.images['grass-front.png']
        self.image_trees = self.images['trees.png']
        self.image_rect_mountains = self.image_mountains.get_rect()
        self.image_rect_grass_back = self.image_grass_back.get_rect()
        self.image_rect_grass_front = self.image_grass_front.get_rect()
        self.image_rect_trees = self.image_trees.get_rect()


    def update(self):
        if self.scroll and self.ctrl.Player.stand_lock:
            if self.ctrl.Player.move_left:
                self.image_rect_mountains.x += 1
                self.image_rect_grass_back.x += 2
                self.image_rect_grass_front.x += 2
                self.image_rect_trees.x += 2
                for enemy in self.game.enemies:
                    enemy.rect.x += 2
                for snowflake in self.game.snowflakes:
                    snowflake.rect.x += 2
            else:
                self.image_rect_mountains.x -= 1
                self.image_rect_grass_back.x -= 2
                self.image_rect_grass_front.x -= 2
                self.image_rect_trees.x -= 2
                for enemy in self.game.enemies:
                    enemy.rect.x -= 2
                for snowflake in self.game.snowflakes:
                    snowflake.rect.x -= 2


    def draw_background_pre(self, screen):

        screen.blit(self.images['sky.png'], (0,0))

        screen.blit(self.image_mountains, (self.image_rect_mountains.x,0))
        if self.image_rect_mountains.x < 0:
            screen.blit(self.image_mountains, (self.image_rect_mountains.right, 0))
        elif self.image_rect_mountains.right > screen_width:
            screen.blit(self.image_mountains, (self.image_rect_mountains.left - self.image_rect_mountains.width, 0))
        if self.image_rect_mountains.x < -screen_width or self.image_rect_mountains.x > screen_width:
            self.image_rect_mountains.x = 0

        screen.blit(self.image_trees, (self.image_rect_trees.x,0))
        if self.image_rect_trees.x < 0:
            screen.blit(self.image_trees, (self.image_rect_trees.right, 0))
        elif self.image_rect_trees.right > screen_width:
            screen.blit(self.image_trees, (self.image_rect_trees.left - self.image_rect_trees.width, 0))
        if self.image_rect_trees.x < -screen_width or self.image_rect_trees.x > screen_width:
            self.image_rect_trees.x = 0

        screen.blit(self.image_grass_back, (self.image_rect_grass_back.x,0))
        if self.image_rect_grass_back.x < 0:
            screen.blit(self.image_grass_back, (self.image_rect_grass_back.right, 0))
        elif self.image_rect_grass_back.right > screen_width:
            screen.blit(self.image_grass_back, (self.image_rect_grass_back.left - self.image_rect_grass_back.width, 0))
        if self.image_rect_grass_back.x < -screen_width or self.image_rect_grass_back.x > screen_width:
            self.image_rect_grass_back.x = 0

    def draw_background_post(self, screen):
        screen.blit(self.image_grass_front, (self.image_rect_grass_front.x,0))
        if self.image_rect_grass_front.x < 0:
            screen.blit(self.image_grass_front, (self.image_rect_grass_front.right, 0))
        elif self.image_rect_grass_front.right > screen_width:
            screen.blit(self.image_grass_front, (self.image_rect_grass_front.left - self.image_rect_grass_front.width, 0))
        if self.image_rect_grass_front.x < -screen_width or self.image_rect_grass_front.x > screen_width:
            self.image_rect_grass_front.x = 0
