import json

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
