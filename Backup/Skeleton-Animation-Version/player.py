import pygame as pg
from settings import *
from random import randint
vec = pg.math.Vector2

class Thor(pg.sprite.Sprite):
    def __init__(self, game, bodypart):
        self.game = game

        self.bodypart = bodypart
        self.groups = game.all_sprites, game.tBody

        #layer 2
        if self.bodypart in ['right_lower_arm']:
            self._layer = 2

        #layer 3
        if self.bodypart in ['right_upper_arm','right_leg']:
            self._layer = 3

        #layer 4
        elif self.bodypart in ['torso']:
            self._layer = 4

        #layer 5
        elif self.bodypart in ['left_leg']:
            self._layer = 5

        #layer 6
        elif self.bodypart in ['cloth']:
            self._layer = 6

        #layer 7
        elif self.bodypart in ['necklace','face']:
            self._layer = 7

        #layer 8
        elif self.bodypart in ['beard','eyebrows','hair']:
            self._layer = 8

        #layer 9
        elif self.bodypart in ['left_upper_arm']:
            self._layer = 9

        #layer 10
        elif self.bodypart in ['hammer']:
            self._layer = 10

        #layer 11
        elif self.bodypart in ['left_lower_arm']:
            self._layer = 11


        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load('images/player/' + bodypart + '.png').convert_alpha()

        #set imagesizes
        if self.bodypart == 'hammer':
            self.image = pg.transform.scale(self.image, (self.image.get_width() // 5, self.image.get_height() // 5))
        else:
            self.image = pg.transform.scale(self.image, (self.image.get_width() // 10, self.image.get_height() // 10))
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

        #create callable vars for each sprite
        if bodypart == 'torso':
            self.rect.x = Width // 2
            self.rect.y = Height - (self.rect.height*2)
            self.game.torso = self
        else:
            component = 'self.game.' + bodypart + ' = self'
            exec(component)

        #init for rotation
        if self.bodypart == 'right_lower_arm':
            self.initAngle = -30
        elif self.bodypart == 'hammer':
            self.initAngle = 55
        else:
            self.initAngle = 0
        self.angle = self.initAngle
        self.orig_image = self.image
        self.rotate()

    def update(self):
        ########
        # LEGS #
        ########
        if self.bodypart == 'left_leg':
            self.rect.x = self.game.torso.rect.bottomleft[0] - 3                                        #anchor to torso x
            self.rect.y = self.game.torso.rect.centery + (self.game.torso.rect.height // 3) - 4             #anchor to torso y

        elif self.bodypart == 'right_leg':
            self.rect.x = self.game.torso.rect.bottomleft[0] - (self.game.torso.rect.width // 3) - 3   #anchor to torso x
            self.rect.y = self.game.torso.rect.centery + (self.game.torso.rect.height // 3) - 8       #anchor to torso y

        #arms
        elif self.bodypart == 'left_upper_arm':
            self.rect.x = self.game.torso.rect.topright[0] - 15
            self.rect.y = self.game.torso.rect.topleft[1] + 5
        elif self.bodypart == 'left_lower_arm':
            self.rect.x = self.game.left_upper_arm.rect.bottomleft[0] - 15
            self.rect.y = self.game.left_upper_arm.rect.bottomleft[1] - 7
        elif self.bodypart == 'right_upper_arm':
            self.rect.x = self.game.torso.rect.topleft[0] - 5
            self.rect.y = self.game.torso.rect.topright[1] + 5
        elif self.bodypart == 'right_lower_arm':
            self.rect.x = self.game.right_upper_arm.rect.bottomleft[0] - 13
            self.rect.y = self.game.right_upper_arm.rect.bottomleft[1] - 8

        #head
        elif self.bodypart == 'face':
            self.rect.x = self.game.torso.rect.centerx - 25
            self.rect.y = self.game.torso.rect.topleft[1] - 50
        elif self.bodypart == 'beard':
            self.rect.x = self.game.face.rect.x
            self.rect.y = self.game.face.rect.y + 36
        elif self.bodypart == 'hair':
            self.rect.x = self.game.face.rect.x + 6
            self.rect.y = self.game.face.rect.y - 6
        elif self.bodypart == 'eyebrows':
            self.rect.x = self.game.face.rect.x + 2
            self.rect.y = self.game.face.rect.y + 17

        #clothes
        elif self.bodypart == 'cloth':
            self.rect.centerx = self.game.torso.rect.centerx
            self.rect.centery = self.game.torso.rect.centery
        elif self.bodypart == 'necklace':
            self.rect.centerx = self.game.torso.rect.centerx - 5
            self.rect.centery = self.game.torso.rect.centery - 5

        #weapons
        elif self.bodypart == 'hammer':
            self.rect.x = self.game.left_lower_arm.rect.bottomleft[0] - 95
            self.rect.y = self.game.left_lower_arm.rect.bottomleft[1] - 105

    def rotate(self):
        self.image = pg.transform.rotozoom(self.orig_image, self.angle, 1)
        #self.rect = self.image.get_rect(topleft=self.rect.topleft)
        #self.rect = self.image.get_rect(center=self.rect.center)

        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
