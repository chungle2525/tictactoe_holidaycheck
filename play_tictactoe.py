def play_game():
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
	taken = []
	taken.append(['-', '-', '-'])
	taken.append(['-', '-', '-'])
	taken.append(['-', '-', '-'])
	print_board(taken)
	num_moves = 0
	while True:
		move = input('Enter a position: ')
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
			lower_col = move[1].lower()
			if lower_col != 'a' and lower_col != 'b' and lower_col != 'c':
				print('Invalid column!')
				continue
			int_col = ord(lower_col) - 97
			# check that position is available
			if taken[int_col][int_row] != '-':
				print('Position unavailable!')
				continue
			else:
				num_moves += 1
				# valid input
				taken[int_col][int_row] = 'X'
				make_move(taken)
				print_board(taken)
				# check for winner
				winner = check_for_winner(num_moves, int_col, int_row, 'X',
					                      taken)
				if winner != '-':
					if winner == 'X':
						print('Winner: X (you)\n'\
							  'Congratulations, you are the winner!')
					if winner == '0':
						print('Winner: O (computer)"\n'\
							  'Sorry, you lost. Better luck next time!')
					if winner == 'C':
						print("Winner: It's a tie!\n"\
							  "Better luck next time!")
					play_again = input('Play again? (Y/N): ')
					if play_again == 'Y' or play_again == 'y':
						# reset taken positions
						taken[0] = ['-', '-', '-']
						taken[1] = ['-', '-', '-']
						taken[2] = ['-', '-', '-']
						# reset the move count and restart game
						num_moves = 0
						print_board(taken)
						continue
					else:
						print('Goodbye!')
						return
		else:
			print('Invalid input!')
			continue

def make_move(taken):
	pass


def check_for_winner(num_moves, current_col, current_row, player, taken):
	# check for vertical win
	row_idx = 0
	while row_idx < 3:
		if taken[current_col][row_idx] != player:
			# no win
			break
		row_idx += 1
	if row_idx == 3:
		return player

	# check for horizontal win
	col_idx = 0
	while col_idx < 3:
		if taken[col_idx][current_row] != player:
			break
		col_idx += 1
	if col_idx == 3:
		return player

	# check for diagonal win if move is one of the 4 corners or the center
	if current_col == current_row or (current_col + current_row == 2):
		# can only be diagonal win if center == player
		if (taken[1][1] == player):
			if (taken[0][0] == player) and (taken[2][2] == player):
				return player
			if (taken[2][0] == player) and (taken[0][2] == player):
				return player

	# if no winner is found and board is full, it is a Cat's game (tie)
	if num_moves == 9:
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
		if taken[0][row] != '-':
			col_a = taken[0][row]
		if taken[1][row] != '-':
			col_b = taken[1][row]
		if taken[2][row] != '-':
			col_c = taken[2][row]

		print('%c     %s    |    %s    |    %s    ' % (str(row + 1), col_a,
			                                           col_b, col_c))
		print('           |         |         ')
		if row < 2:
			print('  -------------------------------')


if __name__ == '__main__':
	play_game()
