import pygame
import sys
from settings import Settings
from main_hero import Hero

class Killem_all:
	""" Initializing game"""
	def __init__(self):
		pygame.init()

		"""Initializing screen"""
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption('Killem_All')

		"""Initializing main hero"""
		self.player = Hero(self)

	def run(self):
		while True:
			self._event_manager()
			self._update_screen()

	def _event_manager(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()


	def _update_screen(self):
		"""Screen updater"""
		self.screen.fill(self.settings.background)
		self.player.blit_mh()
		pygame.display.flip()

if __name__ == '__main__':
	Killem_all = Killem_all()
	Killem_all.run()