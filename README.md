# tictactoe_holidaycheck
tic-tac-toe challenge for Holidaycheck recruiting process

This python program plays tic-tac-toe against the user. The program prints the
3x3 tic-tac-toe board to the terminal after each move.
The program can be started with:
> python3 play_tictactoe.py

The user can make a move by typing in the row (1-3) and column (A-C) of the
desired position in the terminal. Here are some possible moves:
> 3A
> 2C
> 1b
> 3c

If a user enters an invalid position (e.g. 5X, 4b, B2), the following message
will appear:
> Please enter a valid board position in the format RC, where R is the row
(1-3) and C is the column (A-C)

The positions for each board position are shown below:
--------------------------------
|		  |          |         |
|   3A    |    3B    |    3C   |
|		  |          |         |
--------------------------------
|		  |          |         |
|   2A    |    2B    |    2C   |
|		  |          |         |
--------------------------------
|		  |          |         |
|   1A    |    1B    |    1C   |
|		  |          |         |
--------------------------------

Available positions will appear empty. Positions taken by the user will contain
an 'X' and positions taken by the computer will contain an 'O'. Here is a
possible board state in during the game:
--------------------------------
|		  |          |         |
|    O    |     X    |         |
|		  |          |         |
--------------------------------
|		  |          |         |
|         |     X    |         |
|		  |          |         |
--------------------------------
|		  |          |         |
|         |     O    |         |
|		  |          |         |
--------------------------------


