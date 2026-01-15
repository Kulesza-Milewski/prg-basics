def pomoc(word,index):
    ref = list(word)
    ref[index] = ref[index].upper()
    wynik = "".join(ref)
    return wynik

def f(word):

    result = ""
    for i in range(len(word)):
        result = result + pomoc(word, i) + "-"

    return result[0:len(result)-1]

print(f("water"))