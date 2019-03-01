import sys
import io
from play_tictactoe import TicTacToeBoard
from play_tictactoe import play_game

def test_comp_starts_tie():
	trying_tie()

def test_comp_starts_comp_wins():
	# computer wins quickly
	opposite_corners()
	adjacent_corners()
	opposite_middles()
	trying_win()

def trying_tie():
	board = TicTacToeBoard(3)
	board.player = 'O'
	sys.stdin = io.StringIO("1a\n2c\n3a\n3b\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 0

	board = TicTacToeBoard(3)
	board.player = 'O'
	sys.stdin = io.StringIO("3c\n2c\n3a\n1b\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 0

def opposite_corners():
	"""Test if user takes opposite corners"""
	# topleft, bottom right
	board = TicTacToeBoard(3)
	board.player = 'O'
	sys.stdin = io.StringIO("1a\n3c\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1
	# top right, bottom left
	board = TicTacToeBoard(3)
	board.player = 'O'
	sys.stdin = io.StringIO("1c\n3a\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1

def adjacent_corners():
	"""Test if user takes adjacent corners"""
	# top two
	board = TicTacToeBoard(3)
	board.player = 'O'
	sys.stdin = io.StringIO("1a\n1c\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1
	# right two
	board = TicTacToeBoard(3)
	board.player = 'O'
	sys.stdin = io.StringIO("1c\n3c\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1
	# bottom two
	board = TicTacToeBoard(3)
	board.player = 'O'
	sys.stdin = io.StringIO("3a\n3c\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1
	# left two
	board = TicTacToeBoard(3)
	board.player = 'O'
	sys.stdin = io.StringIO("1a\n3a\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1

def opposite_middles():
	"""Test if user takes opposite middle positions"""
	# vertical two
	board = TicTacToeBoard(3)
	board.player = 'O'
	sys.stdin = io.StringIO("1b\n3b\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1
	# horizontal two
	board = TicTacToeBoard(3)
	board.player = 'O'
	sys.stdin = io.StringIO("2a\n2c\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1

def trying_win():
	"""Test if user tries to beat the computer"""
	board = TicTacToeBoard(3)
	board.player = 'O'
	sys.stdin = io.StringIO("2a\n3b\n1c\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1

	board = TicTacToeBoard(3)
	board.player = 'O'
	sys.stdin = io.StringIO("2c\n3b\n3c\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1

def test_play_game():
	test_comp_starts_tie()
	test_comp_starts_comp_wins()

if __name__ == "__main__":
	print("Testing tic tac to game...")
	test_play_game()
	print("Passed!")
