def f(oceny1_str, oceny2_str):
    # Obliczanie średniej dla pierwszego ucznia bezpośrednio w funkcji
    oceny1 = [int(x) for x in oceny1_str.split(',')]
    srednia1 = sum(oceny1) / len(oceny1)
    
    # Obliczanie średniej dla drugiego ucznia bezpośrednio w funkcji
    oceny2 = [int(x) for x in oceny2_str.split(',')]
    srednia2 = sum(oceny2) / len(oceny2)
    
    # Porównanie średnich
    if srednia1 > srednia2:
        return "Uczeń 1 ma wyższą średnią"
    elif srednia2 > srednia1:
        return "Uczeń 2 ma wyższą średnią"
    else:
        return "Średnie są równe"

if __name__ == "__main__":
    print(f("5,5,4", "3,4,3"))