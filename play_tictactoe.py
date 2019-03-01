import random

class WinCombo:

	def __init__(self, id_in, combo):
		self.id = id_in
		self.user_count = 0
		self.comp_count = 0
		self.indices = combo

	def __gt__(self, other):
		if self.comp_count > other.comp_count:
			return True
		if self.comp_count == other.comp_count:
			if self.user_count > other.user_count:
				return True
			if self.user_count == other.user_count:
				return self.id < other.id
		return False

	def __str__(self):
		string = ("INDICES: " + str(self.indices) + (" USER: %d, COMP: %d" % (self.user_count, self.comp_count)))
		return string


class TicTacToeBoard:

	def __init__(self, length):
		assert length % 2 == 1
		self.size = length
		self.moves = 0
		self.player = 'O'
		self.user_score = 0
		self.comp_score = 0
		self.board = [' '] * (self.size * self.size)
		self.corners = [0, (self.size - 1), (self.size * (self.size - 1)),
			            ((self.size + 1) * (self.size - 1))]
		self.combo_queue = []
		combo_count = 0
		# winning rows
		for row in range(0, self.size):
			columns = []
			for col in range(0, self.size):
				columns.append((row * self.size) + col)
			tpl = tuple(columns)
			combo = WinCombo(combo_count, tpl)
			combo_count += 1
			self.combo_queue.append(combo)

		# winning columns
		for col in range(0, self.size):
			rows = []
			for row in range(0, self.size):
				rows.append(col + (row * self.size))
			tpl = tuple(rows)
			combo = WinCombo(combo_count, tpl)
			combo_count += 1
			self.combo_queue.append(combo)

		# winning diags
		if self.size > 1:
			diag1 = []
			i = 0
			while i < self.size:
				diag1.append((i) * (self.size + 1))
				i += 1
			tpl = tuple(diag1)
			combo = WinCombo(combo_count, tpl)
			combo_count += 1
			self.combo_queue.append(combo)

			diag2 = []
			j = 0
			while j < self.size:
				diag2.append((j + 1) * (self.size - 1))
				j += 1
			tpl = tuple(diag2)
			combo = WinCombo(combo_count, tpl)
			combo_count += 1
			self.combo_queue.append(combo)

	def choose_starter(self):
		"""Randomly choose starting player"""
		if random.randint(0, 1) == 0:
			print("Computer starts!")
			board.player = 'O'
		else:
			print("You start!")
			board.player = 'X'

	def get_potential(self, move):
		"""Return maximum potential winning combos for current move."""
		possible_comp_wins = 0
		possible_user_wins = 0
		for combo in self.combo_queue:
			if move in combo.indices:
				if combo.user_count + 1 == self.size - 1 and combo.comp_count == 0:
					possible_user_wins += 1
				if combo.comp_count + 1 == self.size - 1 and combo.user_count == 0:
					possible_comp_wins += 1
		return max(possible_user_wins, possible_comp_wins)

	def make_move(self, move):
		"""Make the player's move on the game board. X=user, O=computer."""
		if self.player == 'O':
			print("Computer's turn")
		else:
			print('Your turn')

		for combo in self.combo_queue:
			if move in combo.indices:
				if self.player == 'O':
					combo.comp_count += 1
				else:
					combo.user_count += 1
		self.board[move] = self.player
		self.moves += 1
		self.print_board()

	def make_user_move(self, move):
		int_row = int(move[0]) - 1 
		int_col = ord(move[1]) - 97
		position = (int_row * self.size) + int_col
		self.make_move(position)

	def first_comp_move(self):
		"""Choose center or first corner as computer's first move"""
		mul = (self.size - 1) / 2
		center = (self.size * mul) + mul
		center = int(center)
		if self.is_open(center):
			self.make_move(center)
		else:
			self.make_move(self.corners[0])

	def make_winning_move(self):
		"""Make a winning move, or take a winning move from the user"""
		for combo in self.combo_queue:
			if (combo.user_count == self.size - 1 or
				combo.comp_count == self.size - 1):
				for idx in combo.indices:
					if self.is_open(idx):
						self.make_move(idx)
						return True
		return False

	def handle_corners(self):
		""" Handle if user owns two opposite corners"""
		if ((self.board[self.corners[0]] == 'X' and self.board[self.corners[3]] == 'X') or
			(self.board[self.corners[1]] == 'X' and self.board[self.corners[2]] == 'X')):
			# ignore potential, try to win
			for combo in self.combo_queue:
				for idx in combo.indices:
					if self.is_open(idx):
						self.make_move(idx)
						return True
		return False

	def highest_potential_move(self):
		max_potential = 0
		max_idx = 0
		for idx in range(0, len(self.board)):
			if self.is_open(idx):
				ptn = self.get_potential(idx)
				if ptn > max_potential:
					max_potential = ptn
					max_idx = idx
		self.make_move(max_idx)

	def make_comp_move(self):
		"""Make a start, winning or highest potential move"""
		self.combo_queue.sort(reverse=True)
		if self.moves > 1:			
			winning_move = self.make_winning_move()
			if not winning_move:
				user_has_corners = self.handle_corners()
				if not user_has_corners:
					self.highest_potential_move()
					return
				else:
					pass
		else:
			self.first_comp_move()

	def check_input(self, move):
		"""Return whether or not the user input has valid length, row, column
		   and position.
		"""
		if len(move) == 2:
			if not move[0].isdigit():
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
		for combo in self.combo_queue:
			current = True
			for idx in combo.indices:
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
			self.board = [' '] * (self.size * self.size)
			for combo in self.combo_queue:
				combo.user_count = 0
				combo.comp_count = 0
			self.print_board()
			self.choose_starter()
			return True
		return False

	def is_open(self, move):
		if self.board[move] == ' ':
			return True
		return False

	def game_over(self, winner):
		if winner != ' ':
			# user wins
			if winner == 'X':
				print('Winner: X (you)\n'\
					  'Congratulations, you won!')
				self.user_score += 1
			# computer wins
			if winner == 'O':
				print('Winner: O (computer)\n'\
					  'Sorry, you lost. Better luck next time.')
				self.comp_score += 1
			# tie game
			if winner == 'C':
				print("Winner: It's a tie!\n"\
					  "Better luck next time.")

			self.print_scores()

			try:
				if self.play_again():
					return False
				return True
			except KeyboardInterrupt:
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


def play_game(board):
	"""Play a game of tic-tac-toe against the user."""
	while True:
		winner = ' '
		if board.player == 'X':
			try:
				move = input('Your turn\n'\
					         'Enter a position: ')
				move = move.lower()
				if move == 'exit':
					print('Goodbye')
					return
				if board.check_input(move):
					board.make_user_move(move)
					winner = board.check_for_winner()
					board.player = 'O'
			except KeyboardInterrupt:
				print('\nGoodbye')
				return
		else:
			board.make_comp_move()
			winner = board.check_for_winner()
			board.player = 'X'

		if board.game_over(winner):
			return

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
	board = TicTacToeBoard(3)
	print_welcome()
	board.print_board()
	board.choose_starter()
	play_game(board)
