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
	taken = {}
	taken['A'] = ['-', '-', '-']
	taken['B'] = ['-', '-', '-']
	taken['C'] = ['-', '-', '-']
	print_board(taken)
	num_moves = 0
	while True:
		move = input('Enter a position: ')
		if move == 'exit':
			print('Goodbye!')
			return
		# check for valid user input
		if len(move) == 2:
			int_row = int(move[0])
			# check for valid row
			if int_row != 1 and int_row != 2 and int_row != 3:
				print('Invalid row!')
				continue
			# check for column
			upper_col = move[1].upper()
			if upper_col != 'A' and upper_col != 'B' and upper_col != 'C':
				print('Invalid column!')
				continue
			# check that position is available
			if taken[upper_col][int_row - 1] != '-':
				print('Position unavailable!')
				continue
			else:
				num_moves += 1
				# valid input
				taken[upper_col][int_row - 1] = 'X'
				make_move(num_moves, taken)
				print_board(taken)
				# check for winner
				winner = check_for_winner(num_moves, taken)
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
						taken['A'] = ['-', '-', '-']
						taken['B'] = ['-', '-', '-']
						taken['C'] = ['-', '-', '-']
						# reset the move count and restart game
						num_moves = 0
						continue
					else:
						print('Goodbye!')
						return
		else:
			print('Invalid input!')
			continue

def make_move(num_moves, taken):
	pass


def check_for_winner(num_moves, taken):
	return '-'


def print_board(taken):
	print('      A         B         C')
	for row in range(0, 3):
		print('           |         |         ')
		# print if taken
		col_a = ' '
		col_b = ' '
		col_c = ' '
		if taken['A'][row] != '-':
			col_a = taken['A'][row]
		if taken['B'][row] != '-':
			col_b = taken['B'][row]
		if taken['C'][row] != '-':
			col_c = taken['C'][row]

		print('%c     %s    |    %s    |    %s    ' % (str(row + 1), col_a,
			                                           col_b, col_c))
		print('           |         |         ')
		if row < 2:
			print('  -------------------------------')


if __name__ == '__main__':
	play_game()
