def f(player1,player2):
    
    max_value = ['A', 'K','Q','J','T']
    score1 = 0
    score2 = 0

    for card1 in player1:
        if card1 in max_value:
            score1 += 10
        else:
            score1 += int(card1)
        

    for card2 in player2:
        if card2 in max_value:
            score2 += 10
        else:
            score2 += int(card2)

    if score1 == score2 or score1 > score2:
        return True
    else:
        return False
        
print(f("9532","K8"))





