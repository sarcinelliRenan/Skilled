import pygame
import math

WHITE = (255, 255, 255)
 
class Player(pygame.sprite.Sprite):
 
    def __init__(self, color, width, height, speed):
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        self.width=width
        self.height=height
        self.color=color
        self.speed=speed
        self.angle=0
 
       # pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
 
        self.image = pygame.image.load("sprites/hero1.png").convert_alpha()
        self.orig_img = self.image

        self.rect = self.image.get_rect()
 
    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, pixels):
        self.rect.y -= pixels
 
    def moveBackward(self, pixels):
        self.rect.y += pixels

    def rotate(self, vector):
        self.angle = math.atan2(self.rect.x-vector.x,self.rect.y-vector.y)*180/math.pi
        self.image = pygame.transform.rotozoom(self.orig_img, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.moveLeft(2)
        if keys[pygame.K_d]:
            self.moveRight(2)
        if keys[pygame.K_w]:
            self.moveForward(2);
        if keys[pygame.K_s]:
            self.moveBackward(2);
            
        mouseX, mouseY = pygame.mouse.get_pos()
        vetMouse=pygame.math.Vector2(mouseX,mouseY)
        self.rotate(vetMouse)

    def handleEvent(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("fire")
