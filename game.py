"""
            Tic-Tac-Toe Game
===================================================================================================
This program implements a simple console-based Tic-Tac-Toe game for two players.
Players take turns to place their marks ('X' for Player 1 and 'O' for Player 2) on a 3x3 grid.
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
    - Date: 03//2025
    - Version: 1.1
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
        place[0],"|",place[1],"|",place[2],
        "\n-----------\n",
        place[3],"|",place[4],"|",place[5],
        "\n-----------\n",
        place[6],"|",place[7],"|",place[8],
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
        print("Player 1 WON!")
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
        print("Player 2 WON!")
        break
    elif not any(isinstance(i, int) for i in place):
        print("Nice game, but no one won")
        break
    if not any(isinstance(i, int) for i in place):
        print("Nice game, but no one won")
        break

