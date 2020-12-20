import pygame
from snake_chunk import Snake_chunk
pygame.init()

class Snake():

	def __init__(self):
		self.direction = 'right'

		self.head = Snake_chunk(40, 40)
		self.body = []

		self.head_color = (252, 194, 3) # yellowish orange
		self.body_color = (200, 150, 0) # darker yellowish orange
	
	def move(self):
		i = len(self.body)-1
		while i >= 0:
			if i == 0:
				self.body[i].x = self.head.x
				self.body[i].y = self.head.y
			else:
				self.body[i].x = self.body[i-1].x
				self.body[i].y = self.body[i-1].y
			i -= 1

		if self.direction == 'left':
			self.head.x -= 20
		if self.direction == 'right':
			self.head.x += 20
		if self.direction == 'up':
			self.head.y -= 20
		if self.direction == 'down':
			self.head.y += 20

		if self.head.x < 0:
			self.head.x = 380
		if self.head.x > 380:
			self.head.x = 0
		if self.head.y < 0:
			self.head.y = 380
		if self.head.y > 380:
			self.head.y = 0


	def eat(self):
		if self.direction == 'left':
			self.body.append(Snake_chunk(self.head.x+20, self.head.y))
		if self.direction == 'right':
			self.body.append(Snake_chunk(self.head.x-20, self.head.y))
		if self.direction == 'up':
			self.body.append(Snake_chunk(self.head.x, self.head.y+20))
		if self.direction == 'down':
			self.body.append(Snake_chunk(self.head.x, self.head.y-20))
		print(len(self.body))
		