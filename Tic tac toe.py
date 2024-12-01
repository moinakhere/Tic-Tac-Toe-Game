n=0
l=[]
print('Player 1: X\nPlayer 2: O')
for i in range(9):
    l.append(i)
print('', l[0], '|', l[1], '|', l[2], '\n-----------\n', l[3], '|', l[4], '|', l[5], '\n-----------\n', l[6], '|', l[7], '|', l[8])
moves=[]
while n!=1:
    a = int(input('Player 1, enter your move:'))
    if a in moves:
        print('Invalid move.')
    else:
        moves.append(a)
        for i in range(9):
            if a == l[i]:
                l.pop(a)
                l.insert(a,'X')
        print('', l[0], '|', l[1], '|', l[2], '\n-----------\n', l[3], '|', l[4], '|', l[5], '\n-----------\n', l[6], '|', l[7], '|', l[8])
        if (l[0]==l[1]==l[2]=='X') or (l[3]==l[4]==l[5]=='X') or (l[6]==l[7]==l[8]=='X') or (l[0]==l[3]==l[6]=='X') or (l[1]==l[4]==l[7]=='X') or (l[2]==l[5]==l[8]=='X') or (l[0]==l[4]==l[8]=='X') or (l[2]==l[4]==l[6]=='X'):
            print('Player 1 is the winner!')
            break
        elif l[0]!=0 and l[1]!=1 and l[2]!=2 and l[3]!=3 and l[4]!=4 and l[5]!=5 and l[6]!=6 and l[7]!=7 and l[8]!=8:
            if (l[0]!=l[1]!=l[2]) or (l[3]!=l[4]!=l[5]) or (l[6]!=l[7]!=l[8]) or (l[0]!=l[3]!=l[6]) or (l[1]!=l[4]!=l[7]) or (l[2]!=l[5]!=l[8]) or (l[0]!=l[4]!=l[8]) or (l[2]!=l[4]!=l[6]):
                print('Nice game, but no one won')
                break
            else:
                print('Nice game, but no one won')
                break
    b = int(input('Player 2, enter your move:'))
    if b in moves:
        print('Invalid move.')
    else:
        moves.append(b)
        for i in range(9):
            if b == l[i]:
                l.pop(b)
                l.insert(b,'O')
        print('', l[0], '|', l[1], '|', l[2], '\n-----------\n', l[3], '|', l[4], '|', l[5], '\n-----------\n', l[6], '|', l[7], '|', l[8])
        if (l[0]==l[1]==l[2]=='O') or (l[3]==l[4]==l[5]=='O') or (l[6]==l[7]==l[8]=='O') or (l[0]==l[3]==l[6]=='O') or (l[1]==l[4]==l[7]=='O') or (l[2]==l[5]==l[8]=='O') or (l[0]==l[4]==l[8]=='O') or (l[2]==l[4]==l[6]=='O'):
            print('Player 2 is the winner!')
            break
