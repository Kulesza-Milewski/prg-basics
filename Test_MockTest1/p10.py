def f(sentence):
    n = 0
    suma = 0

    while n < len(sentence):
        znak = int(ord(sentence[n]))
        suma += znak
        n += 1

    if suma % 3 == 0:
        return True
    else:
        return False
    
print(f("student"))

#Dobrze