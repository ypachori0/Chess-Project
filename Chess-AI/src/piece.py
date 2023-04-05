import os

class Piece:

	def __init__(self, name, color, value, texture, texture_rect=None):
		self.name = name
		self.color = color

		value_sign = 1 if color == 'white' else -1 #black pieces assigned negative values and white pieces assigned positive values
		self.value = value * value_sign
		self.moves = []
		self.moved = False
		self.texture = texture
		self.set_texture()
		self.texture_rect = texture_rect

	def set_texture(self, size=80):
		self.texture = os.path.join(
				f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')

	def add_moves(self, move):
		self.moves.append(move)

class Pawn(Piece):

	def __init__(self, color):
		self.dir = -1 if color == 'white' else 1
		super().__init__('pawn', color, 1.0)

class Knight(Piece):
	def __init__(self, color):
		super().__init__('knight', color, 3.0)

class Bishop(Piece):
	def __init__(self, color):
		super().__init__('bishop', color, 3.001) #this is just saying that bishops are a *little* more important than knights

class Rook):
	def __init__(self, color):
		super().__init__('rook', color, 5.0)

class Queen(Piece):
	def __init__(self, color):
		super().__init__('queen', color, 9.0)

class King(Piece):
	def __init__(self, color):
		super().__init__('king', color, 10000.0) #any high value can be used, this is just telling the ai that the king is the most important piece on the board
