import csv

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
