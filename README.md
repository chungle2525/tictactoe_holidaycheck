# tictactoe_holidaycheck
tic-tac-toe challenge for Holidaycheck recruiting process

This python program plays tic-tac-toe against the user. The program prints the
3x3 tic-tac-toe board to the terminal after each move. The user always makes
the first move.
The program can be started with:
> python3 play_tictactoe.py

The program will randomly choose who makes the first move.
When prompted, the user can make a move by typing in the row (1-3) and column
(A-C) of the desired position in the terminal. Here are some possible moves:
> 3A
> 2C
> 1b
> 3c

If a user enters an invalid position (e.g. 5X, 4b, B2), they will be notified
and asked to enter a valid move.

The names for each board position are shown below:
--------------------------------
|		  |          |         |
|   1A    |    1B    |    1C   |
|		  |          |         |
--------------------------------
|		  |          |         |
|   2A    |    2B    |    2C   |
|		  |          |         |
--------------------------------
|		  |          |         |
|   3A    |    3B    |    3C   |
|		  |          |         |
--------------------------------

Available positions will appear empty. Positions taken by the user will contain
an 'X' and positions taken by the computer will contain an 'O'. Here is a
possible board state in during the game:
-------------------------------
|		  |         |         |
|    O    |    X    |         |
|		  |         |         |
--------------------------------
|		  |         |         |
|         |    X    |         |
|		  |         |         |
--------------------------------
|		  |         |         |
|         |    O    |         |
|		  |         |         |
-------------------------------

Once a player wins, the user has the option to exit the program or play another
tic tac toe game.
