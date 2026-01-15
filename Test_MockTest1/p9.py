def f(sentence):
    samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
    n = 0
    wynik = 0

    while n < len(sentence):
        if sentence[n] in samogloski:
            wynik += 1
            n += 1

        else:
            n += 1
    return wynik

print(f("aeiouy"))

#Dobrze