import sys
import io
from play_tictactoe import TicTacToeBoard
from play_tictactoe import play_game

def test_play_game():
	# tie games where user starts
	sys.stdin = io.StringIO("1a\n1c\n3b\n2a\n2c\n")
	board = TicTacToeBoard(3)
	play_game(board)
	assert board.user_score == 0
	assert board.comp_score == 0

if __name__ == "__main__":
	print("Testing tic tac to game...")
	test_play_game()
	print("Passed!")
