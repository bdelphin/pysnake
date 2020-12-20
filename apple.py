import pygame
pygame.init()


class Apple(pygame.Rect):

	def __init__(self, x, y):
		super().__init__(x, y, 20, 20)
		self.color = (128, 252, 3) # lime