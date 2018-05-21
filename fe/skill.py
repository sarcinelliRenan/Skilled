import pygame
import math

WHITE = (255, 255, 255)

class Skill(pygame.sprite.Sprite):

    def __init__(self, speed, cooldown, damage, width, height):
        super().__init__()

        self.speed = speed
        self.cooldown = cooldown
        self.damage = damage
        self.using = False
        self.direction = 0

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width=width
        self.height=height
        self.color=WHITE

        self.image = pygame.image.load("sprites/skill1.png").convert_alpha()
        self.orig_img = self.image
        self.rect = self.image.get_rect()

    def cast(self, player_x, player_y, direction):
        self.using = True
        self.direction = direction
        print(direction)
        self.rect.x = player_x
        self.rect.y = player_y

        print("fire")

    def update(self):
        if(self.using):
            self.rect.x += self.speed*math.cos(-math.pi*(self.direction+90)/180)
            self.rect.y += self.speed*math.sin(-math.pi*(self.direction+90)/180)
