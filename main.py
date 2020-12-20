import pygame
import datetime
from game import Game
pygame.init()

resolution = (400, 400)
FPS = 2
clock = pygame.time.Clock()

black_color = (0, 0, 0)
darkblue_color = (0, 34, 64)


game = Game()

pygame.display.set_caption("Snake")
window = pygame.display.set_mode(resolution)

lastTick = datetime.datetime.now()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT] and game.snake.direction != 'right':
		game.snake.direction = 'left'
	if key[pygame.K_RIGHT] and game.snake.direction != 'left':
		game.snake.direction = 'right'
	if key[pygame.K_UP] and game.snake.direction != 'down':
		game.snake.direction = 'up'
	if key[pygame.K_DOWN] and game.snake.direction != 'up':
		game.snake.direction = 'down'

	# draw background
	window.fill(darkblue_color)

	# move snake & detect if apple eaten
	delta = datetime.datetime.now() - lastTick
	if( delta.microseconds > 500000-10000*len(game.snake.body)):
		game.snake.move()
		lastTick = datetime.datetime.now()
		if game.snake.head.x == game.apple.x and game.snake.head.y == game.apple.y:
			game.apple_eaten()

	# detect if snake has eaten its tail
	for chunk in game.snake.body:
		if game.snake.head.x == chunk.x and game.snake.head.y == chunk.y:
			running = False
	
	# draw apple
	pygame.draw.rect(window, game.apple.color, game.apple)

	# draw snake body
	for chunk in game.snake.body:
		pygame.draw.rect(window, game.snake.body_color, chunk)

	# draw snake head
	pygame.draw.rect(window, game.snake.head_color, game.snake.head)

	#clock.tick(FPS)
	pygame.display.flip()

pygame.quit()