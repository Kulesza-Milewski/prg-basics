def f(first_letter, last_letter):
    with open('data.txt', 'r', encoding='utf-8') as file:
        tresc = file.read()
        tresc_lista = tresc.split()
        n = 0

        for word in tresc_lista:
            if word[0] == first_letter and word[-1] == last_letter:
                n += 1
    return n

print(f("w","d"))