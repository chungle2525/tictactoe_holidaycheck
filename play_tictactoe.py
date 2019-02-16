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
	while True:
		if not start:
			move = input('Your turn!\n'\
				         'Enter a position: ')
			move = move.lower()
			if move == 'exit':
				print('Goodbye!')
				return
			if check_input(move, board):
				num_moves += 1
				int_row = int(move[0]) - 1
				int_col = ord(move[1]) - 97
				board[(3 * int_row) + int_col] = 'X'
				print_board(board)

				# check for winner
				winner = check_for_winner(num_moves, int_col, int_row, 'X',
					                      board, winning_combinations)
				if winner != '-':
					# a user can only win after they take a turn
					if winner == 'X':
						print('Winner: X (you)\n'\
							  'Congratulations, you won!')
						user_score += 1
						print_scores(user_score, computer_score)
					# since they always make the first move, a tie game can
					# only happen after the user takes their turn
					if winner == 'C':
						print("Winner: It's a tie!\n"\
							  "Better luck next time!")
						print_scores(user_score, computer_score)

					if play_again(board):
						num_moves = 0
						start = True
						continue
					else:
						print('Goodbye!')
						return

				# make computer move if user's move does not produce win
				num_moves += 1
				print("Computer's turn!")
				computer_move(board)
				winner = check_for_winner(num_moves, int_col, int_row, 'O',
					          board, winning_combinations)

				if winner != '-':
					# the computer can only win if it is its own turn
					if winner == 'O':
						print('Winner: O (computer)\n'\
							  'Sorry, you lost. Better luck next time!')
						computer_score += 1
						print_scores(user_score, computer_score)
					if winner == 'C':
						print("Winner: It's a tie!\n"\
							  "Better luck next time!")
						print_scores(user_score, computer_score)
					
					if play_again(board):
						num_moves = 0
						start = True
						continue
					print('Goodbye!')
					return

			else:
				continue
		else:
			starter = determine_start()
			start = False
			if starter == 0:
				num_moves += 1
				print("Computer starts!")
				computer_move(board)
			else:
				continue


def determine_start():
	return random.randint(0, 1)


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


def computer_move(board):
	# if random index is taken, search iteratively for open spot
	random_idx = random.randint(0, 8)
	if board[random_idx] != '-':
		for adder in range(1, 9):
			new_idx = (random_idx + adder) % 9
			if board[new_idx] == '-':
				random_idx = new_idx
				break
	board[random_idx] = 'O'
	print_board(board)


def check_for_winner(moves, col, row, player, board, winning_combos):
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
