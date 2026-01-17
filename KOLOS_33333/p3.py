def f(vname):
    # 1. Sprawdzamy długość (od 1 do 5)
    if len(vname) < 1:
        return False
    if len(vname) > 5:
        return False
        
    # 2. Sprawdzamy pierwszy znak (musi być literą lub _)
    pierwszy_znak = vname[0]
    # isalpha() sprawdza czy to litera (a-z, A-Z)
    if not pierwszy_znak.isalpha() and pierwszy_znak != '_':
        return False
        
    # 3. Sprawdzamy pozostałe znaki (litery, cyfry lub _)
    # vname[1:] to napis od drugiego znaku do końca
    for znak in vname[1:]:
        # isdigit() sprawdza czy to cyfra
        je_litera = znak.isalpha()
        je_cyfra = znak.isdigit()
        je_podkreslnik = (znak == '_')
        
        # Jeśli znak NIE jest ani literą, ani cyfrą, ani _, to błąd
        if not (je_litera or je_cyfra or je_podkreslnik):
            return False
            
    # Jeśli przeszliśmy wszystkie testy
    return True


"""
import re

def f(vname):
    # Sprawdzenie długości (od 1 do 5 znaków)
    if len(vname) < 1 or len(vname) > 5:
        return False
        
    # Regex:
    # ^ - początek
    # [a-zA-Z_] - pierwszy znak (litera duża/mała lub podkreślnik)
    # [a-zA-Z0-9_]* - reszta znaków (litery, cyfry, podkreślniki)
    # $ - koniec
    pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    
    if re.match(pattern, vname):
        return True
    return False
"""