from play_tictactoe import TicTacToeBoard

def test_wc():
	board_0 = TicTacToeBoard(0)
	win_combos0 = []
	for combo in board_0.combo_queue:
		win_combos0.append(combo.indices)
	assert(win_combos0 == [])

	board_1 = TicTacToeBoard(1)
	win_combos1 = []
	for combo in board_1.combo_queue:
		win_combos1.append(list(combo.indices))
	assert(win_combos1 == [[0], [0]])

	board_3 = TicTacToeBoard(3)
	win_combos3 = []
	for combo in board_3.combo_queue:
		win_combos3.append(list(combo.indices))
	assert(win_combos3 == [[0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
		                   [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
		                   [0, 4, 8], [2, 4, 6]]) # diagonals

	board_5 = TicTacToeBoard(5)
	win_combos5 = []
	for combo in board_5.combo_queue:
		win_combos5.append(list(combo.indices))
	assert(win_combos5 == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], # rows
						   [15, 16, 17, 18, 19], [20, 21, 22, 23, 24], # rows
		                   [0, 5, 10, 15, 20], [1, 6, 11, 16, 21], [2, 7, 12, 17, 22], # columns
		                   [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], # columns
		                   [0, 6, 12, 18, 24], [4, 8, 12, 16, 20]]) # diagonals

if __name__ == "__main__":
	print("Testing win combos...")
	test_wc()
	print("Passed!")
