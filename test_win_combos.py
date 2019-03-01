from play_tictactoe import TicTacToeBoard

def test_wc():

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

	board_7 = TicTacToeBoard(7)
	win_combos7 = []
	for combo in board_7.combo_queue:
		win_combos7.append(list(combo.indices))
	assert(win_combos7 == [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13],
		                   [14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27],
		                   [28, 29, 30, 31, 32, 33, 34], [35, 36, 37, 38, 39, 40, 41],
		                   [42, 43, 44, 45, 46, 47, 48], # rows
		                   [0, 7, 14, 21, 28, 35, 42], [1, 8, 15, 22, 29, 36, 43],
		                   [2, 9, 16, 23, 30, 37, 44], [3, 10, 17, 24, 31, 38, 45],
		                   [4, 11, 18, 25, 32, 39, 46], [5, 12, 19, 26, 33, 40, 47],
		                   [6, 13, 20, 27, 34, 41, 48], # columns
		                   [0, 8, 16, 24, 32, 40, 48], [6, 12, 18, 24, 30, 36, 42]]) # diags

	board_9 = TicTacToeBoard(9)
	win_combos9 = []
	for combo in board_9.combo_queue:
		win_combos9.append(list(combo.indices))
	assert(win_combos9 == [[0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17],
		                   [18, 19, 20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 32, 33, 34, 35],
		                   [36, 37, 38, 39, 40, 41, 42, 43, 44], [45, 46, 47, 48, 49, 50, 51, 52, 53],
		                   [54, 55, 56, 57, 58, 59, 60, 61, 62], [63, 64, 65, 66, 67, 68, 69, 70, 71],
		                   [72, 73, 74, 75, 76, 77, 78, 79, 80], # rows
		                   [0, 9, 18, 27, 36, 45, 54, 63, 72], [1, 10, 19, 28, 37, 46, 55, 64, 73],
		                   [2, 11, 20, 29, 38, 47, 56, 65, 74], [3, 12, 21, 30, 39, 48, 57, 66, 75],
		                   [4, 13, 22, 31, 40, 49, 58, 67, 76], [5, 14, 23, 32, 41, 50, 59, 68, 77],
		                   [6, 15, 24, 33, 42, 51, 60, 69, 78], [7, 16, 25, 34, 43, 52, 61, 70, 79],
		                   [8, 17, 26, 35, 44, 53, 62, 71, 80], # columns
		                   [0, 10, 20, 30, 40, 50, 60, 70, 80], [8, 16, 24, 32, 40, 48, 56, 64, 72]]) # diags

if __name__ == "__main__":
	print("Testing win combos...")
	test_wc()
	print("Passed!")
