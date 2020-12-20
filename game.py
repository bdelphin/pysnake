import random
from apple import Apple
from snake import Snake

class Game():

	def __init__(self):
		self.new_apple()
		self.snake = Snake()

	def apple_eaten(self):
		self.snake.eat()
		self.new_apple()
		while not self.apple_collision_clear():
			self.new_apple()

	def apple_collision_clear(self):
		for chunk in self.snake.body:
			if self.apple.x == chunk.x and self.apple.y == chunk.y:
				return False
		return True

	def new_apple(self):
		print("New Apple !")
		self.apple = Apple(random.randint(0, 19)*20,random.randint(0, 19)*20)