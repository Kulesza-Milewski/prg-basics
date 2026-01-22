import os

# Słownik zawierający nazwy plików i ich treść (kody rozwiązań bez komentarzy)
pliki = {
    "p1.py": """def f(player1, player2):
    def policz_punkty(reka):
        suma = 0
        for karta in reka:
            if karta in "TJQKA":
                suma += 10
            else:
                suma += int(karta)
        return suma

    return policz_punkty(player1) >= policz_punkty(player2)
""",

    "p2.py": """def f(arr):
    for liczba in arr:
        if arr.count(liczba) == 1:
            return liczba
""",

    "p3.py": """def f(array2D):
    liczba_wierszy = len(array2D)
    for i in range(liczba_wierszy):
        suma_wiersza = sum(array2D[i])
        suma_kolumny = 0
        for wiersz in array2D:
            suma_kolumny += wiersz[i]
            
        if suma_wiersza != suma_kolumny:
            return False
            
    return True
""",

    "p4.py": """def f(subjects):
    najwyzsza_srednia = 0
    najlepszy_przedmiot = ""
    
    for przedmiot, oceny in subjects.items():
        if len(oceny) > 0:
            srednia = sum(oceny) / len(oceny)
            if srednia > najwyzsza_srednia:
                najwyzsza_srednia = srednia
                najlepszy_przedmiot = przedmiot
            
    return najlepszy_przedmiot
""",

    "p5.py": """def f(first_letter, last_letter):
    licznik = 0
    try:
        with open("data.txt", "r", encoding="utf-8") as plik:
            tekst = plik.read()
            slowa = tekst.split()
            
            for slowo in slowa:
                czyste_slowo = slowo.strip(".,!?:")
                if czyste_slowo.startswith(first_letter) and czyste_slowo.endswith(last_letter):
                    licznik += 1
        return licznik
    except FileNotFoundError:
        return 0
""",

    "p6.py": """import json

def f(years, course, average_grade):
    licznik = 0
    try:
        with open("data.json", "r") as plik:
            lista_studentow = json.load(plik)
            
        for student in lista_studentow:
            if student["age"] >= years:
                kursy = student["studies"]
                if course in kursy:
                    oceny = kursy[course]
                    srednia = sum(oceny) / len(oceny)
                    if srednia >= average_grade:
                        licznik += 1
        return licznik
    except FileNotFoundError:
        return 0
""",

    "p7.py": """def f(array):
    poprawne_loginy = 0
    
    for login in array:
        if len(login) < 4 or len(login) > 12:
            continue
            
        jest_poprawny = True
        for znak in login:
            if not (znak.islower() or znak.isdigit() or znak == "_"):
                jest_poprawny = False
                break
        
        if jest_poprawny:
            poprawne_loginy += 1
            
    return poprawne_loginy
""",

    "p8.py": """def f(expression):
    stos = []
    elementy = expression.split()
    
    for element in elementy:
        if element.isdigit():
            stos.append(int(element))
        else:
            liczba2 = stos.pop()
            liczba1 = stos.pop()
            
            if element == "+":
                wynik = liczba1 + liczba2
            elif element == "-":
                wynik = liczba1 - liczba2
            
            stos.append(wynik)
            
    return stos[0]
""",

    "p9.py": """import csv

def f(value):
    licznik = 0
    try:
        with open("data.csv", "r") as plik:
            czytnik = csv.reader(plik)
            next(czytnik)
            
            for wiersz in czytnik:
                if wiersz:
                    napis_pensja = wiersz[-1]
                    pensja = float(napis_pensja)
                    if pensja >= value:
                        licznik += 1
        return licznik
    except FileNotFoundError:
        return 0
""",

    "p10.py": """def f(array):
    min_wartosc = float('inf')
    min_wiersz = -1
    min_kolumna = -1
    
    ilosc_wierszy = len(array)
    ilosc_kolumn = len(array[0])
    
    for w in range(ilosc_wierszy):
        for k in range(ilosc_kolumn):
            if array[w][k] < min_wartosc:
                min_wartosc = array[w][k]
                min_wiersz = w
                min_kolumna = k
                
    return min_wiersz == min_kolumna
"""
}

# Główna pętla tworząca pliki
def generuj_pliki():
    print("Rozpoczynam tworzenie plików...")
    for nazwa_pliku, tresc in pliki.items():
        try:
            with open(nazwa_pliku, "w", encoding="utf-8") as f:
                f.write(tresc)
            print(f"[OK] Utworzono plik: {nazwa_pliku}")
        except Exception as e:
            print(f"[BLAD] Nie udalo sie utworzyc {nazwa_pliku}: {e}")
    print("\nGotowe! Wszystkie pliki zostały wygenerowane.")

if __name__ == "__main__":
    generuj_pliki()