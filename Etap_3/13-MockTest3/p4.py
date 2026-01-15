def f(fnc,res):

    lista = []
    for x in res:
        if fnc(x):
            lista.append(x)
    return max(lista) - min(lista)



res = [95,90,20,50,70]
fnc1 = lambda x: x>50
#f(fnc1,res) returns 25
#fnc2 = lambda x: x>30 and x<90
#f(fnc2,res) returns 20

print(f(fnc1, res))