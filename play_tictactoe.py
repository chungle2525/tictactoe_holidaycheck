import random

def play_game():
	"""Play a game of tic-tac-toe against the user."""
	print_welcome()
	# initialize the board array of size 9. '-' indicates an empty spot
	board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
	computer_score = 0
	user_score = 0
	print_board(board)
	num_moves = 0
	winning_combinations = [(0, 1, 2),
							(3, 4, 5),
							(6, 7, 8),
							(0, 3, 6),
							(1, 4, 7),
							(2, 5, 8),
							(0, 4, 8),
							(2, 4, 6)]

	start = True
	player = 'O'
	while True:
		if not start:
			winner = '-'
			# user's turn
			if player == 'X':
				try:
					move = input('Your turn\n'\
						         'Enter a position: ')
					move = move.lower()
					if move == 'exit':
						print('Goodbye')
						return
					if check_input(move, board):
						int_row = int(move[0]) - 1
						int_col = ord(move[1]) - 97
						position = (int_row * 3) + int_col
						make_move(player, position, board)
						num_moves += 1
						winner = check_for_winner(num_moves, player, board,
					                      winning_combinations)
						player = 'O'
				except KeyboardInterrupt:
					print('\nGoodbye')
					return
			else:
				# if random index is taken, search iteratively for open spot
				random_idx = random.randint(0, 8)
				if board[random_idx] != '-':
					for adder in range(1, 9):
						new_idx = (random_idx + adder) % 9
						if board[new_idx] == '-':
							random_idx = new_idx
							break
				make_move(player, random_idx, board)
				num_moves += 1
				# check for winner
				winner = check_for_winner(num_moves, player, board,
				                      winning_combinations)
				player = 'X'

			if winner != '-':
				# user wins
				if winner == 'X':
					print('Winner: X (you)\n'\
						  'Congratulations, you won!')
					user_score += 1
				# computer wins
				if winner == 'O':
					print('Winner: O (computer)\n'\
						  'Sorry, you lost. Better luck next time.')
					computer_score += 1
				# tie game
				if winner == 'C':
					print("Winner: It's a tie!\n"\
						  "Better luck next time.")
				
				print_scores(user_score, computer_score)

				try:
					if play_again(board):
						num_moves = 0
						start = True
						continue
				except KeyboardInterrupt:
					print('\nGoodbye')
					return
				else:
					print('Goodbye')
					return
		# first move
		else:
			# randomly choose starting player
			starter = random.randint(0, 1)
			start = False
			if starter == 0:
				print("Computer starts!")
				player = 'O'
			else:
				print("You start!")
				player = 'X'


def check_input(move, board):
	"""Return whether or not the user input has valid length, row, column and
	   position.
	"""
	if len(move) == 2:
		if not move[0].isdigit():
			print('Oops, you entered an invalid row.')
			return False
		int_row = int(move[0]) - 1
		# check for valid row
		if int_row != 0 and int_row != 1 and int_row != 2:
			print('Oops, you entered an invalid row.')
			return False
		# check for valid column
		col = move[1]
		if col != 'a' and col != 'b' and col != 'c':
			print('Oops, you entered an invalid column.')
			return False
		int_col = ord(col) - 97
		# check that position is available
		if board[(3 * int_row) + int_col] != '-':
			print('Oops, that position is taken.')
			return False
		return True
	print('Invalid input.')
	return False


def make_move(player, move, board):
	"""Make the player's move on the game board. X=user, O=computer."""
	if player == 'O':
		print("Computer's turn")
		board[move] = 'O'
	else:
		print('Your turn')
		board[move] = 'X'

	print_board(board)


def check_for_winner(moves, player, board, winning_combos):
	"""Check if player has acquired a winning combination.
	   If so, return player. Otherwise, return '-'.
    """
	for combo in winning_combos:
		if (board[combo[0]] == player and board[combo[1]] == player and
			board[combo[2]] == player):
			return player

	# if no winner is found and board is full, it is a Cat's game (tie)
	if moves == 9:
		return 'C'

	return '-'


def print_scores(user_score, comp_score):
	"""Print the total score of the user and the computer.
	   Scores reset if the user exits the program.
	"""
	print('\n*SCORES:\n'\
		  '*You: ' + str(user_score) + '\n'\
		  '*Computer: ' + str(comp_score) + '\n')


def play_again(board):
	"""Return whether or not the user wants to play another game.
	   If True, reset the board to contain all empty positions.
	"""
	play_again = input('Play again? (Y/N): ')
	if play_again == 'Y' or play_again == 'y':
		# reset board positions
		board[:] = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
		print_board(board)
		return True
	return False


def print_board(board):
	"""Print the current state of the game board.
	   Spots taken by the user are represented by 'X'.
	   Spots taken by the computer are represented by 'O'.
	"""
	board_str = '      A         B         C\n'
	for row in range(0, 3):
		board_str += '           |         |         \n'
		# print player if spot is taken
		col_a = ' '
		col_b = ' '
		col_c = ' '
		if board[(3 * row)] != '-':
			col_a = board[(3 * row)]
		if board[(3 * row) + 1] != '-':
			col_b = board[(3 * row) + 1]
		if board[(3 * row) + 2] != '-':
			col_c = board[(3 * row) + 2]

		board_str += ('%c     %s    |    %s    |    %s    \n'
			          % (str(row + 1), col_a, col_b, col_c))
		board_str += '           |         |         \n'
		if row < 2:
			board_str += '  -------------------------------\n'
	print(board_str + '\n')


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
	play_game()
