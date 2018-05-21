import pygame
import math
from player import Player
from skill import Skill

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
SCREENWIDTH=800
SCREENHEIGHT=600
FPS=60
 
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TreeGen")

all_sprites_list = pygame.sprite.Group()

player = Player(WHITE, 60, 80, 70)
skill = Skill(5,0,0, 60, 80)

all_sprites_list.add(player)
all_sprites_list.add(skill)

carryOn = True
clock=pygame.time.Clock()

while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
                player.handleEvent(event)
            if event.type==pygame.MOUSEBUTTONDOWN:
                skill.cast(player.rect.x, player.rect.y, player.angle)

        all_sprites_list.update()
        screen.fill(PURPLE)

        all_sprites_list.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)
        
pygame.quit()
