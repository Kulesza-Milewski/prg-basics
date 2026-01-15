def f(name):
    slowa = name.split()
    akronim = ""

    for slowo in slowa:
        pierwsza_litera = slowo[0]
        akronim += pierwsza_litera

    return akronim

print(f("Internet Of Things"))

# Błędy

"""
1. Nie dodałem () do split
2. W pętli for chciałem od razu dodać slowo[0] do akronim a nalerzało dodać pośrednika w formie pierwsza_litera
3. Ogólnie nie wiedziałem jak się do tego zabrać

"""