import random

class TicTacToeBoard:

	def __init__(self, length):
		self.size = length
		self.moves = 0
		self.start = True
		self.player = 'O'
		self.user_score = 0
		self.comp_score = 0
		self.board = [' '] * (self.size * self.size)

		self.win_combos = []
		self.combo_dict = {}
		# winning rows
		for row in range(0, self.size):
			columns = []
			for col in range(0, self.size):
				columns.append((row * self.size) + col)
			tpl = tuple(columns)
			self.win_combos.append(tpl)
			self.combo_dict[tpl] = [0,0]

		# winning columns
		for col in range(0, self.size):
			rows = []
			for row in range(0, self.size):
				rows.append(col + (row * self.size))
			tpl = tuple(rows)
			self.win_combos.append(tpl)
			self.combo_dict[tpl] = [0,0]

		# winning diags
		diag1 = []
		i = 0
		while i < self.size:
			diag1.append((i) * (self.size + 1))
			i += 1
		tpl = tuple(diag1)
		self.win_combos.append(tpl)
		self.combo_dict[tpl] = [0,0]

		diag2 = []
		j = 0
		while j < self.size:
			diag2.append((j + 1) * (self.size - 1))
			j += 1
		tpl = tuple(diag2)
		self.win_combos.append(tpl)
		self.combo_dict[tpl] = [0,0]

	def make_move(self, move):
		"""Make the player's move on the game board. X=user, O=computer."""
		if self.player == 'O':
			print("Computer's turn")
		else:
			print('Your turn')
		self.board[move] = self.player
		self.print_board()

	def make_comp_move(self):
		# make move to win
		if self.moves > 1:
			count = 0
			move = 0
			for combo in self.win_combos:
				


		else:
			mul = (self.size - 1) / 2
			center = (self.size * mul) + mul
			center = int(center)
			if self.is_open(center):
				self.make_move(center)
			else:
				corners = [0, (self.size - 1), (self.size * (self.size - 1)),
				           ((self.size + 1) * (self.size - 1))]
				moved = False
				for corner in corners:
					if self.is_open(corner):
						self.make_move(corner)
						moved = True
						break
				if not moved:
					# other
					pass

		self.moves += 1
		winner = self.check_for_winner()
		self.player = 'X'

	def check_input(self, move):
		"""Return whether or not the user input has valid length, row, column
		   and position.
		"""
		if len(move) == 2:
			if not move[0].isdigit(): # first char must be digit
				print('Oops, you entered an invalid row.')
				return False
			int_row = int(move[0]) - 1
			# check for valid row
			if int_row >= self.size:
				print('Oops, you entered an invalid row.')
				return False
			# check for valid column
			col = move[1]
			int_col = ord(col) - 97
			if int_col >= self.size or int_col < 0:
				print('Oops, you entered an invalid column.')
				return False
			# check that position is available
			if not self.is_open((self.size * int_row) + int_col):
				print('Oops, that position is taken.')
				return False
			return True
		print('Invalid input.')
		return False

	def check_for_winner(self):
		"""Check if player has acquired a winning combination.
		   If so, return player. Otherwise, return ' '.
	    """
		for combo in self.win_combos:
			current = True
			for idx in combo:
				if self.board[idx] != self.player:
					current = False
					break
			if current:
				return self.player

		# if no winner is found and board is full, it is a Cat's game (tie)
		if self.moves == (self.size * self.size):
			return 'C'
		return ' '

	def print_scores(self):
		"""Print the total score of the user and the computer.
		   Scores reset if the user exits the program.
		"""
		print('\n*SCORES:\n'\
			  '*You: ' + str(self.user_score) + '\n'\
			  '*Computer: ' + str(self.comp_score) + '\n')

	def play_again(self):
		"""Return whether or not the user wants to play another game.
		   If so, reset the board attributes.
		"""
		play_again = input('Play again? (Y/N): ')
		if play_again == 'Y' or play_again == 'y':
			self.moves = 0
			self.start = True
			self.player = 'O'
			self.board = [' '] * (self.size * self.size)
			self.print_board()
			return True
		return False

	def is_open(self, move):
		if self.board[move] == ' ':
			return True
		return False

	def print_board(self):
		"""Print the current state of the game board.
		   Spots taken by the user are represented by 'X'.
		   Spots taken by the computer are represented by 'O'.
		"""
		board_str = ''
		start_ascii = ord('A')
		board_str += '      A'
		for i in range(1, self.size):
			board_str += '         ' + chr(start_ascii + i)
		board_str += '\n'

		for row in range(0, self.size):
			board_str += '           '
			for col in range(0, self.size - 1):
				board_str += '|         '
			board_str += '\n'

			board_str += str(row + 1) + ' '
			for col in range(0, self.size):
				index = (self.size * row) + col
				board_str += ('    %s    |' % self.board[index])
			board_str = board_str[:-1]
			board_str += '\n'
			board_str += '           '
			for col in range(0, self.size - 1):
				board_str += '|         '
			board_str += '\n'

			if row < self.size - 1:
				board_str += '  '
				board_str += '-' * ((self.size * 10) - 2)
				board_str += '\n'

		print(board_str + '\n')


def play_game(length):
	"""Play a game of tic-tac-toe against the user."""
	board = TicTacToeBoard(length)
	print_welcome()
	board.print_board()

	while True:
		if not board.start:
			winner = ' '
			# user's turn
			if board.player == 'X':
				try:
					move = input('Your turn\n'\
						         'Enter a position: ')
					move = move.lower()
					if move == 'exit':
						print('Goodbye')
						return
					if board.check_input(move):
						int_row = int(move[0]) - 1 
						int_col = ord(move[1]) - 97
						position = (int_row * board.size) + int_col
						board.make_move(position)
						board.moves += 1
						winner = board.check_for_winner()
						board.player = 'O'
				except KeyboardInterrupt:
					print('\nGoodbye')
					return
			else:
				# randomly choose spot, then linear probe
				board.make_comp_move()

			if winner != ' ':
				# user wins
				if winner == 'X':
					print('Winner: X (you)\n'\
						  'Congratulations, you won!')
					board.user_score += 1
				# computer wins
				if winner == 'O':
					print('Winner: O (computer)\n'\
						  'Sorry, you lost. Better luck next time.')
					board.comp_score += 1
				# tie game
				if winner == 'C':
					print("Winner: It's a tie!\n"\
						  "Better luck next time.")

				board.print_scores()

				try:
					if board.play_again():
						continue
				except KeyboardInterrupt:
					print('\nGoodbye')
					return
				else:
					print('Goodbye')
					return
		# first move (start = True)
		else:
			# randomly choose starting player
			starter = random.randint(0, 1)
			board.start = False
			if starter == 0:
				print("Computer starts!")
				board.player = 'O'
			else:
				print("You start!")
				board.player = 'X'


def print_welcome():
	"""Print welcome, directions and rules. Only prints at the start
	   of the program.
	"""
	print('\nWelcome to Tic Tac Toe.\n'\
		  'To win this game, acquire 3 spots in a row\n'\
		  '(vertically, horizontally, or diagonally).\n'\
		  'When prompted, make a move by typing in the Row (1-3) and \n'\
		  'Column (A-C) of your desired position in the format RC.\n'\
		  'Here are some possible moves:\n'\
		  '    > 3A\n'\
		  '    > 2C\n'\
		  '    > 1B\n\n'\
		  "*  Your moves are represented by 'X'.\n"\
		  "*  The computer's moves are represented by 'O'.\n"\
		  '*  The starting player is randomly chosen.\n'\
		  '*  You may exit the game any time by holding Control+C\n'\
		  '   or typing "exit".\n\n'\
		  'Below is the empty board. Have fun!\n')


if __name__ == '__main__':
	# hardcoded game dimension of size 3
	play_game(3)
