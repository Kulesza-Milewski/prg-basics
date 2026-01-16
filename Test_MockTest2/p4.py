def f(subjects):
    naj_srednia = 0
    przedmiot_koniec = ""
    
    for przedmiot, oceny in subjects.items():
        srednia = sum(oceny) / len(oceny)

        if srednia > naj_srednia:
            naj_srednia = srednia
            przedmiot_koniec = przedmiot
    return przedmiot_koniec
    
print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))

#Błędy

"""
Brak wiedzy o .items() i możliwości przechowywania wiedzy w pętli for

"""