def f(numer, even):
    numer2 = str(numer)
    liczba = 0
    suma = 0
    if even == True:
        while liczba < len(numer2):
            if int(numer2[liczba]) % 2 == 0:
                suma += int(numer2[liczba])
                liczba += 1
            else:
                liczba += 1
    
    elif even == False:
        while liczba < len(numer2):
            if int(numer2[liczba]) % 2 == 1:
                suma += int(numer2[liczba])
                liczba += 1
            else:
                liczba += 1
    
    
    return suma

print(f(3124, False))

#Błędy:

