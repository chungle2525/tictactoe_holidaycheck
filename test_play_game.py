import sys
import StringIO
from play_tictactoe import TicTacToeBoard

def test_play_game():
	# tie games where user starts
	sys.stdin = StringIO.StringIO("1a\n1c\n3b\n2a\n2c\n")
	play_tictactoe.play_game(3)
	

if __name__ == "__main__":
	print("Testing tic tac to game...")
	test_play_game()
	print("Passed!")
