def win(a):
    if (l[0]==l[1]==l[2]==a) or (l[3]==l[4]==l[5]==a) or (l[6]==l[7]==l[8]==a) or (l[0]==l[3]==l[6]==a) or (l[1]==l[4]==l[7]==a) or (l[2]==l[5]==l[8]==a) or (l[0]==l[4]==l[8]==a) or (l[2]==l[4]==l[6]==a):
        return True
    return False
'''def draw():
    if (all(isinstance(i, str) for i in l)):
        return True
    if (l[0]!=l[1]!=l[2]) or (l[3]!=l[4]!=l[5]) or (l[6]!=l[7]!=l[8]) or (l[0]!=l[3]!=l[6]) or (l[1]!=l[4]!=l[7]) or (l[2]!=l[5]!=l[8]) or (l[0]!=l[4]!=l[8]) or (l[2]!=l[4]!=l[6]):
        return True
    return False'''
''''def final_check():
    if l[0]!=0 and l[1]!=1 and l[2]!=2 and l[3]!=3 and l[4]!=4 and l[5]!=5 and l[6]!=6 and l[7]!=7 and l[8]!=8:
        return True'''
def draw_board():
    print('', l[0], '|', l[1], '|', l[2], '\n-----------\n', l[3], '|', l[4], '|', l[5], '\n-----------\n', l[6], '|', l[7], '|', l[8])
#n=0
l=list(range(1, 10))
print("""Rules of the game:
      1. The game is played on a 3x3 grid.
      2. Player 1 uses 'X' and Player 2 uses 'O'.
      3. Players will have to enter the cell the number of choice to place the move.
      4. Players take turns placing their marks in empty squares.
      5. The first player to get three of their marks in a row (vertically, horizontally, or diagonally) wins.
      6. If all squares are filled and no player has three in a row, the game ends in a draw.""")
print(draw_board())
#moves=[]
while any(isinstance(i, int) for i in l):
    a = int(input('Player 1, enter your move:'))-1
    if a < 0 or a > 8 or isinstance(l[a], str):
        print('Invalid move.')
        continue
    l[a] = 'X'
    draw_board()
    if win('X'):
        print('Player 1 is the winner!')
        break
    elif not any(isinstance(i, int) for i in l):
        print('Nice game, but no one won')
        break
    '''if a in moves:
        print('Invalid move.')
    else:
        moves.append(a)
        for i in range(9):
            if a == l[i]:
                l.pop(a)
                l.insert(a,'X')
        print(draw_board())
        if win('X'):
            print('Player 1 is the winner!')
            break
        elif final_check():
            if draw():
                print('Nice game, but no one won')
                break
            else:
                print('Nice game, but no one won')
                break'''
    b = int(input('Player 2, enter your move:'))-1
    if b < 0 or b > 8 or isinstance(l[b], str):
        print('Invalid move.')
        continue
    l[b] = 'O'
    draw_board()
    if win('O'):
        print('Player 2 is the winner!')
        break
    elif not any(isinstance(i, int) for i in l):
        print('Nice game, but no one won')
        break
    '''if b in moves:
        print('Invalid move.')
    else:
        moves.append(b)
        for i in range(9):
            if b == l[i]:
                l.pop(b)
                l.insert(b,'O')
        print(draw_board())
        if win('O'):
            print('Player 2 is the winner!')
            break'''
    if not any(isinstance(i, int) for i in l):
        print('Nice game, but no one won')
        break