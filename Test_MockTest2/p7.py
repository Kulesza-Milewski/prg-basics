def f(array):
    poprawne_loginy = 0
    
    for login in array:
        if len(login) < 4 or len(login) > 12:
            continue
            
        jest_poprawny = True
        for znak in login:
            if not (znak.islower() or znak.isdigit() or znak == "_"):
                jest_poprawny = False
                break
        
        if jest_poprawny:
            poprawne_loginy += 1
            
    return poprawne_loginy
