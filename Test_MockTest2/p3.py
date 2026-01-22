def f(array2D):
    liczba_wierszy = len(array2D)
    for i in range(liczba_wierszy):
        suma_wiersza = sum(array2D[i])
        suma_kolumny = 0
        for wiersz in array2D:
            suma_kolumny += wiersz[i]
            
        if suma_wiersza != suma_kolumny:
            return False
            
    return True
