import sys
import io
from play_tictactoe import TicTacToeBoard
from play_tictactoe import play_game

def test_user_starts_comp_wins():
	corners_lose()
	medium_lose()
	complex_lose()

def test_user_starts_tie():
	test_corners_tie()
	test_middle_tie()
	complex_tie()

def test_corners_tie():
	# start top left, then bottom right
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("1a\n3c\n2c\n3a\n1b\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 0

	# start top left, then top right
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("1a\n1c\n3b\n2a\n2c\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 0

	# start bottomw left, then bottom right
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("3a\n3c\n1b\n2a\n2c\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 0

def test_middle_tie():
	# start middle, then left
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("2b\n2a\n1c\n1b\n3c\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 0

	# start middle, then bottom right
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("2b\n3c\n1b\n2a\n3a\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 0

def complex_tie():
	# start top middle, then top right
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("1b\n1c\n3c\n2a\n3b\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 0

	# start top left, then bottom middle
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("1a\n3b\n1c\n2c\n2a\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 0

def corners_lose():
	# top right three corners
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("1a\n1c\n3c\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1

	# bottom right three corners
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("1c\n3c\n3a\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1

	# bottom left three corners
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("3c\n3a\n1a\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1

	# top left three corners
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("3a\n1a\n1c\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1


def medium_lose():
	# top left triangle
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("1a\n1b\n2a\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1

	# top right, bottom left
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("1c\n2c\n3a\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1

	# start middle, bottom middle triangle
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("2b\n3b\n3a\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1

	# start middle, top right, bottom right
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("2b\n1c\n3c\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1

def complex_lose():
	# start middle, then 3 consecutive
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("2b\n2c\n3a\n3b\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1

	# start middle, then almost win
	board = TicTacToeBoard(3)
	board.player = 'X'
	sys.stdin = io.StringIO("2b\n1b\n1c\n2c\nn\n")
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 1

def test_play_game():
	test_user_starts_tie()
	test_user_starts_comp_wins()


if __name__ == "__main__":
	print("Testing tic tac to game...")
	test_play_game()
	print("Passed!")
