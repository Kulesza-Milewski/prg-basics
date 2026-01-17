# Funkcja pomocnicza 1: wyciąga rejestrację (klucz)
def daj_rejestracje(slownik_auta):
    klucze = list(slownik_auta.keys())
    return klucze[0] # Zwraca np. "KR333"

# Funkcja pomocnicza 2: wyciąga przebieg (wartość)
def daj_przebieg(slownik_auta):
    wartosci = list(slownik_auta.values())
    return wartosci[0] # Zwraca np. 138

def f(cars, order):
    if order == 1:
        # Sortowanie alfabetycznie po rejestracji
        return sorted(cars, key=daj_rejestracje)
        
    elif order == 2:
        # Sortowanie po przebiegu, malejąco (reverse=True)
        return sorted(cars, key=daj_przebieg, reverse=True)
    
"""
def f(cars, order):
    # cars = [{"KR333":138}, {"WL555":497}...]
    
    if order == 1:
        # Sortowanie alfabetycznie po kluczu (rejestracji)
        # list(x.keys())[0] wyciąga klucz ze słownika
        return sorted(cars, key=lambda x: list(x.keys())[0])
        
    elif order == 2:
        # Sortowanie malejąco (descending) po wartości (przebieg)
        # list(x.values())[0] wyciąga wartość ze słownika
        return sorted(cars, key=lambda x: list(x.values())[0], reverse=True)
"""