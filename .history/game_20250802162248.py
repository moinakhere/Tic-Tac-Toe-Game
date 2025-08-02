"""
            Tic-Tac-Toe Game
===================================================================================================
This program implements a simple console-based Tic-Tac-Toe game for two players.\n
Players take turns to place their marks ('X' for Player 1 and 'O' for Player 2) on a 3x3 grid.\n
The game checks for winning conditions after each move and declares the winner or a draw accordingly.

Features:
    - Displays game rules and instructions.
    - Shows the current state of the board after each move.
    - Validates player moves to prevent overwriting and out-of-range selections.
    - Detects win conditions (horizontal, vertical, diagonal).
    - Declares the winner or a draw when the game ends.

Global Variables:
    - place (list): Represents the current state of the Tic-Tac-Toe board.

Functions:
    - win(m): Checks if the player with marker `m` has won the game.
    - draw_board(): Displays the current state of the board.

Credits:
    - Author: moinakhere
    - Date: 02/08/2025
    - Version: 1.0
    - License: MIT License

MIT License

Copyright (c) 2025 moinakhere

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


def win(m):
    """
    Check if the player with marker `m` has won the Tic-Tac-Toe game.

    Args:
        m (str): The marker to check for a win (e.g., 'X' or 'O').

    Returns:
        bool: True if the player with marker `m` has a winning combination, False otherwise.

    Note:
        This function relies on a global variable `place`, which should be a list of 9 elements
        representing the current state of the Tic-Tac-Toe board.
    """
    if (
        (place[0] == place[1] == place[2] == m)
        or (place[3] == place[4] == place[5] == m)
        or (place[6] == place[7] == place[8] == m)
        or (place[0] == place[3] == place[6] == m)
        or (place[1] == place[4] == place[7] == m)
        or (place[2] == place[5] == place[8] == m)
        or (place[0] == place[4] == place[8] == m)
        or (place[2] == place[4] == place[6] == m)
    ):
        return True
    return False


def draw_board():
    """
    Displays the current state of the Tic-Tac-Toe board in the console.
    The board is represented by the global list `place`, where each element corresponds
    to a cell in the 3x3 grid. The function prints the board in a formatted manner,
    showing the values of each cell separated by vertical and horizontal lines.
    Assumes that `place` is a list of length 9 containing the current board values.
    """

    print(
        "",
        place[0],
        "|",
        place[1],
        "|",
        place[2],
        "\n-----------\n",
        place[3],
        "|",
        place[4],
        "|",
        place[5],
        "\n-----------\n",
        place[6],
        "|",
        place[7],
        "|",
        place[8],
    )


place = list(range(1, 10))
print(
    """Rules of the game:
      1. The game is played on a 3x3 grid.
      2. Player 1 uses 'X' and Player 2 uses 'O'.
      3. Players will have to enter the cell the number of choice to place the move.
      4. Players take turns placing their marks in empty squares.
      5. The first player to get three of their marks in a row (vertically, horizontally, or diagonally) wins.
      6. If all squares are filled and no player has three in a row, the game ends in a draw."""
)
print(draw_board())
while any(isinstance(i, int) for i in place):
    a = int(input("Player 1, enter your move:")) - 1
    if a < 0 or a > 8 or isinstance(place[a], str):
        print("Invalid move.")
        continue
    place[a] = "X"
    draw_board()
    if win("X"):
        print("Player 1 is the winner!")
        break
    elif not any(isinstance(i, int) for i in place):
        print("Nice game, but no one won")
        break
    b = int(input("Player 2, enter your move:")) - 1
    if b < 0 or b > 8 or isinstance(place[b], str):
        print("Invalid move.")
        continue
    place[b] = "O"
    draw_board()
    if win("O"):
        print("Player 2 is the winner!")
        break
    elif not any(isinstance(i, int) for i in place):
        print("Nice game, but no one won")
        break
    if not any(isinstance(i, int) for i in place):
        print("Nice game, but no one won")
        break
