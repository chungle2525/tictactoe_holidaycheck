import random

def play_game():
	print_welcome()
	# initialize array of size 9 of taken moves
	taken = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
	print_board(taken)
	num_moves = 0
	winning_combinations = [(0, 1, 2),
							(3, 4, 5),
							(6, 7, 8),
							(0, 3, 6),
							(1, 4, 7),
							(2, 5, 8),
							(0, 4, 8),
							(2, 4, 6)]

	while True:
		print('Your turn!')
		move = input('Enter a position: ')
		move = move.lower()
		if move == 'exit':
			print('Goodbye!')
			return
		# check for valid user input
		if len(move) == 2:
			int_row = int(move[0]) - 1
			# check for valid row
			if int_row != 0 and int_row != 1 and int_row != 2:
				print('Invalid row!')
				continue
			# check for column
			col = move[1]
			if col != 'a' and col != 'b' and col != 'c':
				print('Invalid column!')
				continue
			int_col = ord(col) - 97
			# check that position is available
			if taken[(3 * int_row) + int_col] != '-':
				print('Position unavailable!')
				continue
			else:
				# valid input
				num_moves += 1
				taken[(3 * int_row) + int_col] = 'X'
				print_board(taken)

				# check for winner
				winner = check_for_winner(num_moves, int_col, int_row, 'X',
					                      taken, winning_combinations)
				if winner != '-':
					# a user can only win after they take a turn
					if winner == 'X':
						print('Winner: X (you)\n'\
							  'Congratulations, you are the winner!')
					# since they always make the first move, a tie game can
					# only happen after the user takes their turn
					if winner == 'C':
						print("Winner: It's a tie!\n"\
							  "Better luck next time!")
					play_again = input('Play again? (Y/N): ')
					if play_again == 'Y' or play_again == 'y':
						# reset taken positions
						taken = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
						# reset the move count and restart game
						num_moves = 0
						print_board(taken)
						continue
					else:
						print('Goodbye!')
						return
				# make computer move if user's move does not produce win
				print("Computer's turn!")
				num_moves += 1
				make_computer_move(taken)
				winner = check_for_winner(num_moves, int_col, int_row, 'O',
					          taken, winning_combinations)
				# the computer can only win if it is its own turn
				if winner == 'O':
					print('Winner: O (computer)\n'\
						  'Sorry, you lost. Better luck next time!')
		else:
			print('Invalid input!')
			continue


def make_computer_move(taken):
	# if random index is taken, search iteratively for open spot
	random_idx = random.randint(0, 8)
	if taken[random_idx] != '-':
		for adder in range(1, 9):
			new_idx = (random_idx + adder) % 9
			if taken[new_idx] == '-':
				random_idx = new_idx
				break
	taken[random_idx] = 'O'
	print_board(taken)

def check_for_winner(moves, col, row, player, taken, winning_combos):
	# check for vertical win
	for combo in winning_combos:
		if (taken[combo[0]] == player and taken[combo[1]] == player and
			taken[combo[2]] == player):
			return player

	# if no winner is found and board is full, it is a Cat's game (tie)
	if moves == 9:
		return 'C'

	return '-'


def print_board(taken):
	print('      A         B         C')
	for row in range(0, 3):
		print('           |         |         ')
		# print if taken
		col_a = ' '
		col_b = ' '
		col_c = ' '
		if taken[(3 * row)] != '-':
			col_a = taken[(3 * row)]
		if taken[(3 * row) + 1] != '-':
			col_b = taken[(3 * row) + 1]
		if taken[(3 * row) + 2] != '-':
			col_c = taken[(3 * row) + 2]

		print('%c     %s    |    %s    |    %s    ' % (str(row + 1), col_a,
			                                           col_b, col_c))
		print('           |         |         ')
		if row < 2:
			print('  -------------------------------')


def print_welcome():
	print('\nWelcome to Tic Tac Toe.\n'\
		  'Make a move by typing in the Row (1-3) and Column (A-C) of the\n'\
		  'desired position in the terminal in the format RC.\n'\
		  'Here are some possible moves:\n'\
		  '    > 3A\n'\
		  '    > 2C\n'\
		  '    > 1B\n'\
		  'The game can be exited any time by holding Control+C\n'\
		  'or typing "exit"\n\n'\
		  'Below is the empty board. Have fun! \n\n')


if __name__ == '__main__':
	play_game()
