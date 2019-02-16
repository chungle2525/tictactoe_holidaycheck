import random

def play_game():
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
					move = input('Your turn!\n'\
						         'Enter a position: ')
					move = move.lower()
					if move == 'exit':
						print('Goodbye!')
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
					print('\nGoodbye!')
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
						  'Sorry, you lost. Better luck next time!')
					computer_score += 1
				# tie game
				if winner == 'C':
					print("Winner: It's a tie!\n"\
						  "Better luck next time!")
				
				print_scores(user_score, computer_score)

				try:
					if play_again(board):
						num_moves = 0
						start = True
						continue
				except KeyboardInterrupt:
					print('\nGoodbye!')
					return
				else:
					print('Goodbye!')
					return

		else:
			starter = random.randint(0, 1)
			start = False
			if starter == 0:
				print("Computer starts!")
				player = 'O'
			else:
				print("You start!")
				player = 'X'


def check_input(move, board):
	if len(move) == 2:
		if not move[0].isdigit():
			print('Invalid row!')
			return False
		int_row = int(move[0]) - 1
		# check for valid row
		if int_row != 0 and int_row != 1 and int_row != 2:
			print('Invalid row!')
			return False
		# check for valid column
		col = move[1]
		if col != 'a' and col != 'b' and col != 'c':
			print('Invalid column!')
			return False
		int_col = ord(col) - 97
		# check that position is available
		if board[(3 * int_row) + int_col] != '-':
			print('Position unavailable!')
			return False
		return True
	print('Invalid input!')
	return False


def make_move(player, move, board):
	# if random index is taken, search iteratively for open spot
	if player == 'O':
		print("Computer's turn!")
		board[move] = 'O'
	else:
		print('Your turn!')
		board[move] = 'X'
	print_board(board)


def check_for_winner(moves, player, board, winning_combos):
	# check for vertical win
	for combo in winning_combos:
		if (board[combo[0]] == player and board[combo[1]] == player and
			board[combo[2]] == player):
			return player

	# if no winner is found and board is full, it is a Cat's game (tie)
	if moves == 9:
		return 'C'

	return '-'


def print_scores(user_score, comp_score):
	print('\nSCORES:\n'\
		  'You: ' + str(user_score) + '\n'\
		  'Computer: ' + str(comp_score) + '\n')


def play_again(board):
	play_again = input('Play again? (Y/N): ')
	if play_again == 'Y' or play_again == 'y':
		# reset board positions
		board[:] = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
		print_board(board)
		return True
	return False


def print_board(board):
	print('      A         B         C')
	for row in range(0, 3):
		print('           |         |         ')
		# print if taken
		col_a = ' '
		col_b = ' '
		col_c = ' '
		if board[(3 * row)] != '-':
			col_a = board[(3 * row)]
		if board[(3 * row) + 1] != '-':
			col_b = board[(3 * row) + 1]
		if board[(3 * row) + 2] != '-':
			col_c = board[(3 * row) + 2]

		print('%c     %s    |    %s    |    %s    ' % (str(row + 1), col_a,
			                                           col_b, col_c))
		print('           |         |         ')
		if row < 2:
			print('  -------------------------------')
	print('\n')


def print_welcome():
	print('\nWelcome to Tic Tac Toe.\n'\
		  'When prompted, make a move by typing in the Row (1-3) and \n'\
		  'Column (A-C) of the desired position in the format RC.\n'\
		  'Here are some possible moves:\n'\
		  '    > 3A\n'\
		  '    > 2C\n'\
		  '    > 1B\n\n'\
		  "*  Your moves are represented by 'X'\n"\
		  "*  The computer's moves are represented by 'O'\n"\
		  '*  The starting player is randomly chosen.\n'\
		  '*  You may exit the game any time by holding Control+C\n'\
		  '   or typing "exit"\n\n'\
		  'Below is the empty board. Have fun!\n')


if __name__ == '__main__':
	play_game()
