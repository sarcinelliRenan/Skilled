import pygame
import math
from skill import Skill

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = [20, 20]
        self.image = pygame.Surface(self.size)
        self.image = pygame.image.load("hero1.png").convert_alpha()
        self.orig_img = self.image
        self.rect = self.image.get_rect()
        self.center = [self.rect.x + self.size[0]/2, self.rect.y + self.size[1]/2]

        self.life = 100
        self.speed = 2
        self.cooldown_timer = 0
        self.cooldown = 0.2
        self.damage = 2
        self.skillspeed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_d]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_w]:
            self.rect.move_ip(0, -self.speed)
        if keys[pygame.K_s]:
            self.rect.move_ip(0, self.speed)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        vector=pygame.math.Vector2(mouse_x,mouse_y) 
        self.dir = math.atan2(self.rect.x-vector.x,self.rect.y-vector.y)*180/math.pi
        self.image = pygame.transform.rotozoom(self.orig_img, self.dir, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.center = [self.rect.x + self.size[0]/2, self.rect.y + self.size[1]/2]

    def cast(self):
    	if(self.cooldown_timer >= self.cooldown):
    		self.cooldown_timer = 0
    		skill = Skill(self)
    		return skill
    	else:
    		return False