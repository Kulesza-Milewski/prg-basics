def f(subjects):
    najwyzsza_srednia = 0
    najlepszy_przedmiot = ""
    
    for przedmiot, oceny in subjects.items():
        if len(oceny) > 0:
            srednia = sum(oceny) / len(oceny)
            if srednia > najwyzsza_srednia:
                najwyzsza_srednia = srednia
                najlepszy_przedmiot = przedmiot
            
    return najlepszy_przedmiot
