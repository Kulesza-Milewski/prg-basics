def f(first_letter, last_letter):
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
