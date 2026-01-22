def f(expression):
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
