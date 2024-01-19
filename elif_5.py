print('1->Rock\n2->Paper\n3->Scissor')
p1=input('player 1 :\n')
p2=input('player 2 :\n')
if p1 == p2:
    print('match tie')
elif p1=='1' and p2=='3':
    print('player1 WON')
elif p1=='2' and p2=='1':
    print('player1 WON')
elif p1=='3' and p2=='2':
    print('player1 WON') 
else:
    print("player2 won")