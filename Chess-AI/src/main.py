import pygame #imports pygame
import sys #allows so that we can quit the application

from const import * #import all the stuff from const file
from game import Game

class Main:

	def __init__(self):
		pygame.init() #initializes pygame, always need to initialize it when using pygame
		self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
		#whenever we wanna create an attribute for class, use self
		pygame.display.set_caption('Chess')
		self.game = Game()

	def mainloop(self):

		screen = self.screen

		game = self.game
		
		while True:
			game.show_bg(screen)
			game.show_pieces(screen)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			


			pygame.display.update()

main = Main()
main.mainloop()
# init method is always called when creating an object
# so when main function is called it uses init method then the mainloop