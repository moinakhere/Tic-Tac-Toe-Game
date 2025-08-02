def win(m):
    if (place[0]==place[1]==place[2]==m) or (place[3]==place[4]==place[5]==m) or (place[6]==place[7]==place[8]==m) or (place[0]==place[3]==place[6]==m) or (place[1]==place[4]==place[7]==m) or (place[2]==place[5]==place[8]==m) or (place[0]==place[4]==place[8]==m) or (place[2]==place[4]==place[6]==m):
        return True
    return False
def draw_board():
    print('', place[0], '|', place[1], '|', place[2], '\n-----------\n', place[3], '|', place[4], '|', place[5], '\n-----------\n', place[6], '|', place[7], '|', place[8])
#n=0
place=list(range(1, 10))
print("""Rules of the game:
      1. The game is played on a 3x3 grid.
      2. Player 1 uses 'X' and Player 2 uses 'O'.
      3. Players will have to enter the cell the number of choice to place the move.
      4. Players take turns placing their marks in empty squares.
      5. The first player to get three of their marks in a row (vertically, horizontally, or diagonally) wins.
      6. If all squares are filled and no player has three in a row, the game ends in a draw.""")
print(draw_board())
#moves=[]
while any(isinstance(i, int) for i in place):
    a = int(input('Player 1, enter your move:'))-1
    if a < 0 or a > 8 or isinstance(place[a], str):
        print('Invalid move.')
        continue
    place[a] = 'X'
    draw_board()
    if win('X'):
        print('Player 1 is the winner!')
        break
    elif not any(isinstance(i, int) for i in place):
        print('Nice game, but no one won')
        break
    b = int(input('Player 2, enter your move:'))-1
    if b < 0 or b > 8 or isinstance(place[b], str):
        print('Invalid move.')
        continue
    place[b] = 'O'
    draw_board()
    if win('O'):
        print('Player 2 is the winner!')
        break
    elif not any(isinstance(i, int) for i in place):
        print('Nice game, but no one won')
        break
    if not any(isinstance(i, int) for i in place):
        print('Nice game, but no one won')
        break