def f(card_number):
    poczatek = card_number[:2]
    koniec = card_number[-4:]
    gwiazdy = "*" * 10

    wynik = poczatek + gwiazdy + koniec

    return wynik

print(f("5290312400019022"))

#Błędy

"""
1. Kombinowałem 
2. Nie zauważyłem że dane do testów są w nawiasach 
3. Nie znałem sposobu odczytywania elementów listy 

"""