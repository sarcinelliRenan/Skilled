import pygame
from player import Player
import math

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
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Game(object):
	def __init__(self):
		self.characters = pygame.sprite.Group()
		self.skills = pygame.sprite.Group()
		
		self.player = Player()
		self.characters.add(self.player)

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
			else:
				if event.type == pygame.MOUSEBUTTONDOWN:
					skill = self.player.cast()
					if(skill != False):
						self.skills.add(skill)

		return False

	def run_logic(self):
		self.characters.update()
		self.skills.update()

		for skill in self.skills:
			if skill.rect.x >= SCREEN_WIDTH or skill.rect.x <= 0 or skill.rect.y >= SCREEN_HEIGHT or skill.rect.y <= 0:
				self.skills.remove(skill)

		for character in self.characters:
			if character.center[1] + character.size[1]/2 > SCREEN_HEIGHT:
				character.rect.y = SCREEN_HEIGHT - character.size[1]
			elif character.center[1] - character.size[1]/2 < 0:
				character.rect.y = 0
			
			if character.center[0] + character.size[0]/2 > SCREEN_WIDTH:
				character.rect.x = SCREEN_WIDTH - character.size[0]
			elif character.center[0] - character.size[0]/2 < 0:
				character.rect.x = 0

			character.cooldown_timer += 1/FPS

	def display_frame(self, screen):
		screen.fill(PURPLE)

		pygame.font.init()
		myfont = pygame.font.SysFont('Arial', 50)
		HUB = myfont.render(str(self.player.life) + " " + str(1 if self.player.cooldown_timer > self.player.cooldown else 0), False, YELLOW)
		
		screen.blit(HUB,(SCREEN_WIDTH-100,SCREEN_HEIGHT-50))

		self.characters.draw(screen)
		self.skills.draw(screen)
		pygame.display.flip()

def main():
	pygame.init()
	size = [SCREEN_WIDTH, SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption("Skilled")

	done = False
	clock = pygame.time.Clock()

	game = Game()

	while not done:
		# processa entrada do teclado, mouse, joystick e checa se o jogo terminou
		done = game.handle_events()

		# roda a logica do jogo
		game.run_logic()

		# mostra na tela o frame atual do jogo
		game.display_frame(screen)

		# garante que o jogo rode no fps desejado
		clock.tick(FPS)

	pygame.quit()

if __name__ == "__main__":
	main()
