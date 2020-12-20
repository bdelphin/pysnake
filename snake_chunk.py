import pygame
pygame.init()


class Snake_chunk(pygame.Rect):

	def __init__(self, x, y):
		super().__init__(x, y, 20, 20)
		
