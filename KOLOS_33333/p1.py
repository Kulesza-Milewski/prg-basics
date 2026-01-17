"""def f(d):
    n = 0
    number = 0

    while n < len(d):
        if d[n] == "+":
            number += 1
        elif d[n] == "-":
            number -= 1
        n += 1
    return number

print(f("+-+++++-")) """ 


# Propozycja SI

def f(d):
    # Metoda count zlicza wystąpienia znaku w napisie
    plusy = d.count('+')
    minusy = d.count('-')
    return plusy - minusy