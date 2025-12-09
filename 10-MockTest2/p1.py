def f(player1, player2):
    wynik = lambda reka: sum(10 if c in "AKQJT" else int(c) for c in reka)

    return wynik(player1) >= wynik(player2)

print(f("AJ972", "AQT72"))

print(f("9532", "K8"))