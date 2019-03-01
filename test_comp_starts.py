import sys
import io
from play_tictactoe import TicTacToeBoard
from play_tictactoe import play_game

def test_comp_starts_tie():
	pass

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

def test_comp_starts_comp_wins():
	opposite_corners()


def test_play_game():
	test_comp_starts_tie()
	test_comp_starts_comp_wins()


if __name__ == "__main__":
	print("Testing tic tac to game...")
	test_play_game()
	print("Passed!")
