def f(fnc, res):
    # Lista na przefiltrowane wyniki
    przefiltrowane = []
    
    for wynik in res:
        # Wywołujemy funkcję fnc dla każdego wyniku
        # Jeśli fnc zwróci True, dodajemy wynik do listy
        if fnc(wynik) == True:
            przefiltrowane.append(wynik)
            
    # Jeśli po filtrowaniu lista jest pusta, zwróć 0 (zabezpieczenie)
    if len(przefiltrowane) == 0:
        return 0
        
    # Obliczamy różnicę
    najwiekszy = max(przefiltrowane)
    najmniejszy = min(przefiltrowane)
    
    return najwiekszy - najmniejszy