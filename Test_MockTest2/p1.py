def f(player1, player2):
    high = ['A', 'K', 'Q', 'J', 'T']
    n1 = 0
    n2 = 0
    player1_value = 0
    player2_value = 0

    while n1 < len(player1):
        if player1[n1] in high:
            player1_value += 10
        else:
            player1_value += int(player1[n1])
        n1 += 1

    while n2 < len(player2):
        if player2[n2] in high:
            player2_value += 10
        else:
            player2_value += int(player2[n2])
        n2 += 1

    if player1_value >= player2_value:
        return True, player1_value, player2_value
    else:
        return False, player1_value, player2_value
    

print(f("9532","K8"))

#Błędy

"""
Miałem jedną wartość n, nic jej nie resetowało, 
musiałem zmienić ją na dwie wartości n1, n2

"""