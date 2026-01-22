def f(player1, player2):
    def policz_punkty(reka):
        suma = 0
        for karta in reka:
            if karta in "TJQKA":
                suma += 10
            else:
                suma += int(karta)
        return suma

    return policz_punkty(player1) >= policz_punkty(player2)
