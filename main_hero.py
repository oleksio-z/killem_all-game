"""Module with main hero logic"""
import pygame

class Hero:
	def __init__(self, killem_all):

		"""Initializing screen and settings"""
		self.screen = killem_all.screen
		self.screen_rect = killem_all.screen_rect
		self.settings = killem_all.settings

		"""Initializing MH image"""
		self.image = pygame.image.load('images/test.png')
		self.mh_rect = self.image.get_rect()

		"""Initializing moving"""
		self.moving_right = False
		self.moving_top = False
		self.moving_left = False
		self.moving_down = False
		self.x = float(self.mh_rect.x)
		self.y = float(self.mh_rect.y)

	def blit_mh(self):
		"""Blit character"""
		self.screen.blit(self.image, self.mh_rect)

