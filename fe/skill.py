import pygame
import math

class Skill(pygame.sprite.Sprite):
	def __init__(self, owner):
		super().__init__()
		self.image = pygame.Surface([20, 20])
		self.image = pygame.image.load("skill1.png").convert_alpha()
		self.orig_img = self.image
		self.rect = self.image.get_rect()

		self.owner = owner
		self.rect.x = owner.rect.x
		self.rect.y = owner.rect.y
		self.dir = owner.dir

	def update(self):
		self.rect.x += self.owner.skillspeed*math.cos(-math.pi*(self.dir+90)/180)
		self.rect.y += self.owner.skillspeed*math.sin(-math.pi*(self.dir+90)/180)