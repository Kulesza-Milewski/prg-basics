def f(array):
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
